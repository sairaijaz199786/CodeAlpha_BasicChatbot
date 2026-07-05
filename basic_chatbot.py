import random
from datetime import datetime
print("=" * 50)
print("🤖 Welcome to Smart Chatbot 🤖")
print("=" * 50)
name = input("Enter your name: ").title()
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
print("\n-----------------------------")
print("Available Commands:")
print("hello / hi / hey")
print("how are you")
print("time")
print("date")
print("joke")
print("quote")
print("python")
print("calculator")
print("bye / exit")
print("-----------------------------")
while True:
    user = input(f"\n{name}: ").strip().lower()
    if user in ["hello", "hi", "hey", "hii", "hy"]:
        print("Bot: Hello! Nice to meet you. 😊")
    elif user in ["how are you", "how are u", "how r you"]:
        print("Bot: I am fine. Thanks for asking! 😊")
    elif user in ["time", "current time", "what is the time"]:
        print("Bot:", datetime.now().strftime("%I:%M %p"))
    elif user in ["date", "today date", "today's date"]:
        print("Bot:", datetime.now().strftime("%d-%m-%Y"))
    elif user in ["joke", "tell me a joke"]:
        print("Bot:", random.choice(jokes))
    elif user in ["quote", "motivation", "motivational quote"]:
        print("Bot:", random.choice(quotes))
    elif user in ["python", "what is python"]:
        print("Bot: Python is a powerful and beginner-friendly programming language.")
    elif user in ["calculator", "calculate", "calc"]:
        try:
            num1 = float(input("Enter first number: "))
            operator = input("Enter operator (+ - * /): ").strip()
            num2 = float(input("Enter second number: "))
            if operator == "+":
                print("Result =", num1 + num2)
            elif operator == "-":
                print("Result =", num1 - num2)
            elif operator == "*":
                print("Result =", num1 * num2)
            elif operator == "/":
                if num2 == 0:
                    print("Bot: Cannot divide by zero.")
                else:
                    print("Result =", num1 / num2)
            else:
                print("Bot: Invalid operator.")
        except ValueError:
            print("Bot: Please enter valid numbers.")
    elif user in ["bye", "goodbye", "exit", "quit"]:
        print(f"Bot: Goodbye {name}! Have a nice day. 😊")
        break
    else:
        print("Bot: Sorry! I don't understand that command. Please try again.")