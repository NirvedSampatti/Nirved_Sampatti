import os
from flask import Flask, request, redirect

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return "Nirved Sampatti Flask App is Running"

# Login route to initiate ICICI Direct OAuth flow
@app.route("/login")
def login():
    client_id = "9021115667"  # 🔐 Replace with your actual ICICI client ID
    api_key = os.getenv("6R2647876651#k*JK859036`Nn464937")  # 🔐 Your ICICI API key from environment variables
    redirect_uri = "https://nirved-sampatti.onrender.com/callback"  # ✅ Match this with your ICICI developer portal
    response_type = "code"
    state = "nirved_secure_sampatti"  # Can be any string you use for tracking

    login_url = (
        f"https://api.icicidirect.com/apiuser/login"
        f"?client_id={client_id}"
        f"&redirect_uri={redirect_uri}"
        f"&response_type={response_type}"
        f"&state={state}"
        f"&api_key={api_key}"  # <-- Added API key here
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
