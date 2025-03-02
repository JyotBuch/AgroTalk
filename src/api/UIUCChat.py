import subprocess
import json
import os
import uuid
import requests
from google.cloud import speech
from langdetect import detect  # or skip if you don't need language detection
from transformers import MarianMTModel, MarianTokenizer

def chat_with_bot(user_input):
    """
    Sends user input to the chatbot and returns the response while maintaining conversation history.
    """
    url = os.getenv("CHATBOT_API_URL")  # Ensure the API URL is stored securely
    api_key = os.getenv("CHATBOT_API_KEY")  # Hide API keys using environment variables
    headers = {'Content-Type': 'application/json'}

    conversation_history = [
        {"role": "system", "content": "You are AgroTalk, a chatbot that helps with agricultural queries."}
    ]
    conversation_history.append({"role": "user", "content": user_input})
    
    data = {
        "model": "llama3.1:8b-instruct-fp16",
        "messages": conversation_history,
        "temperature": 0.1,
        "course_name": "AgroTalk",
        "stream": False,
        "api_key": api_key  # Secure API key usage
    }

    try:
        response = requests.post(url, headers=headers, json=data, timeout=50)
        if response.status_code == 200:
            json_response = response.json()
            bot_reply = json_response.get("message", "No response received.")
            conversation_history.append({"role": "assistant", "content": bot_reply})
            return bot_reply
        else:
            return f"Error: {response.status_code}, {response.text}"
    except requests.RequestException as e:
        return f"Request failed: {str(e)}"

# Uncomment for standalone execution
# if __name__ == "__main__":
#     audio_path = "./uploads/user_audio.wav"
#     result = transcribe_audio_file(
#         audio_file_path=audio_path,
#         primary_language="en-US",
#         alternative_languages=["es-ES"]
#     )
#     print(result)
