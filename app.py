from flask import Flask, request, jsonify
from breeze_connect import BreezeConnect

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Nirved Sampatti Flask App is Running"

@app.route("/login", methods=["POST"])
def login():
    try:
        data = request.get_json()

        client_code = data.get("client_code")
        password = data.get("password")
        api_key = data.get("api_key")

        if not client_code or not password or not api_key:
            return jsonify({"error": "Missing credentials"}), 400

        breeze = BreezeConnect(api_key=api_key)
        breeze.generate_session(api_secret=password, session_token=client_code)

        return jsonify({"message": "Login successful ✅"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
