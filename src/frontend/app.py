import os
import sys
import json
import uuid
import subprocess
from flask import Flask, render_template, request, jsonify, session

# Add your project paths so modules are accessible
sys.path.append("/Users/jyotbuch/AgroTalk/src")
sys.path.append("/Users/jyotbuch/AgroTalk")

from api.UIUCChat import chat_with_bot
from data.models import Speech_To_Text
from llm.openai_driver import describe_image

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__, template_folder='/Users/jyotbuch/AgroTalk/templates')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'your_secret_key_here'  # required for session usage

# --- Helper functions to manage conversation context ---

def count_tokens(text):
    """A rough approximation of token count."""
    return len(text.split())

def trim_messages(messages, max_tokens=120000):
    """Remove oldest messages until total token count is under max_tokens."""
    total_tokens = sum(count_tokens(msg.get('content', '')) for msg in messages)
    while total_tokens > max_tokens and messages:
        messages.pop(0)
        total_tokens = sum(count_tokens(msg.get('content', '')) for msg in messages)
    return messages

# --- (Translation functionalities commented out for now) ---
# from transformers import MarianMTModel, MarianTokenizer
# def translate_english_to_spanish(text):
#     model_name = 'Helsinki-NLP/opus-mt-en-es'
#     tokenizer = MarianTokenizer.from_pretrained(model_name)
#     model = MarianMTModel.from_pretrained(model_name)
#     inputs = tokenizer(text, return_tensors='pt', padding=True)
#     translated = model.generate(**inputs)
#     translated_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
#     return translated_text[0]

# --- Flask endpoints ---

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form.get('user_input')
    farm_type = request.form.get('farm_type', 'General Information')
    # language = request.form.get('language', 'en')  # language param (unused for now)

    if farm_type != "General Information":
        farm_info = f"Information requested is for {farm_type}."
    else:
        farm_info = "Information requested is for general information."
    
    # Initialize conversation history if not present.
    if 'messages' not in session:
        session['messages'] = []
    
    session['messages'].append({'role': 'user', 'content': user_input})
    session['messages'] = trim_messages(session['messages'])
    
    query = f"{farm_info}\n{user_input}"
    response = chat_with_bot(query)
    
    session['messages'].append({'role': 'assistant', 'content': response})
    
    # Translation functionality commented out:
    # if language == "es":
    #     response = translate_english_to_spanish(response)
    
    return jsonify({'response': response})

@app.route('/upload_image', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)
    
    description = describe_image(file_path)
    return jsonify({'description': description})

@app.route('/upload_audio', methods=['POST'])
def upload_audio():
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file provided'}), 400
    file = request.files['audio']
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'user_audio.wav')
    file.save(file_path)
    
    transcribed_text = Speech_To_Text.transcribe_audio_file(file_path)
    
    farm_type = request.form.get('farm_type', 'General Information')
    # language = request.form.get('language', 'en')  # language param (unused for now)
    
    if farm_type != "General Information":
        farm_info = f"Information requested is for {farm_type}."
    else:
        farm_info = "Information requested is for general information."
    
    if 'messages' not in session:
        session['messages'] = []
    
    session['messages'].append({'role': 'user', 'content': transcribed_text})
    session['messages'] = trim_messages(session['messages'])
    
    query = f"{farm_info}\n{transcribed_text}"
    response = chat_with_bot(query)
    session['messages'].append({'role': 'assistant', 'content': response})
    
    # Translation functionality commented out:
    # if language == "es":
    #     response = translate_english_to_spanish(response)
    
    return jsonify({'transcribed_text': transcribed_text, 'response': response})

if __name__ == '__main__':
    app.run(debug=True)


# from flask import Flask, render_template, request, jsonify
# from PIL import Image
# import os
# import sys
# import io

# # Add the path to your project folders so you can import your modules
# sys.path.append("/Users/jyotbuch/AgroTalk/src")
# sys.path.append("/Users/jyotbuch/AgroTalk")

# # Import your existing functions
# from api.UIUCChat import chat_with_bot
# from data.models import Speech_To_Text
# from llm.openai_driver import describe_image

# UPLOAD_FOLDER = 'uploads'
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# app = Flask(__name__, template_folder='/Users/jyotbuch/AgroTalk/templates')
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# # Home page: Render the chat interface
# @app.route('/')
# def index():
#     return render_template('index.html')

