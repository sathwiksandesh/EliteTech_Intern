pip install nltk
import nltk
nltk.download('punkt')
import nltk
from nltk.tokenize import word_tokenize
# Predefined intents with keywords and responses
intents = {
    'greeting': {
        'keywords': ['hello', 'hi', 'hey', 'greetings'],
        'responses': ['Hello!', 'Hi there!', 'Hey! How can I help you?']
    },
    'goodbye': {
        'keywords': ['bye', 'goodbye', 'see you', 'exit', 'quit'],
        'responses': ['Goodbye!', 'See you later!', 'Have a nice day!']
    },
    'thanks': {
        'keywords': ['thanks', 'thank you', 'thx'],
        'responses': ['You\'re welcome!', 'No problem!', 'Anytime!']
    },
    'hours': {
        'keywords': ['hours', 'open', 'close', 'time'],
        'responses': ['We are open from 9 AM to 5 PM, Monday to Friday.']
    },
    'name': {
        'keywords': ['your name', 'who are you'],
        'responses': ['I am a simple chatbot built with NLTK.']
    }
}
import random

def preprocess(text):
    # Tokenize and lowercase
    tokens = word_tokenize(text.lower())
    return tokens

def get_intent(tokens):
    for intent, data in intents.items():
        for keyword in data['keywords']:
            # Check if any keyword is in user tokens
            if keyword in tokens or ' '.join(tokens).find(keyword) != -1:
                return intent
    return None

def chatbot():
    print("Chatbot: Hello! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Chatbot: Goodbye! Have a great day!")
            break

        tokens = preprocess(user_input)
        intent = get_intent(tokens)

        if intent:
            response = random.choice(intents[intent]['responses'])
            print("Chatbot:", response)
        else:
            print("Chatbot: Sorry, I didn't understand that. Can you rephrase?")

if __name__ == "__main__":
    chatbot()
