import subprocess
import json
import os
import uuid
from google.cloud import speech
from langdetect import detect  # or skip if you don't need language detection
from transformers import MarianMTModel, MarianTokenizer

def ensure_linear_pcm_wav(file_path):
    """
    Ensure the audio file is in linear PCM WAV format.

    Steps:
    1. Use ffprobe to check the codec of the input file.
    2. If already PCM, return the original file path.
    3. Otherwise, convert the file to 16-bit PCM at 16 kHz, mono.

    Args:
        file_path (str): Path to the input audio file.

    Returns:
        str: Path to the converted or original PCM WAV file.
    """
    cmd = [
        "ffprobe", "-v", "quiet",
        "-print_format", "json",
        "-show_streams", file_path
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    info = json.loads(proc.stdout)
    
    is_pcm = False
    for stream in info.get("streams", []):
        codec_name = stream.get("codec_name", "")
        if codec_name.startswith("pcm_"):
            is_pcm = True
            break
    
    if is_pcm:
        return file_path  # Already in PCM format
    
    # Convert to a secure temporary file
    tmp_path = os.path.join("/tmp", f"{uuid.uuid4()}.wav")
    subprocess.run([
        "ffmpeg", "-i", file_path,
        "-ac", "1",            # mono
        "-ar", "16000",        # 16kHz
        "-c:a", "pcm_s16le",   # 16-bit PCM
        tmp_path
    ], check=True)
    
    return tmp_path

def translate_spanish_to_english(text):
    """
    Translate Spanish text to English using MarianMT.
    
    Args:
        text (str): Text in Spanish.
    
    Returns:
        str: Translated English text.
    """
    model_name = 'Helsinki-NLP/opus-mt-es-en'
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    
    inputs = tokenizer(text, return_tensors='pt', padding=True)
    translated = model.generate(**inputs)
    translated_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
    
    return translated_text[0]

def transcribe_audio_file(
    audio_file_path,
    primary_language="en-US",
    alternative_languages=["es-ES"]
):
    """
    Transcribe an audio file using Google Cloud Speech-to-Text API.
    
    The function ensures the audio file is properly formatted (PCM WAV) 
    before sending it to the API.

    Args:
        audio_file_path (str): Path to the input audio file.
        primary_language (str): Primary language for transcription.
        alternative_languages (list): List of alternative language codes.

    Returns:
        dict: A dictionary containing the transcript and detected language.
    """
    # Convert to PCM WAV if necessary
    normalized_path = ensure_linear_pcm_wav(audio_file_path)
    
    # Initialize Google Speech-to-Text client
    client = speech.SpeechClient()
    
    # Read audio content
    with open(normalized_path, "rb") as f:
        content = f.read()
    
    # Configure speech recognition settings
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code=primary_language,
        alternative_language_codes=alternative_languages,
    )
    audio = speech.RecognitionAudio(content=content)
    
    # Transcribe the audio
    response = client.recognize(config=config, audio=audio)
    
    # If no results, return an empty transcript
    if not response.results:
        return {'Transcript': '', 'Language': 'unknown'}
    
    # Extract the transcript from the response
    transcript = " ".join(
        result.alternatives[0].transcript for result in response.results
    )
    
    # Detect language from transcript (fallback to 'unknown' if detection fails)
    try:
        detected_language = detect(transcript) if transcript else "unknown"
    except:
        detected_language = "und"
    
    # Translate if necessary
    if detected_language == "es":
        transcript = translate_spanish_to_english(transcript)
    
    return {'Transcript': transcript, 'Language': detected_language}

# Uncomment for standalone execution
# if __name__ == "__main__":
#     audio_path = "./uploads/user_audio.wav"
#     result = transcribe_audio_file(
#         audio_file_path=audio_path,
#         primary_language="en-US",
#         alternative_languages=["es-ES"]
#     )
#     print(result)