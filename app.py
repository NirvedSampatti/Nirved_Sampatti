from flask import Flask

app = Flask(__name__)

@app.route("/nirvedsampatti/")
def home():
    return "Nirved Sampatti is live at /nirvedsampatti!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)