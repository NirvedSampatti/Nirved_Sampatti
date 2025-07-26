import os
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "Nirved Sampatti Flask App is Running"

@app.route("/login", methods=["POST"])
def login():
    data = request.json

    # Check if JSON body has required keys
    required_keys = ["clientCode", "password", "apiKey"]
    if not data or not all(key in data for key in required_keys):
        return jsonify({"error": "Missing clientCode, password or apiKey in JSON body"}), 400

    clientCode = data["clientCode"]
    password = data["password"]
    apiKey = data["apiKey"]

    # Breeze Connect login endpoint
    login_url = "https://api.icicidirect.com/breezeapi/apiuser/login"

    # Prepare payload according to ICICI Breeze docs
    payload = {
        "clientCode": clientCode,
        "password": password,
        "apiKey": apiKey
    }

    try:
        # Send POST request to ICICI Breeze Connect login API
        response = requests.post(login_url, json=payload)

        # Forward the response JSON from ICICI to the client
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    # Run on port 5000 on all IPs, debug True for development
    app.run(host="0.0.0.0", port=5000, debug=True)
