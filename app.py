from flask import Flask, request, redirect

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return "Nirved Sampatti Flask App is Running"

# Login route to initiate ICICI Direct OAuth flow
@app.route("/login")
def login():
    client_id = "My Client ID"  # 🔐 <-- Replace with your ICICI client ID 
    redirect_uri = "https://nirvedsampatti.onrender.com/callback"  # ✅ <-- Your actual Render URL
    response_type = "code"
    state = "nirved_secure_sampatti"  # You can change this to any string 

    login_url = (
        f"https://api.icicidirect.com/apiuser/login"
        f"?client_id={client_id}"
        f"&redirect_uri={redirect_uri}"
        f"&response_type={response_type}"
        f"&state={state}"
    )
    return redirect(login_url)

# Callback route to receive authorization code from ICICI Direct
@app.route("/callback", methods=["GET", "POST"])
def callback():
    code = request.args.get("code") or request.form.get("code")
    if code:
        return f"Authorization Code: {code}"
    return "Authorization code not found", 400

if __name__ == "__main__":
    app.run()

