  from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "GoalGenieBot is Live!"

@app.route("/whatsapp/webhook", methods=["POST"])
def whatsapp_webhook():
    incoming_msg = request.form.get('Body', '').lower()
    if "goal" in incoming_msg:
        return jsonify({"message": "Got your goal! Generating recommendations..."})
    return jsonify({"message": "Please send your goal like: Goal 5000000, Tenure 7 years, SIP 100000, Risk Aggressive"})

if __name__ == "__main__":
    app.run(debug=True)
