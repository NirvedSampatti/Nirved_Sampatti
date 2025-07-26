import os
from flask import Flask, request, redirect

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")  # ✅ Recommended

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

@app.route("/callback")
def callback():
    args = request.args.to_dict()
    if "code" in args:
        return f"Authorization Code: {args.get('code')}, State: {args.get('state', 'None')}"
    else:
        # Show all query params for debugging
        return f"No authorization code found. Parameters received: {args}", 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
