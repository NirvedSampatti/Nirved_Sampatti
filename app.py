from flask import Flask, request, redirect

app = Flask(__name__)  # ✅ Correct Flask app initialization

@app.route("/")
def home():
    return "Welcome to Nirved Sampatti!"

@app.route("/login")
def login():
    client_id = "9021115667"  # ✅ Your ICICI client ID
    redirect_uri = "https://nirvedsampatti.onrender.com/callback"
    response_type = "code"
    state = "nirved_secure_sampatti"  # ✅ Custom state string

    login_url = (
        f"https://api.icicidirect.com/apiuser/login?"
        f"client_id={client_id}&"
        f"redirect_uri={redirect_uri}&"
        f"response_type={response_type}&"
        f"state={state}"
    )

    return redirect(login_url)

@app.route("/callback")
def callback():
    code = request.args.get("code")
    state = request.args.get("state")

    return f"Authorization code: {code}, State: {state}"

if __name__ == "__main__":
    app.run(debug=True)