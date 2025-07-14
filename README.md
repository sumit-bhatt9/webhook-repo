README.md

```markdown
# ✅ Techstax Dev Assessment – Webhook Receiver (Final Submission)

This Flask-based application receives GitHub webhook events (`push`, `pull_request`, and `merge`), stores them in MongoDB, and displays them live on a frontend UI that refreshes every 15 seconds.

---

## 🚀 Features Implemented

- GitHub webhook receiver for:
  - ✅ Push events
  - ✅ Pull request (opened)
  - ✅ Merge (pull request closed + merged)
- Stores events in MongoDB
- Frontend UI auto-refreshes every 15 seconds
- Timestamps formatted as: "Travis pushed to staging on 1st April 2021 - 9:30 PM UTC"

- Modular Flask blueprint architecture

---

## 🧱 Tech Stack

- Python + Flask
- MongoDB (local)
- Flask-PyMongo
- HTML + JavaScript
- Ngrok (for testing webhooks from GitHub)

---
```
## 🛠 Setup Instructions

1. Clone this repository:

```bash
git clone https://github.com/sumit-bhatt9/webhook-repo.git
cd webhook-repo
````

2. Create and activate a virtual environment:

```bash
pip install virtualenv
virtualenv venv
# On Windows
.\venv\Scripts\activate
# On Mac/Linux
source venv/bin/activate
```

3. Install all required packages:

```bash
pip install -r requirements.txt
```

4. Start your local MongoDB instance.

5. Run the Flask application:

```bash
python run.py
```

6. (Optional) Use ngrok to expose localhost:

```bash
ngrok http 5000
```

7. Set your GitHub Webhook to:

```
https://<your-ngrok-subdomain>.ngrok-free.app/webhook/receiver
```

---

## 🌐 Endpoint Summary

| Method | Endpoint          | Description                    |
| ------ | ----------------- | ------------------------------ |
| POST   | /webhook/receiver | Receives GitHub webhook events |
| GET    | /webhook/         | Displays frontend UI           |
| GET    | /webhook/events   | Sends JSON list of events      |

---

## 🖥️ UI Behavior

* The index.html page shows the most recent webhook events.
* Updates every 15 seconds via JavaScript polling.
* Event formats:

  * Push:

    ```
    {author} pushed to {to_branch} on {timestamp}
    ```

  * Pull Request:

    ```
    {author} submitted a pull request from {from_branch} to {to_branch} on {timestamp}
    ```

  * Merge:

    ```
    {author} merged branch {from_branch} to {to_branch} on {timestamp}
    ```

---

## 📂 Project Structure

```
webhook-repo/
│
├── app/
│   ├── __init__.py            # Flask app factory with template path
│   ├── extensions.py          # MongoDB connection
│   └── webhook/
│       └── routes.py          # Webhook + frontend routes
│
├── templates/
│   └── index.html             # Frontend UI
│
├── run.py                     # App entry point
├── requirements.txt
└── README.md
```
