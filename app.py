from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Nirved Sampatti – Trading App Redirect Handler"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)