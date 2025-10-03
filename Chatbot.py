# Simple Rule-Based Chatbot using if-else

print("Welcome! Type 'bye' to exit the chat.")

while True:
    user_input = input("You: ").lower().strip()
    
    if user_input == "hi" or user_input == "hello":
        print("Bot: Hello! How can I help you today?")
    elif user_input == "how are you":
        print("Bot: I'm doing well, thank you! How are you?")
    elif user_input == "what is your name":
        print("Bot: I'm a simple rule-based chatbot created in Python.")
    elif user_input == "bye":
        print("Bot: Goodbye! Have a great day.")
        break
    else:
        print("Bot: Sorry, I didn't understand that. Please try again.")


