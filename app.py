from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Nirved Sampatti is Live and Working!"