from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Nirved Sampatti Flask App is Running"

@app.route("/callback", methods=["GET", "POST"])
def callback():
    code = request.args.get("code") or request.form.get("code")
    if code:
        return f"Authorization Code: {code}"
    return "Authorization code not found", 400

if __name__ == "__main__":
    app.run()