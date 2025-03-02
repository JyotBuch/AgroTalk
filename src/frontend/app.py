import streamlit as st
from PIL import Image
import os
from streamlit_mic_recorder import mic_recorder

# Page configuration
st.set_page_config(page_title='AgroTalk Chatbot', layout='wide')

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Language selection
language = st.sidebar.selectbox("Select Language / Seleccionar Idioma", ["English", "Español"])

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
        "processing_audio": "Processing your audio... (Speech-to-text + LLM response)"
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
        "processing_audio": "Procesando tu audio... (Conversión de voz a texto + Respuesta del modelo de lenguaje)"
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

# Initialize session state for chat history
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
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
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
    
    response = f"{t['processing_text']}\n\nEcho: {user_input}"
    
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
    
    st.rerun()

if user_image:
    img = Image.open(user_image)
    file_path = os.path.join(UPLOAD_FOLDER, user_image.name)
    img.save(file_path)
    
    st.session_state.messages.append({"role": "user", "content": t["image_uploaded"]})
    with st.chat_message("user"):
        st.image(img, caption=t["image_uploaded"], width=300)
        st.markdown(t["image_uploaded"])
    
    response = t["processing_image"]
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
    
    st.rerun()

if audio:
    audio_bytes = audio['bytes'] if isinstance(audio, dict) and 'bytes' in audio else audio
    
    if isinstance(audio_bytes, bytes):
        file_path = os.path.join(UPLOAD_FOLDER, "user_audio.wav")
        with open(file_path, "wb") as f:
            f.write(audio_bytes)
        
        st.session_state.messages.append({"role": "user", "content": t["audio_recorded"]})
        with st.chat_message("user"):
            st.audio(file_path, format="audio/wav")
            st.markdown(t["audio_recorded"])
        
        response = t["processing_audio"]
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.markdown(response)
        
        st.rerun()
    else:
        st.error("Invalid audio data received.")


# import streamlit as st
# from PIL import Image
# import os
# from streamlit_mic_recorder import mic_recorder

# # Page configuration
# st.set_page_config(page_title='AgroTalk Chatbot', layout='wide')

# UPLOAD_FOLDER = "uploads"
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# # Language selection
# language = st.sidebar.selectbox("Select Language / Seleccionar Idioma", ["English", "Español"])

# # Translations
# translations = {
#     "English": {
#         "title": "🌾 AgroTalk - Smart Farming Assistant",
#         "chat_placeholder": "Chat messages will appear here",
#         "input_placeholder": "Type a message...",
#         "upload_image": "Upload an image:",
#         "record_audio": "Record audio:",
#         "image_uploaded": "Image uploaded.",
#         "audio_recorded": "Audio recorded.",
#         "processing_text": "Processing your text... (LLM response)",
#         "processing_image": "Processing your image... (Vision model response)",
#         "processing_audio": "Processing your audio... (Speech-to-text + LLM response)"
#     },
#     "Español": {
#         "title": "🌾 AgroTalk - Asistente Inteligente de Agricultura",
#         "chat_placeholder": "Los mensajes del chat aparecerán aquí",
#         "input_placeholder": "Escribe un mensaje...",
#         "upload_image": "Subir una imagen:",
#         "record_audio": "Grabar audio:",
#         "image_uploaded": "Imagen subida.",
#         "audio_recorded": "Audio grabado.",
#         "processing_text": "Procesando tu texto... (Respuesta del modelo de lenguaje)",
#         "processing_image": "Procesando tu imagen... (Respuesta del modelo de visión)",
#         "processing_audio": "Procesando tu audio... (Conversión de voz a texto + Respuesta del modelo de lenguaje)"
#     }
# }

# # Get translations for the selected language
# t = translations[language]

# # Title
# st.title(t["title"])

# # Custom CSS styling
# st.markdown(
#     """
#     <style>
#         .chat-message {
#             padding: 1.5rem;
#             border-radius: 0.5rem;
#             margin-bottom: 1rem;
#             display: flex
#         }
#         .chat-message.user {
#             background-color: #2b313e
#         }
#         .chat-message.bot {
#             background-color: #475063
#         }
#         .chat-message .avatar {
#           width: 20%;
#         }
#         .chat-message .avatar img {
#           max-width: 78px;
#           max-height: 78px;
#           border-radius: 50%;
#           object-fit: cover;
#         }
#         .chat-message .message {
#           width: 80%;
#           padding: 0 1.5rem;
#           color: #fff;
#         }
#         .input-container {
#             display: flex;
#             align-items: center;
#             gap: 10px;
#         }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# # Initialize session state for chat history
# if 'messages' not in st.session_state:
#     st.session_state.messages = []

# # Display chat messages
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# # Input container with image upload and audio recording options in the same field
# with st.container():
#     col1, col2, col3 = st.columns([5, 1, 1])

#     with col1:
#         user_input = st.text_input(t["input_placeholder"])

#     with col2:
#         user_image = st.file_uploader("", type=["jpg", "jpeg", "png"], label_visibility="collapsed")

#     with col3:
#         audio = mic_recorder(start_prompt="🎤", key="mic")

# # Handle user inputs
# if user_input:
#     st.session_state.messages.append({"role": "user", "content": user_input})
#     with st.chat_message("user"):
#         st.markdown(user_input)
    
#     response = f"{t['processing_text']}\n\nEcho: {user_input}"
    
#     st.session_state.messages.append({"role": "assistant", "content": response})
#     with st.chat_message("assistant"):
#         st.markdown(response)
    
#     st.rerun()

# if user_image:
#     img = Image.open(user_image)
#     file_path = os.path.join(UPLOAD_FOLDER, user_image.name)
#     img.save(file_path)
    
#     st.session_state.messages.append({"role": "user", "content": t["image_uploaded"]})
#     with st.chat_message("user"):
#         st.image(img, caption=t["image_uploaded"], width=300)
#         st.markdown(t["image_uploaded"])
    
#     response = t["processing_image"]
#     st.session_state.messages.append({"role": "assistant", "content": response})
#     with st.chat_message("assistant"):
#         st.markdown(response)
    
#     st.rerun()

# if audio:
#     audio_bytes = audio['bytes'] if isinstance(audio, dict) and 'bytes' in audio else audio
    
#     if isinstance(audio_bytes, bytes):
#         file_path = os.path.join(UPLOAD_FOLDER, "user_audio.wav")
#         with open(file_path, "wb") as f:
#             f.write(audio_bytes)
        
#         st.session_state.messages.append({"role": "user", "content": t["audio_recorded"]})
#         with st.chat_message("user"):
#             st.audio(file_path, format="audio/wav")
#             st.markdown(t["audio_recorded"])
        
#         response = t["processing_audio"]
#         st.session_state.messages.append({"role": "assistant", "content": response})
#         with st.chat_message("assistant"):
#             st.markdown(response)
        
#         st.rerun()
#     else:
#         st.error("Invalid audio data received.")
