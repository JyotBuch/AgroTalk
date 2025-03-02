import subprocess
import json
import os
import uuid
from google.cloud import speech
from langdetect import detect  # or skip if you don't need language detection

def ensure_linear_pcm_wav(file_path):
    """
    1. Detect the true codec using ffprobe.
    2. If it's already linear PCM, return the same file.
    3. Otherwise, convert to 16-bit PCM at 16 kHz, mono.
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
        # We assume it's already correct if it's PCM.
        # (Optionally, check for sample rate/channels and re-encode anyway.)
        return file_path
    
    # Convert to a new file
    tmp_path = f"/tmp/{uuid.uuid4()}.wav"
    subprocess.run([
        "ffmpeg", "-i", file_path,
        "-ac", "1",            # mono
        "-ar", "16000",        # 16kHz
        "-c:a", "pcm_s16le",   # 16-bit PCM
        tmp_path
    ], check=True)
    
    return tmp_path

def transcribe_audio_file(
    audio_file_path,
    primary_language="en-US",
    alternative_languages=["es-ES"]
):
    """
    Transcribe audio by ensuring it's properly formatted PCM,
    then calling the Google Speech-to-Text API.

    'primary_language' is the main language_code.
    'alternative_languages' is a list of additional languages, e.g. ["es-ES"].
    """
    # Convert if needed
    normalized_path = ensure_linear_pcm_wav(audio_file_path)
    
    # Initialize client
    client = speech.SpeechClient()
    
    # Read the (converted) audio file
    with open(normalized_path, "rb") as f:
        content = f.read()
    
    # Configuration: primary + alternative language(s)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code=primary_language,
        alternative_language_codes=alternative_languages,
    )
    audio = speech.RecognitionAudio(content=content)
    
    # Transcribe
    response = client.recognize(config=config, audio=audio)
    # Debug: print the raw response
    print(response)
    
    # If no results, return empty transcript
    if not response.results:
        return {'Transcript': '', 'Language': 'unknown'}
    
    # Collect the transcripts
    transcript = " ".join(
        result.alternatives[0].transcript for result in response.results
    )
    
    # Optionally, try to detect the language from the transcript
    try:
        detected_language = detect(transcript) if transcript else "unknown"
    except:
        detected_language = "und"
    
    return transcript

# if __name__ == "__main__":
#     # Example usage
#     audio_path = "./uploads/user_audio.wav"
#     result = transcribe_audio_file(
#         audio_file_path=audio_path,
#         primary_language="en-US",
#         alternative_languages=["es-ES"]
#     )
#     print(result)