import os
import sys
import json
import uuid
import subprocess
from flask import Flask, render_template, request, jsonify, session

# Ensure secure handling of paths
sys.path.append(os.path.abspath("src"))
sys.path.append(os.path.abspath("."))

from api.UIUCChat import chat_with_bot
from data.models import Speech_To_Text
from llm.openai_driver import describe_image

# Configure application settings
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__, template_folder='templates')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = os.getenv("SECRET_KEY", "default_secret_key")  # Use environment variable for security

# --- Helper functions to manage conversation context ---

def count_tokens(text):
    """Estimate the number of tokens in a given text."""
    return len(text.split())

def trim_messages(messages, max_tokens=120000):
    """Trims conversation history to stay within token limits."""
    total_tokens = sum(count_tokens(msg.get('content', '')) for msg in messages)
    while total_tokens > max_tokens and messages:
        messages.pop(0)
        total_tokens = sum(count_tokens(msg.get('content', '')) for msg in messages)
    return messages

# --- Flask endpoints ---

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form.get('user_input')
    farm_type = request.form.get('farm_type', 'General Information')
    
    farm_info = f"Information requested is for {farm_type}." if farm_type != "General Information" else "General information requested."
    
    if 'messages' not in session:
        session['messages'] = []
    
    session['messages'].append({'role': 'user', 'content': user_input})
    session['messages'] = trim_messages(session['messages'])
    
    query = f"{farm_info}\n{user_input}"
    response = chat_with_bot(query)
    
    session['messages'].append({'role': 'assistant', 'content': response})
    
    return jsonify({'response': response})

@app.route('/upload_image', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], uuid.uuid4().hex + os.path.splitext(file.filename)[1])
    file.save(file_path)
    
    description = describe_image(file_path)
    
    os.remove(file_path)  # Remove file after processing to ensure security
    
    return jsonify({'description': description})

@app.route('/upload_audio', methods=['POST'])
def upload_audio():
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file provided'}), 400
    file = request.files['audio']
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'user_audio.wav')
    file.save(file_path)
    
    transcribed_text = Speech_To_Text.transcribe_audio_file(file_path)
    
    os.remove(file_path)  # Remove file after processing to ensure security
    
    if 'messages' not in session:
        session['messages'] = []
    
    session['messages'].append({'role': 'user', 'content': transcribed_text})
    session['messages'] = trim_messages(session['messages'])
    
    response = chat_with_bot(transcribed_text)
    session['messages'].append({'role': 'assistant', 'content': response})
    
    return jsonify({'transcribed_text': transcribed_text, 'response': response})

if __name__ == '__main__':
    app.run(debug=False)  # Ensure debug mode is disabled in production