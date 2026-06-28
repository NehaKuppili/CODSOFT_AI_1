# 🤖 BuddyAI - NLP Intent Recognition Chatbot

BuddyAI is an AI-powered chatbot developed as part of the **CodSoft AI Internship**. It uses **Natural Language Processing (NLP)** to recognize user intents from natural language input and generate appropriate responses.

## 🚀 Features

- 🧠 Intent Recognition using NLP
- 💬 Natural language conversation
- 🔍 Text preprocessing
- 📝 Tokenization
- 🚫 Stopword removal
- 🌱 Word stemming
- 🎯 Keyword & Pattern Matching
- 🤝 User-friendly chat interface

## 🛠️ Technologies Used

- Python
- NLTK
- JSON
- Regular Expressions (Regex)
- Difflib
- Tkinter (GUI)

## 📂 Project Structure

```
BuddyAI/
│── chatbot.py
│── intents.json
│── gui.py
│── download_nltk.py
│── README.md
```

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/NehaKuppili/CODSOFT.git
```

### Install dependencies

```bash
pip install nltk
```

### Download NLTK resources

```bash
python download_nltk.py
```

### Run the chatbot

```bash
python gui.py
```

## 💻 How It Works

1. User enters a message.
2. The chatbot preprocesses the text by:
   - Converting to lowercase
   - Removing punctuation
   - Tokenizing words
   - Removing stopwords
   - Applying stemming
3. The processed text is compared with predefined intent patterns.
4. The closest matching intent is identified.
5. BuddyAI returns an appropriate response.

## 📌 Supported Intents

- Greetings
- Goodbye
- Thanks
- Help
- About
- Time
- Date
- Joke
- Motivation
- Programming
- AI
- Python
- Creator Information

## 📸 Sample Conversation

```
You: Hello
BuddyAI: Hi! How can I help you today?

You: Tell me a joke
BuddyAI: Why do programmers prefer dark mode? Because light attracts bugs!

You: What is AI?
BuddyAI: Artificial Intelligence enables machines to learn, reason, and solve problems.
```

## 🎯 Future Improvements

- Machine Learning-based intent classification
- Voice Assistant Integration
- Speech-to-Text Support
- Chat History
- Web Deployment

## 👩‍💻 Developed By

**Neha Kuppili**

AI & Machine Learning Student

## 📄 License

Developed for educational purposes as part of the **CodSoft AI Internship**.
