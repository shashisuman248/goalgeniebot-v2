 from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "GoalGenieBot is Live!"

@app.route("/whatsapp/webhook", methods=["POST"])
def whatsapp_webhook():
    incoming_msg = request.form.get('Body', '').lower()

    if "goal" in incoming_msg:
        # Simple demo response
        return jsonify({"message": "📈 Based on your goal, we will recommend suitable mutual funds soon!"})
    
    return jsonify({
        "message": "❓ Please send your goal like this:\nGoal 5000000\nTenure 7 years\nSIP 100000\nRisk Aggressive"
    })

if __name__ == "__main__":
    app.run(debug=True)