# # Endpoint to handle text chat
# @app.route('/chat', methods=['POST'])
# def chat():
#     user_input = request.form.get('user_input')
#     farm_type = request.form.get('farm_type', 'General Information')
#     # Create a message that includes farm-specific info
#     if farm_type != "General Information":
#         farm_info = f"Information requested is for {farm_type}."
#     else:
#         farm_info = "Information requested is for general information."
    
#     # Combine your input with the farm info
#     query = f"{farm_info}\n{user_input}"
#     response = chat_with_bot(query)
#     return jsonify({'response': response})

# # Endpoint to handle image uploads
# @app.route('/upload_image', methods=['POST'])
# def upload_image():
#     if 'image' not in request.files:
#         return jsonify({'error': 'No image file provided'}), 400
#     file = request.files['image']
#     if file.filename == '':
#         return jsonify({'error': 'No file selected'}), 400
    
#     file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
#     file.save(file_path)
    
#     # Optionally, you could compress the image here if needed:
#     img = Image.open(file)
#     img = img.convert("RGB")
#     img.thumbnail((1024, 1024))
#     img.save(file_path, "JPEG", quality=75)
    
#     # Process the image using your function
#     description = describe_image(file_path)
#     return jsonify({'description': description})

# # Endpoint to handle audio uploads
# @app.route('/upload_audio', methods=['POST'])
# def upload_audio():
#     if 'audio' not in request.files:
#         return jsonify({'error': 'No audio file provided'}), 400
#     file = request.files['audio']
#     file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'user_audio.wav')
#     file.save(file_path)
    
#     # Transcribe the audio file using your module
#     transcribed_text = Speech_To_Text.transcribe_audio_file(file_path)
    
#     # Include farm-specific information for the audio request as well
#     farm_type = request.form.get('farm_type', 'General Information')
#     if farm_type != "General Information":
#         farm_info = f"Information requested is for {farm_type}."
#     else:
#         farm_info = "Information requested is for general information."
    
#     query = f"{farm_info}\n{transcribed_text}"
#     response = chat_with_bot(query)
    
#     return jsonify({'transcribed_text': transcribed_text, 'response': response})

# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask, render_template, request, jsonify, session
# from PIL import Image
# import os
# import sys

# # Add the path to your project folders so you can import your modules
# sys.path.append("/Users/jyotbuch/AgroTalk/src")
# sys.path.append("/Users/jyotbuch/AgroTalk")

# # Import your existing functions
# from api.UIUCChat import chat_with_bot
# from data.models import Speech_To_Text
# from llm.openai_driver import describe_image

# UPLOAD_FOLDER = 'uploads'
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# app = Flask(__name__, template_folder='/Users/jyotbuch/AgroTalk/templates')
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.secret_key = 'your_secret_key_here'  # required for session usage

# # --- Helper functions to manage conversation context ---

# def count_tokens(text):
#     """
#     A rough approximation of token count.
#     In production, consider using a tokenizer specific to your model.
#     """
#     return len(text.split())

# def trim_messages(messages, max_tokens=120000):
#     """
#     Given a list of message dicts with a 'content' key,
#     remove oldest messages until total token count is under max_tokens.
#     """
#     total_tokens = sum(count_tokens(msg.get('content', '')) for msg in messages)
#     while total_tokens > max_tokens and messages:
#         messages.pop(0)
#         total_tokens = sum(count_tokens(msg.get('content', '')) for msg in messages)
#     return messages

# # --- Flask endpoints ---

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/chat', methods=['POST'])
# def chat():
#     user_input = request.form.get('user_input')
#     farm_type = request.form.get('farm_type', 'General Information')
#     if farm_type != "General Information":
#         farm_info = f"Information requested is for {farm_type}."
#     else:
#         farm_info = "Information requested is for general information."
    
#     # Initialize conversation history if not present.
#     if 'messages' not in session:
#         session['messages'] = []
    
#     # Append the new user message
#     session['messages'].append({'role': 'user', 'content': user_input})
#     # Trim the conversation context if needed
#     session['messages'] = trim_messages(session['messages'])
    
#     # For this example, we send only the new message plus farm info.
#     # You may choose to send the entire conversation history if desired.
#     query = f"{farm_info}\n{user_input}"
#     response = chat_with_bot(query)
    
