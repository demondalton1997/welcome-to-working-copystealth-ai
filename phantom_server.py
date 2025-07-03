# phantom_server.py
from flask import Flask, request, jsonify
from modules import logger

app = Flask(__name__)

@app.route("/")
def home():
    logger.log_event("Accessed home route")
    return "Phantom Server is Live"

@app.route("/log", methods=["POST"])
def log_event():
    data = request.json
    logger.log_event(data.get("event", "No event provided"))
    return jsonify({"status": "logged"})

if __name__ == "__main__":
    app.run(port=8080)
