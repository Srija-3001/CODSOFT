import re
import random
from datetime import datetime

print("🤖 ChatBot: Hello! I am your Rule-Based ChatBot.")
print("🤖 ChatBot: Type 'bye' to exit.\n")

greetings = [
    "Hello! How can I help you?",
    "Hi there! What can I do for you today?",
    "Hey! Nice to meet you."
]

while True:
    user = input("You: ").lower().strip()

    # Greetings
    if re.search(r"\b(hi|hello|hey)\b", user):
        print("🤖 ChatBot:", random.choice(greetings))

    # How are you
    elif "how are you" in user or "how are" in user:
        print("🤖 ChatBot: I'm doing great! Thanks for asking.")

    # Name
    elif "your name" in user or "who are you" in user:
        print("🤖 ChatBot: I am a Rule-Based AI ChatBot created using Python.")

    # Time
    elif "time" in user:
        current_time = datetime.now().strftime("%H:%M:%S")
        print("🤖 ChatBot: Current time is", current_time)

    # Date
    elif "date" in user:
        current_date = datetime.now().strftime("%d-%m-%Y")
        print("🤖 ChatBot: Today's date is", current_date)

    # AI
    elif "ai" in user or "artificial intelligence" in user:
        print("🤖 ChatBot: Artificial Intelligence enables machines to simulate human intelligence.")

    # Machine Learning
    elif "machine learning" in user:
        print("🤖 ChatBot: Machine Learning is a branch of AI that helps computers learn from data.")

    # Python
    elif "python" in user:
        print("🤖 ChatBot: Python is a popular programming language used in AI, ML, web development, and more.")

    # College
    elif "college" in user:
        print("🤖 ChatBot: College is a great place to learn new skills and build your career.")

    # Hyderabad
    elif "hyderabad" in user:
        print("🤖 ChatBot: Hyderabad is the capital city of Telangana and a major IT hub.")

    # Weather
    elif "weather" in user or "temperature" in user:
        print("🤖 ChatBot: Sorry, I cannot provide live weather updates because I am a rule-based chatbot.")

    # Calculator
    elif user.startswith("calculate"):
        try:
            expression = user.replace("calculate", "").strip()
            result = eval(expression)
            print("🤖 ChatBot: The answer is", result)
        except:
            print("🤖 ChatBot: Please enter a valid mathematical expression.")

    # Thanks
    elif "thank" in user:
        print("🤖 ChatBot: You're welcome!")

    # Help
    elif "help" in user:
        print("🤖 ChatBot: You can ask me about AI, Python, Machine Learning, Date, Time, Weather, Hyderabad, or use 'calculate 5+3'.")

    # Exit
    elif user in ["bye", "exit", "quit"]:
        print("🤖 ChatBot: Goodbye! Have a nice day!")
        break

    # Default
    else:
        print("🤖 ChatBot: Sorry, I don't understand that yet. Type 'help' to see what I can do.")