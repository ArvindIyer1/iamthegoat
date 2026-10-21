print("========================================")
print(" Welcome to AI Rule-Based Chatbot")
print("Type 'bye' to end the conversation.")
print("========================================")

while True:
    user_input = input("\nYou: ").lower().strip()

    if user_input == "hello" or user_input == "hi":
        print("Bot: Hello! How can I help you?")

    elif user_input == "how are you":
        print("Bot: I am fine. Thank you!")

    elif user_input == "what is your name":
        print("Bot: My name is AI Chatbot.")

    elif user_input == "who developed you":
        print("Bot: I was developed for learning AI.")

    elif user_input == "what is ai":
        print("Bot: AI stands for Artificial Intelligence.")

    elif user_input == "help":
        print("Bot: I can answer simple questions.")

    elif user_input == "thanks" or user_input == "thank you":
        print("Bot: You're welcome!")

    elif user_input == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand your question.")