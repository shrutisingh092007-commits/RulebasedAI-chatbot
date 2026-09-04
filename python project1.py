def chatbot():
    print("Chatbot:Hello ! I am a rule-based AI chatbot.")
    print("Chatbot:Type 'bye' or 'exit' to end the conversation.")

    while True:
        user_input = input("you:").lower().strip()

        if user_input in ["bye","exit","quit"]:
            print("Chatbot: Goodbye! Have a great day !")
            break
        elif user_input in ["hi", "hello","hey"]:
            print("Chatbot:Hello! How can i help you?")

        elif"how are you" in user_input:
            print("Chatbot: Iam doing well. Thabks for asking!")

        elif"your name " in user_input:
            print("Chatbot: I am a rule based AI Chatbot")

        elif"help" in user_input:
            print("Chatbot: YOU can greet me, ask my name, or say bye to exit.")

        else:
            print("Chatbot:Sorry, I don't understand that yet.") 

            if __name__ == "__main__":
                chatbot()           