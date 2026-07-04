from flask import Flask, render_template, request
import random
from datetime import datetime
app = Flask(__name__)
jokes = [
    "Why do programmers love Python? Because it is easy to learn! 😄",
    "Debugging is like being a detective in a crime movie. 😂",
    "A programmer's favorite place is the loop! 🤣"
]
quotes = [
    "Success comes from consistency.",
    "Keep learning every day.",
    "Dream big, work hard.",
    "Every expert was once a beginner."
]
@app.route("/", methods=["GET", "POST"])
def home():
    response = ""
    if request.method == "POST":
        user = request.form["message"].lower()
        if user == "hello":
            response = "Hello! Nice to meet you."
        elif user == "how are you":
            response = "I am fine. Thanks for asking!"
        elif user == "time":
            response = datetime.now().strftime("%I:%M %p")
        elif user == "date":
            response = datetime.now().strftime("%d-%m-%Y")
        elif user == "joke":
            response = random.choice(jokes)
        elif user == "quote":
            response = random.choice(quotes)
        elif user == "python":
            response = "Python is a powerful and beginner-friendly programming language."
        elif user == "bye":
            response = "Goodbye! Have a nice day. 😊"
        else:
            response = "Sorry! I don't understand that command."
    return render_template("index.html", response=response)
if __name__ == "__main__":
    app.run(debug=True)