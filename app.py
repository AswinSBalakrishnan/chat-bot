from flask import Flask, render_template, request
from chatbot import get_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def chat():
    user_message = request.form["user_message"]
    bot_response = get_response(user_message)
    return bot_response

if __name__ == "__main__":
    app.run(debug=True)
