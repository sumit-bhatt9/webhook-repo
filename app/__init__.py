import os
from flask import Flask
from app.webhook.routes import webhook

def create_app():
    # Explicitly set the path to the templates folder
    base_dir = os.path.abspath(os.path.dirname(__file__))
    templates_dir = os.path.join(base_dir, "..", "templates")
    
    # Initialize Flask app with the custom templates directory
    app = Flask(__name__, template_folder=templates_dir)

    # Register the webhook blueprint (routes)
    app.register_blueprint(webhook)

    return app