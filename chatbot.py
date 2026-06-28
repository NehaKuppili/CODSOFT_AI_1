import json
import random
import re
import difflib
from datetime import datetime

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Load intents
with open("intents.json", "r") as file:
    data = json.load(file)

# NLP Setup
stop_words = set(stopwords.words("english"))
stemmer = PorterStemmer()


# -------------------------------
# Text Preprocessing
# -------------------------------
def preprocess(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)

    words = word_tokenize(text)

    words = [
        stemmer.stem(word)
        for word in words
        if word not in stop_words
    ]

    return " ".join(words)


# -------------------------------
# Intent Detection
# -------------------------------
def detect_intent(user_input):

    best_intent = None
    highest_score = 0

    for intent in data["intents"]:

        for pattern in intent["patterns"]:

            processed_pattern = preprocess(pattern)

            # Exact Match
            if user_input == processed_pattern:
                return intent

            # Keyword Match
            user_words = set(user_input.split())
            pattern_words = set(processed_pattern.split())

            score = len(user_words.intersection(pattern_words))

            if score > highest_score:
                highest_score = score
                best_intent = intent

            # Fuzzy Match
            similarity = difflib.SequenceMatcher(
                None,
                user_input,
                processed_pattern
            ).ratio()

            if similarity > 0.80:
                highest_score = 100
                best_intent = intent

    return best_intent


# -------------------------------
# Response Function
# -------------------------------
def get_response(user):

    if user.lower() in ["exit", "quit"]:
        return "Goodbye! 👋"

    processed_input = preprocess(user)

    intent = detect_intent(processed_input)

    if intent:

        tag = intent["tag"]

        if tag == "time":
            return datetime.now().strftime("%I:%M:%S %p")

        elif tag == "date":
            return datetime.now().strftime("%d %B %Y")

        else:
            return random.choice(intent["responses"])

    return "🤔 Sorry, I couldn't understand that. Try asking in another way."


# -------------------------------
# Terminal Mode
# -------------------------------
if __name__ == "__main__":

    print("=" * 60)
    print("🤖 BuddyAI - NLP Intent Recognition Chatbot")
    print("=" * 60)
    print("Type 'exit' anytime to quit.\n")

    while True:

        user = input("You : ")

        if user.lower() in ["exit", "quit"]:
            print("BuddyAI : Goodbye! 👋")
            break

        print("BuddyAI :", get_response(user))