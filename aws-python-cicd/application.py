from flask import Flask, jsonify
import logging

application = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@application.route("/")
def home():
    logging.info("Home page visited")
    return "Python Flask App Deployed Successfully using AWS CI/CD Pipeline!"

@application.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "message": "Application is running"
    })

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5000)