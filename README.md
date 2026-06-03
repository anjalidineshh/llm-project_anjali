# Task 1 - Simple AI Chatbot

## Problem Statement
The objective of this task was to build a conversational AI chatbot using the Groq API and a Large Language Model (LLM) that can process user input, generate intelligent responses, support multiple conversational exchanges, and maintain context throughout the conversation.

## Approach

* Created a Python virtual environment `venv` and installed the Groq library.
* Used the Groq API to connect to the `llama-3.1-8b-instant` Large Language Model (LLM).
* Accepted user input through the terminal and sent it to the model for processing.
* Retrieved the model's response using the `ai_response` variable and displayed it in a conversational format.
* Used a `messages` list to store user messages and AI responses, enabling context-aware conversations.
* Added a system message to define the assistant's behavior.
* Implemented a continuous chat loop to support multiple interactions within a session.



## Steps Taken to Solve the Problem
1. Created and activated a Python virtual environment.
2. Installed the Groq package.
3. Generated and configured a Groq API key.
4. Built a basic chatbot capable of sending prompts to the model.
5. Enhanced the chatbot to support continuous conversations using a while loop.
6. Implemented conversation memory using a  `messages` list.
7. Evaluated the chatbot by asking various questions to check content retention.
8. Experimented with parameters such as `temperature` and `max_tokens`.


## Challenges Faced and Solutions
* The originally specified model `llama3-8b-8192` was no longer supported on Groq, so the implementation was updated to use the supported `llama-3.1-8b-instant` model.
* The chatbot was unable to remember previous interactions, so a `messages` list was implemented and the complete conversation history was passed with every API request.
* Errors occurred while implementing the continuous chat loop due to incorrect indentation and loop structure, so the code was reorganized to ensure proper execution flow.

## How to Run the Application

### 1.Clone the GitHub repository to your local machine and navigate to the project directory.
git clone https://github.com/anjalidineshh.git

cd llm-project_anjali

### 2.Create a virtual environment.
python -m venv venv
### 3.Activate the virtual environment.
 For Windows:
 
venv\Scripts\activate

 For Linux/macOS:
 
source venv/bin/activate
### 4.Install all required dependencies from the requirements file.
pip install -r requirements.txt
### 5. Configure the Groq API Key
Set your Groq API key in the terminal before running the application.

Windows:
set GROQ_API_KEY=your_api_key_here

Linux/macOS:
export GROQ_API_KEY=your_api_key_here

Replace `your_api_key_here` with your actual Groq API key.
### 6.Run the chatbot application.
python chat.py
### 7.Enter your queries in the terminal to interact with the chatbot.
Type "exit" to terminate the chat session.

