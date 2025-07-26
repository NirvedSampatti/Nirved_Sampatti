from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Nirved Sampatti – Trading App Redirect Handler"

@app.route('/redirect')
def handle_redirect():
    code = request.args.get('code')
    state = request.args.get('state')
    return f"ICICI Redirect Received – Code: {code}, State: {state}"
    
if __name__ == "__main__":
    app.run()
