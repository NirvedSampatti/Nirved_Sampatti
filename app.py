from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Nirved Sampatti – Trading App Redirect Handler"