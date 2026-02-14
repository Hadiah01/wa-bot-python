from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = "yoga_bot_123"

@app.route("/", methods=["GET"])
def verify():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode and token:
        if mode == "subscribe" and token == VERIFY_TOKEN:
            return challenge, 200
        else:
            return "Verification failed", 403

    return "Hello", 200

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()
    print(data)
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
