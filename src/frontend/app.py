import streamlit as st
from PIL import Image
from streamlit_mic_recorder import mic_recorder
import sys
import os
import tempfile

# Add the path to the folder containing UIUCChat.py to the sys.path
sys.path.append("/Users/jyotbuch/AgroTalk/src")
sys.path.append("/Users/jyotbuch/AgroTalk")

from api.UIUCChat import chat_with_bot  # Importing the chatbot function
from data.models import Speech_To_Text # Importing the Speech-to-Text module



# Page configuration
st.set_page_config(page_title='AgroTalk Chatbot', layout='wide')

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Language selection
language = st.sidebar.selectbox("Select Language / Seleccionar Idioma", ["English", "Español"])

# Farm selection dropdown in sidebar with default option for general information
farm_type = st.sidebar.selectbox("Select Farm Location", ["General Information", "Illinois Farm", "North Dakota Farm"])

# Translations
translations = {
    "English": {
        "title": "🌾 AgroTalk - Smart Farming Assistant",
        "chat_placeholder": "Chat messages will appear here",
        "input_placeholder": "Type a message...",
        "upload_image": "Upload an image:",
        "record_audio": "Record audio:",
        "image_uploaded": "Image uploaded.",
        "audio_recorded": "Audio recorded.",
        "processing_text": "Processing your text... (LLM response)",
        "processing_image": "Processing your image... (Vision model response)",
        "processing_audio": "Processing your audio... (Speech-to-text + LLM response)",
        "farm_selected": f"Selected farm location: {farm_type}"
    },
    "Español": {
        "title": "🌾 AgroTalk - Asistente Inteligente de Agricultura",
        "chat_placeholder": "Los mensajes del chat aparecerán aquí",
        "input_placeholder": "Escribe un mensaje...",
        "upload_image": "Subir una imagen:",    
        "record_audio": "Grabar audio:",
        "image_uploaded": "Imagen subida.",
        "audio_recorded": "Audio grabado.",
        "processing_text": "Procesando tu texto... (Respuesta del modelo de lenguaje)",
        "processing_image": "Procesando tu imagen... (Respuesta del modelo de visión)",
        "processing_audio": "Procesando tu audio... (Conversión de voz a texto + Respuesta del modelo de lenguaje)",
        "farm_selected": f"Ubicación de la granja seleccionada: {farm_type}"
    }
}

# Get translations for the selected language
t = translations[language]

# Title
st.title(t["title"])

# Custom CSS styling
st.markdown(
    """
    <style>
        .chat-message {
            padding: 1.5rem;
            border-radius: 0.5rem;
            margin-bottom: 1rem;
            display: flex
        }
        .chat-message.user {
            background-color: #2b313e
        }
        .chat-message.bot {
            background-color: #475063
        }
        .chat-message .avatar {
          width: 20%;
        }
        .chat-message .avatar img {
          max-width: 78px;
          max-height: 78px;
          border-radius: 50%;
          object-fit: cover;
        }
        .chat-message .message {
          width: 80%;
          padding: 0 1.5rem;
          color: #fff;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Display selected farm type in the sidebar
st.sidebar.write(t["farm_selected"])

# Initialize session state for chat history
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'audio_files' not in st.session_state:
    st.session_state.audio_files = []
if 'last_audio' not in st.session_state:
    st.session_state.last_audio = None
if 'last_image' not in st.session_state:
    st.session_state.last_image = None

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if "audio" in message:
            st.markdown("🎤")  # Show mic emoji instead of audio player
        elif "image" in message:
            st.image(message["image"], caption=t["image_uploaded"], width=300)
        else:
            st.markdown(message["content"])

# User input
user_input = st.chat_input(t["input_placeholder"])

# File upload and audio recording container
col1, col2 = st.columns(2)

# Image upload input
with col1:
    st.write(t["upload_image"])
    user_image = st.file_uploader("", type=["jpg", "jpeg", "png"], label_visibility="collapsed")

# Audio recording input
with col2:
    st.write(t["record_audio"])
    audio = mic_recorder(start_prompt="🎤", key="mic")

# Handle user inputs
if user_input:
    # Add user message to the chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Determine farm-specific message
    farm_info = f"Information requested is for {farm_type}." if farm_type != "General Information" else "Information requested is for general information."
    print(farm_info)
    # Call the chatbot function to get the actual response
    response = chat_with_bot(f"{farm_info}\n".join(user_input))  # Get response from the chatbot backend

    # Prepend farm info to the response
    response_with_farm_info = f"{response}"

    # Append the assistant's response with farm info to session state
    st.session_state.messages.append({"role": "assistant", "content": response_with_farm_info})
    with st.chat_message("assistant"):
        st.markdown(response_with_farm_info)

    st.rerun()

if user_image and user_image != st.session_state.last_image:
    st.session_state.last_image = user_image
    img = Image.open(user_image)
    file_path = os.path.join(UPLOAD_FOLDER, user_image.name)
    img.save(file_path)

    st.session_state.messages.append({"role": "user", "image": file_path})
    with st.chat_message("user"):
        st.image(file_path, caption=t["image_uploaded"], width=300)

    response = t["processing_image"]
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)

    st.rerun()

if audio and audio != st.session_state.last_audio:
    st.session_state.last_audio = audio  # Update last audio to prevent infinite loop
    audio_bytes = audio['bytes'] if isinstance(audio, dict) and 'bytes' in audio else audio

    if isinstance(audio_bytes, bytes):
        file_path = os.path.join(UPLOAD_FOLDER, f"user_audio.wav")
        with open(file_path, "wb") as f:
            f.write(audio_bytes)

        st.session_state.audio_files.append(file_path)
        st.session_state.messages.append({"role": "user", "content": t["audio_recorded"], "audio": file_path})
        with st.chat_message("user"):
            st.markdown("🎤")  # Show mic emoji instead of audio player

        response = t["processing_audio"]
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.markdown(response)

        st.rerun()
