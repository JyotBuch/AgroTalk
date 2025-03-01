from google.cloud import speech

def transcribe_audio(audio_file_path):
    """
    Transcribes the given audio file using Google Cloud Speech-to-Text.
    
    Args:
        audio_file_path (str): Path to the audio file.
    """
    # Instantiate a client
    client = speech.SpeechClient()
    
    # Read the audio file into memory
    with open(audio_file_path, "rb") as audio_file:
        content = audio_file.read()
    
    audio = speech.RecognitionAudio(content=content)
    
    # Configure the request. Adjust sample_rate_hertz and encoding as needed.
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",  # or "es-ES" for Spanish
    )
    
    # Use the recognize method for non-streaming (synchronous) transcription.
    response = client.recognize(config=config, audio=audio)
    
    # Process the results
    for result in response.results:
        # The alternative with the highest confidence is at index 0.
        print("Transcript: {}".format(result.alternatives[0].transcript))

if __name__ == "__main__":
    # Replace 'path_to_audio.wav' with the actual path to your audio file.
    audio_file_path = "/Users/jyotbuch/Downloads/test.wav"
    transcribe_audio(audio_file_path)