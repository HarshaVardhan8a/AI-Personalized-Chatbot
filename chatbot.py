# chatbot.py

import random
import datetime

# Log file setup
LOG_FILE = "chat_log.txt"

def log_message(role, message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as file:
        file.write(f"[{timestamp}] {role}: {message}\n")

def greet():
    return random.choice(["Hi there!", "Hello!", "Hey!", "Welcome!"])

def farewell():
    return random.choice(["Goodbye!", "See you later!", "Take care!", "Bye!"])

def get_time():
    return f"The current time is {datetime.datetime.now().strftime('%I:%M %p')}"

def get_date():
    return f"Today's date is {datetime.date.today().strftime('%B %d, %Y')}"

def tell_joke():
    return random.choice([
        "Why did the Python developer go broke? Because he couldn't find his 'cache'!",
        "Why do programmers prefer dark mode? Because the light attracts bugs!",
        "Why was the JavaScript file so sad? Because it didn’t know how to ‘null’ its feelings!"
    ])

def motivate():
    return random.choice([
        "Keep pushing forward, you’re doing great!",
        "Every expert was once a beginner. Keep learning!",
        "Your hard work will pay off. Believe in yourself!"
    ])

def get_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input or "hey" in user_input:
        return greet()
    elif "your name" in user_input or "who are you" in user_input:
        return "I'm CodBot, your friendly AI chatbot for CodSoft internship."
    elif "help" in user_input:
        return "I can chat, tell jokes, share the time/date, motivate you, and guide you about internships."
    elif "internship" in user_input:
        return "CodSoft internships offer tasks in AI, web dev, and more. Visit https://www.codsoft.in"
    elif "bye" in user_input or "exit" in user_input:
        return farewell()
    elif "time" in user_input:
        return get_time()
    elif "date" in user_input:
        return get_date()
    elif "joke" in user_input or "funny" in user_input:
        return tell_joke()
    elif "motivate" in user_input or "inspire" in user_input:
        return motivate()
    else:
        return "I'm not sure how to respond to that. Can you try asking something else?"

def chatbot():
    print("="*50)
    print("🤖 CodBot - AI Chatbot for CodSoft Internship")
    print("Type 'exit' anytime to end the chat.")
    print("="*50)

    with open(LOG_FILE, "a") as file:
        file.write("\n--- New Chat Session Started ---\n")

    while True:
        user_input = input("👤 You: ")
        log_message("User", user_input)

        if user_input.lower() in ['exit', 'bye']:
            bot_response = farewell()
            print(f"🤖 CodBot: {bot_response}")
            log_message("CodBot", bot_response)
            break

        bot_response = get_response(user_input)
        print(f"🤖 CodBot: {bot_response}\n")
        log_message("CodBot", bot_response)

if __name__ == "__main__":
    chatbot()