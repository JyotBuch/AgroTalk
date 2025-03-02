# # import os
# # from google.cloud import speech
# # from langdetect import detect
# # import soundfile as sf

# # def get_audio_properties(file_path):
# #     """
# #     Retrieve sample rate, channel count, and subtype of the audio file.
# #     """
# #     info = sf.info(file_path)
# #     return info.samplerate, info.channels, info.subtype

# # def choose_encoding(subtype):
# #     """
# #     Map the audio file subtype to a Google Cloud Speech encoding.
# #     """
# #     if subtype.upper() in ["PCM_16", "PCM_S16LE", "PCM_S16BE"]:
# #         return speech.RecognitionConfig.AudioEncoding.LINEAR16
# #     elif "FLAC" in subtype.upper():
# #         return speech.RecognitionConfig.AudioEncoding.FLAC
# #     else:
# #         return speech.RecognitionConfig.AudioEncoding.ENCODING_UNSPECIFIED

# # def create_dynamic_config(file_path, primary_language="en-US", alternative_languages=["es-ES"]):
# #     """
# #     Create a dynamic RecognitionConfig based on audio file properties.
# #     """
# #     sample_rate, channels, subtype = get_audio_properties(file_path)
# #     encoding = choose_encoding(subtype)
    
# #     config = speech.RecognitionConfig(
# #         encoding=encoding,
# #         sample_rate_hertz=sample_rate,
# #         language_code=primary_language,
# #         alternative_language_codes=alternative_languages,
# #         audio_channel_count=channels,
# #     )
# #     return config

# # def detect_language(transcript):
# #     """
# #     Use langdetect to identify the language of the transcript.
# #     Returns the detected language code (e.g., 'en', 'es').
# #     """
# #     try:
# #         return detect(transcript)
# #     except Exception as e:
# #         return "und"  # undetermined

# # def transcribe_audio_file(audio_file_path):
# #     # Initialize the Speech client
# #     client = speech.SpeechClient()
    
# #     # Read audio file content
# #     with open(audio_file_path, "rb") as audio_file:
# #         content = audio_file.read()
    
# #     # Create dynamic configuration based on audio file properties
# #     config = create_dynamic_config(audio_file_path)
# #     audio = speech.RecognitionAudio(content=content)
    
# #     # Transcribe the audio
# #     response = client.recognize(config=config, audio=audio)
# #     transcript = " ".join(result.alternatives[0].transcript for result in response.results)
    
# #     # Detect the language from the transcript
# #     detected_language = detect_language(transcript) if transcript else "unknown"
    
# #     return {'Transcript': transcript, 'Language' : detected_language}

# # if __name__ == "__main__":
# #     # Replace with your audio file path
# #     audio_path = "./uploads/user_audio.wav"
# #     transcript = transcribe_audio_file(audio_path)
    
# #     print(transcript)

# from google.cloud import speech
# from langdetect import detect

# def choose_encoding(file_path):
#     """
#     Automatically determine encoding based on file extension or fallback.
#     """
#     if file_path.lower().endswith(('.wav', '.pcm')):
#         return speech.RecognitionConfig.AudioEncoding.LINEAR16
#     elif file_path.lower().endswith('.flac'):
#         return speech.RecognitionConfig.AudioEncoding.FLAC
#     else:
#         return speech.RecognitionConfig.AudioEncoding.ENCODING_UNSPECIFIED

# def create_dynamic_config(file_path, primary_language="en-US", alternative_languages=["es-ES"]):
#     """
#     Create a dynamic RecognitionConfig based on file extension (no need for external libraries).
#     """
#     encoding = choose_encoding(file_path)
    
#     config = speech.RecognitionConfig(
#         encoding=encoding,
#         language_code=primary_language,
#         alternative_language_codes=alternative_languages,
#     )
#     return config

# def detect_language(transcript):
#     """
#     Use langdetect to identify the language of the transcript.
#     Returns the detected language code (e.g., 'en', 'es').
#     """
#     try:
#         return detect(transcript)
#     except Exception as e:
#         return "und"  # undetermined

# def transcribe_audio_file(audio_file_path):
#     # Initialize the Speech client
#     client = speech.SpeechClient()
    
#     # Read audio file content
#     with open(audio_file_path, "rb") as audio_file:
#         content = audio_file.read()
    
#     # Create dynamic configuration based on file extension
#     config = create_dynamic_config(audio_file_path)
#     audio = speech.RecognitionAudio(content=content)
    
#     # Transcribe the audio
#     response = client.recognize(config=config, audio=audio)
#     transcript = " ".join(result.alternatives[0].transcript for result in response.results)
    
#     # Detect the language from the transcript
#     detected_language = detect_language(transcript) if transcript else "unknown"
    
#     return {'Transcript': transcript, 'Language': detected_language}

# if __name__ == "__main__":
#     # Replace with your audio file path
#     audio_path = "./uploads/user_audio.wav"
#     transcript = transcribe_audio_file(audio_path)
    
#     print(transcript)


from google.cloud import speech
from langdetect import detect
from pydub.utils import mediainfo

def choose_encoding(file_path):
    """
    Automatically determine encoding based on file extension.
    """
    if file_path.lower().endswith(('.wav', '.pcm')):
        return speech.RecognitionConfig.AudioEncoding.LINEAR16
    elif file_path.lower().endswith('.flac'):
        return speech.RecognitionConfig.AudioEncoding.FLAC
    else:
        return speech.RecognitionConfig.AudioEncoding.ENCODING_UNSPECIFIED

def get_sample_rate(file_path):
    """
    Get the sample rate using pydub's mediainfo.
    """
    info = mediainfo(file_path)
    sample_rate = int(info.get('sample_rate', 16000))  # Default to 16kHz if not found
    return sample_rate

def create_dynamic_config(file_path, primary_language="en-US", alternative_languages=["es-ES"]):
    """
    Create a dynamic RecognitionConfig based on file properties.
    """
    encoding = choose_encoding(file_path)
    sample_rate = get_sample_rate(file_path)
    
    config = speech.RecognitionConfig(
        encoding=encoding,
        sample_rate_hertz=sample_rate,
        language_code=primary_language,
        alternative_language_codes=alternative_languages,
    )
    return config

def detect_language(transcript):
    """
    Use langdetect to identify the language of the transcript.
    """
    try:
        return detect(transcript)
    except Exception as e:
        return "und"  # undetermined

def transcribe_audio_file(audio_file_path):
    # Initialize the Speech client
    client = speech.SpeechClient()
    
    # Read audio file content
    with open(audio_file_path, "rb") as audio_file:
        content = audio_file.read()
    
    # Create dynamic configuration based on file properties
    config = create_dynamic_config(audio_file_path)
    audio = speech.RecognitionAudio(content=content)
    
    # Transcribe the audio
    response = client.recognize(config=config, audio=audio)
    transcript = " ".join(result.alternatives[0].transcript for result in response.results)
    
    # Detect the language from the transcript
    detected_language = detect_language(transcript) if transcript else "unknown"
    
    return {'Transcript': transcript, 'Language': detected_language}

if __name__ == "__main__":
    # Replace with your audio file path
    audio_path = "./uploads/user_audio.wav"
    transcript = transcribe_audio_file(audio_path)
    
    print(transcript)

