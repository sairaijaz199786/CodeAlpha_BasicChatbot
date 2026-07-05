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
        user = request.form["message"].strip().lower()
        if user in ["hello", "hi", "hey", "hii", "hy"]:
            response = "Hello! Nice to meet you. 😊"
        elif user in ["how are you", "how are u", "how r you"]:
            response = "I am fine. Thanks for asking! 😊"
        elif user in ["time", "current time", "what is the time"]:
            response = datetime.now().strftime("%I:%M %p")
        elif user in ["date", "today date", "today's date"]:
            response = datetime.now().strftime("%d-%m-%Y")
        elif user in ["joke", "tell me a joke"]:
            response = random.choice(jokes)
        elif user in ["quote", "motivation", "motivational quote"]:
            response = random.choice(quotes)
        elif user in ["python", "what is python"]:
            response = "Python is a powerful and beginner-friendly programming language."
        elif user in ["bye", "goodbye", "exit", "quit"]:
            response = "Goodbye! Have a nice day. 😊"
        # Calculator
        elif any(op in user for op in ["+", "-", "*", "/"]):
            try:
                result = eval(user)
                if isinstance(result, float):
                    result = round(result, 2)
                response = f"Result = {result}"
            except ZeroDivisionError:
                response = "Cannot divide by zero."
            except:
                response = "Invalid calculation. Example: 5+3"
        else:
            response = "Sorry! I don't understand that command."
    return render_template("index.html", response=response)
if __name__ == "__main__":
    app.run(debug=True)