#     # Append the bot's response to the conversation history.
#     session['messages'].append({'role': 'assistant', 'content': response})
    
#     return jsonify({'response': response})

# @app.route('/upload_image', methods=['POST'])
# def upload_image():
#     if 'image' not in request.files:
#         return jsonify({'error': 'No image file provided'}), 400
#     file = request.files['image']
#     if file.filename == '':
#         return jsonify({'error': 'No file selected'}), 400

#     file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
#     file.save(file_path)
    
#     # If your describe_image function uses conversation history,
#     # consider trimming it before calling the function.
#     description = describe_image(file_path)
#     return jsonify({'description': description})

# @app.route('/upload_audio', methods=['POST'])
# def upload_audio():
#     if 'audio' not in request.files:
#         return jsonify({'error': 'No audio file provided'}), 400
#     file = request.files['audio']
#     file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'user_audio.wav')
#     file.save(file_path)
    
#     transcribed_text = Speech_To_Text.transcribe_audio_file(file_path)
    
#     farm_type = request.form.get('farm_type', 'General Information')
#     if farm_type != "General Information":
#         farm_info = f"Information requested is for {farm_type}."
#     else:
#         farm_info = "Information requested is for general information."
    
#     # Initialize conversation history if not present.
#     if 'messages' not in session:
#         session['messages'] = []
    
#     # Append the audio transcription as a user message.
#     session['messages'].append({'role': 'user', 'content': transcribed_text})
#     session['messages'] = trim_messages(session['messages'])
    
#     query = f"{farm_info}\n{transcribed_text}"
#     response = chat_with_bot(query)
#     session['messages'].append({'role': 'assistant', 'content': response})
    
#     return jsonify({'transcribed_text': transcribed_text, 'response': response})

# if __name__ == '__main__':
#     app.run(debug=True)

# import os
# import sys
# import json
# import uuid
# import subprocess
# from flask import Flask, render_template, request, jsonify, session
# from api.UIUCChat import chat_with_bot
# from data.models import Speech_To_Text
# from llm.openai_driver import describe_image

# # Import the translation library from transformers
# from transformers import MarianMTModel, MarianTokenizer

# # Translation function from English to Spanish
# def translate_english_to_spanish(text):
#     model_name = 'Helsinki-NLP/opus-mt-en-es'
#     tokenizer = MarianTokenizer.from_pretrained(model_name)
#     model = MarianMTModel.from_pretrained(model_name)
#     inputs = tokenizer(text, return_tensors='pt', padding=True)
#     translated = model.generate(**inputs)
#     translated_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
#     return translated_text[0]

# # app = Flask(__name__, template_folder="templates")
# # app.secret_key = "your_secret_key_here"
# UPLOAD_FOLDER = "uploads"
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)
# app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/chat", methods=["POST"])
# def chat():
#     user_input = request.form.get("user_input")
#     farm_type = request.form.get("farm_type", "General Information")
#     language = request.form.get("language", "en")  # "en" or "es"
    
#     if farm_type != "General Information":
#         farm_info = f"Information requested is for {farm_type}."
#     else:
#         farm_info = "Information requested is for general information."
    
#     # Create the query for the chatbot.
#     query = f"{farm_info}\n{user_input}"
#     response = chat_with_bot(query)
    
#     # If Spanish is selected, translate the response.
#     if language == "es":
#         response = translate_english_to_spanish(response)
    
#     return jsonify({"response": response})

# @app.route("/upload_audio", methods=["POST"])
# def upload_audio():
#     if "audio" not in request.files:
#         return jsonify({"error": "No audio file provided"}), 400
#     file = request.files["audio"]
#     file_path = os.path.join(app.config["UPLOAD_FOLDER"], "user_audio.wav")
#     file.save(file_path)
    
#     transcript = Speech_To_Text.transcribe_audio_file(file_path)
#     farm_type = request.form.get("farm_type", "General Information")
#     language = request.form.get("language", "en")
    
#     if farm_type != "General Information":
#         farm_info = f"Information requested is for {farm_type}."
#     else:
#         farm_info = "Information requested is for general information."
    
#     query = f"{farm_info}\n{transcript}"
#     response = chat_with_bot(query)
    
#     if language == "es":
#         response = translate_english_to_spanish(response)
    
#     return jsonify({"transcribed_text": transcript, "response": response})

# if __name__ == "__main__":
#     app.run(debug=True)

