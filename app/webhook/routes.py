from flask import Blueprint, request, jsonify, render_template
from datetime import datetime
from app.extensions import get_collection

webhook = Blueprint('webhook', __name__, url_prefix='/webhook')

collection = get_collection()

@webhook.route('/receiver', methods=["POST"])
def receiver():
    event = request.headers.get('X-GitHub-Event')
    payload = request.json
    print("Received event:", event)

    data = None

    if event == "push":
        data = {
            "type": "push",
            "author": payload["pusher"]["name"],
            "to_branch": payload["ref"].split("/")[-1],
            "timestamp": datetime.utcnow()
        }
    elif event == "pull_request" and payload["action"] == "opened":
        data = {
            "type": "pull_request",
            "author": payload["pull_request"]["user"]["login"],
            "from_branch": payload["pull_request"]["head"]["ref"],
            "to_branch": payload["pull_request"]["base"]["ref"],
            "timestamp": datetime.utcnow()
        }
    elif event == "pull_request" and payload["action"] == "closed" and payload["pull_request"]["merged"]:
        data = {
            "type": "merge",
            "author": payload["pull_request"]["user"]["login"],
            "from_branch": payload["pull_request"]["head"]["ref"],
            "to_branch": payload["pull_request"]["base"]["ref"],
            "timestamp": datetime.utcnow()
        }

    if data:
        collection.insert_one(data)
        print("Event stored successfully")
        return jsonify({"message": "Event stored"}), 200
    else:
        return jsonify({"message": "Event not handled"}), 200

@webhook.route("/", methods=["GET"])
def homepage():
    return render_template("index.html")

@webhook.route("/events", methods=["GET"])
def get_events():
    events = list(collection.find({}, {"_id": 0}))
    return jsonify(events)
