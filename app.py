from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Nirved Sampatti Flask App is Running"

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    clientCode = data.get("clientCode")
    password = data.get("password")
    apiKey = data.get("apiKey")

    if not clientCode or not password or not apiKey:
        return jsonify({"error": "Missing clientCode, password or apiKey"}), 400

    return jsonify({
        "message": "Received credentials",
        "clientCode": clientCode,
        "password": password,
        "apiKey": apiKey
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
