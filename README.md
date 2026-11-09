# Personal AI Chatbot Using Local LLM and LangChain Memory

## Project Description

This project is a simple personal AI chatbot developed using Python, Ollama, and LangChain. It uses the Gemma 3:1b language model to generate responses locally.

The chatbot remembers previous conversations using LangChain's InMemoryChatMessageHistory and provides context-aware answers to user questions.

## Technologies Used

- Python
- Ollama
- Gemma 3:1b
- LangChain
- Streamlit

## Features

- Answers general questions.
- Runs an AI model locally.
- Remembers previous conversations.
- Understands follow-up questions.
- Provides a user-friendly chatbot interface.
- Includes a Clear Conversation option.

## Project Structure

```text
Friend_AI_Chatbot/
│
├── app.py
├── requirements.txt
└── README.md
```

## Installation and Setup

### Step 1: Install Ollama

Download Ollama from:

https://ollama.com/

### Step 2: Download the Gemma Model

Open the terminal and run:

```bash
ollama pull gemma3:1b
```

### Step 3: Install Required Libraries

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

Execute the following command:

```bash
python -m streamlit run app.py
```

Open the chatbot in your browser:

```text
http://localhost:8501
```

## Example Conversation

**User:** My name is Shri.

**Bot:** Nice to meet you, Shri!

**User:** What is my name?

**Bot:** Your name is Shri.

## LangChain Memory

This project uses `InMemoryChatMessageHistory` to store user messages and AI responses.

It helps the chatbot remember previous conversations and answer follow-up questions using conversation history.

The memory is temporary and lasts during the active application session.

## Conclusion

This project demonstrates how to build a personal AI chatbot using a local Large Language Model and LangChain Memory. It provides interactive conversations, remembers previous messages, and generates context-aware responses.
