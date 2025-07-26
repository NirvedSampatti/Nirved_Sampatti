from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Nirved Sampatti Flask App is Running 🚀'

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    clientCode = data.get('clientCode')
    password = data.get('password')
    apiKey = data.get('apiKey')

    # Basic dummy check
    if clientCode and password and apiKey:
        return jsonify({
            "message": "Login Successful",
            "token": "dummy_token_example"
        }), 200
    else:
        return jsonify({"error": "Missing credentials"}), 400