import re

def respond(message):
    """Responds to a user message based on predefined rules.

    Args:
        message: The user's input message.

    Returns:
        A string containing the chatbot's response.
    """

    # Greetings
    if re.match(r"hi|hello|hey", message.lower()):
        return "Hi there! How can I help you today?"

    # Questions about the bot
    elif re.search(r"what are you|who are you", message.lower()):
        return "I'm a simple rule-based chatbot designed to understand basic phrases and provide responses based on predefined rules. Ask me anything!"

    # Questions about capabilities
    elif re.search(r"what can you do|what do you know", message.lower()):
        return "I can answer basic questions, respond to greetings, and understand simple requests. While I'm still learning, I'm always getting better!"

    # Thank you
    elif re.search(r"thank you", message.lower()):
        return "You're welcome! I'm glad I could help."

    # Goodbye
    elif re.search(r"bye|good bye|see you later", message.lower()):
        return "Bye! Have a great day!"

    # Acknowledgements
    elif re.search(r"you're welcome|no problem", message.lower()):
        return ""

    # Love you greetings
    elif re.search(r"love you", message.lower()):
        return "I love you too!!"

    # Default response (learn to recognize more patterns and expand responses)
    else:
        return "I'm still learning new things. Could you rephrase your question or try asking something else?"

# Start the conversation
print("Hello! I'm a chatbot. You can start chatting with me. Type 'exit' to end the conversation.")

while True:
    user_message = input("> ")
    bot_response = respond(user_message.lower())
    print(bot_response)

    # Allow for multiple exchanges before exiting
    if re.search(r"bye|exit", user_message.lower()):
        break
    else:
        print("\n")