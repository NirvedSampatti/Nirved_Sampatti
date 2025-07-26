import os
import urllib.parse
from flask import Flask, request, redirect

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")  # Recommended for security

@app.route("/")
def home():
    return "Nirved Sampatti Flask App is Running"

@app.route("/login")
def login():
    client_id = os.getenv("ICICI_CLIENT_ID")
    api_key = os.getenv("ICICI_API_KEY")

    if not client_id or not api_key:
        return "Missing ICICI_CLIENT_ID or ICICI_API_KEY in environment variables", 500

    redirect_uri = "https://nirved-sampatti.onrender.com/callback"
    redirect_uri_encoded = urllib.parse.quote(redirect_uri, safe='')

    response_type = "code"
    state = "nirved_secure_sampatti"

    login_url = (
        f"https://api.icicidirect.com/apiuser/login"
        f"?client_id={client_id}"
        f"&redirect_uri={redirect_uri_encoded}"
        f"&response_type={response_type}"
        f"&state={state}"
        f"&api_key={api_key}"
    )

    return redirect(login_url)

@app.route("/callback", methods=["GET"])
def callback():
    code = request.args.get("code")
    state = request.args.get("state")

    if code:
        return f"Authorization Code: {code}, State: {state}"
    else:
        return "Authorization code not found", 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
