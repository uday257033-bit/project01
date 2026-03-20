import random

# Predefined responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey! How can I help you?"],
    "how are you": ["I'm fine!", "Doing great!", "All good!"],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "name": ["I am your chatbot!", "You can call me Python Bot."],
}

# Default responses if no match
default_responses = [
    "I don't understand that.",
    "Can you say that again?",
    "Interesting... tell me more!",
]

# Chat function
def chatbot():
    print("🤖 Chatbot: Hello! Type 'exit' to quit.\n")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input == "exit":
            print("🤖 Chatbot: Goodbye!")
            break
        
        found = False
        
        for key in responses:
            if key in user_input:
                print("🤖 Chatbot:", random.choice(responses[key]))
                found = True
                break
        
        if not found:
            print("🤖 Chatbot:", random.choice(default_responses))

# Run chatbot
chatbot()