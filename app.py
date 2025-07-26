import os
from flask import Flask, request, redirect
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return "Nirved Sampatti Flask App is Running"

# Login route to initiate ICICI Direct OAuth flow
@app.route("/login")
def login():
    client_id = os.getenv("ICICI_CLIENT_ID")   # ✅ Reads from .env variable
    api_key = os.getenv("ICICI_API_KEY")       # ✅ Reads from .env variable
    redirect_uri = "https://nirved-sampatti.onrender.com/callback"
    response_type = "code"
    state = "nirved_secure_sampatti"

    login_url = (
        f"https://api.icicidirect.com/apiuser/login"
        f"?client_id={client_id}"
        f"&redirect_uri={redirect_uri}"
        f"&response_type={response_type}"
        f"&state={state}"
        f"&api_key={api_key}"
    )

    return redirect(login_url)

# Callback route to receive authorization code from ICICI Direct
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
