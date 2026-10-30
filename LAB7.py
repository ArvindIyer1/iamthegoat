print("=" * 40)
print("Welcome to AI Rule-Based Chatbot")
print("Type 'bye' to end the conversation.")
print("=" * 40)

while True:
    user = input("\nYou: ").lower().strip()

    if user in ("hello", "hi"):
        print("Bot: Hello! How can I help you?")
    elif user == "how are you":
        print("Bot: I am fine. Thank you!")
    elif user == "what is your name":
        print("Bot: My name is AI Chatbot.")
    elif user == "who developed you":
        print("Bot: I was developed for learning Artificial Intelligence.")
    elif user == "what is ai":
        print("Bot: AI stands for Artificial Intelligence.")
    elif user == "help":
        print("Bot: I can answer simple predefined questions.")
    elif user in ("thanks", "thank you"):
        print("Bot: You're welcome!")
    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break
    else:
        print("Bot: Sorry, I don't understand your question.")
