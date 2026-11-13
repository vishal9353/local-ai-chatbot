
# Local AI Chatbot 🤖

A locally running AI chatbot built using Python, LangChain,
Ollama, Llama 3.1 and Streamlit.

## Features
- Interactive web-based chatbot
- Local LLM inference using Ollama
- Conversation history
- No paid LLM API required

## Tech Stack
- Python
- Streamlit
- LangChain
- Ollama
- Llama 3.1 8B

## Architecture

User → Streamlit → LangChain → Ollama → Llama 3.1

## Screenshots

![Chatbot Screenshot](screenshots/chatbot.png)

## Installation

1. Clone the repository:

   git clone https://github.com/YOUR_USERNAME/local-ai-chatbot.git

2. Navigate to the project:

   cd local-ai-chatbot

3. Create a virtual environment:

   python -m venv chatbot

4. Activate it on Windows:

   chatbot\Scripts\activate

5. Install dependencies:

   pip install -r requirements.txt

6. Install Ollama and download the model:

   ollama pull llama3.1:8b

7. Run the application:

   streamlit run app.py

## Requirements

Ollama must be installed and running locally.
The Llama 3.1 8B model must be downloaded before
starting the chatbot.
