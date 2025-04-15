import nltk
from nltk.chat.util import Chat, reflections

# Ensure that necessary NLTK datasets are downloaded
nltk.download('punkt')

# Define the chatbot's response patterns
patterns = [
    (r"Hi|Hello|Hey", ["Hello! How can I help you today?", "Hi there! How can I assist you?"]),
    (r"(.*) your name ?", ["I am a simple chatbot created using NLTK.", "You can call me Chatbot!"]),
    (r"(.*) help(.*)", ["I can help you with basic questions. Just ask me anything!", "Sure! How can I assist you today?"]),
    (r"How are you?", ["I'm just a program, but I'm doing great! How are you?", "I'm good, thanks for asking!"]),
    (r"Bye|Goodbye", ["Goodbye! Have a great day!", "See you later!"]),
    (r"(.*)", ["Sorry, I didn't quite understand that. Can you rephrase?", "Could you please ask something else?"]),
]

# Create the chatbot with the defined patterns
chatbot = Chat(patterns, reflections)

def start_chat():
    print("Chatbot: Hello! Type 'Bye' or 'Goodbye' to end the conversation.")
    print("Chatbot: How can I help you today?")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ['bye', 'goodbye']:
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    start_chat()
