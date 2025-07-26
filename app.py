import os
from flask import Flask, request, redirect
from urllib.parse import urlencode

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "dev_secret_key_for_testing")  # fallback for dev only

@app.route("/")
def home():
    return "Nirved Sampatti Flask App is Running"

@app.route("/login")
def login():
    client_id = os.getenv("ICICI_CLIENT_ID")
    api_key = os.getenv("ICICI_API_KEY")

    if not client_id or not api_key:
        return "Missing ICICI_CLIENT_ID or ICICI_API_KEY in environment variables", 500

    params = {
        "client_id": client_id,
        "redirect_uri": "https://nirved-sampatti.onrender.com/callback",
        "response_type": "code",
        "state": "nirved_secure_sampatti",
        "api_key": api_key
    }

    login_url = "https://api.icicidirect.com/apiuser/login?" + urlencode(params)
    return redirect(login_url)

@app.route("/callback")
def callback():
    code = request.args.get("code")
    state = request.args.get("state")

    if code:
        return f"Authorization Code: {code}, State: {state}"
    else:
        return "Authorization code not found", 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
