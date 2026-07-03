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
print("hello")
print("how are you")
print("time")
print("date")
print("joke")
print("quote")
print("python")
print("calculator")
print("bye")
print("-----------------------------")

while True:
    user = input(f"\n{name}: ").lower()



    if user == "hello":
        print("Bot: Hello! Nice to meet you.")

    elif user == "how are you":
        print("Bot: I am fine. Thanks for asking!")

    elif user == "time":
        print("Bot:", datetime.now().strftime("%I:%M %p"))

    elif user == "date":
        print("Bot:", datetime.now().strftime("%d-%m-%Y"))

    elif user == "joke":
        print("Bot:", random.choice(jokes))

    elif user == "quote":
        print("Bot:", random.choice(quotes))

    elif user == "python":
        print("Bot: Python is a powerful and beginner-friendly programming language.")

    elif user == "calculator":

        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+ - * /): ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            print("Result =", num1 + num2)

        elif operator == "-":
            print("Result =", num1 - num2)

        elif operator == "*":
            print("Result =", num1 * num2)

        elif operator == "/":
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                print("Result =", num1 / num2)

        else:
            print("Invalid operator.")

    elif user == "bye":
        print(f"Bot: Goodbye {name}! Have a nice day. 😊")
        break

    else:
        print("Bot: Sorry! I don't understand that command.")