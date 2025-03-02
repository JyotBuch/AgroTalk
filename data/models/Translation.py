from transformers import MarianMTModel, MarianTokenizer

def translate_spanish_to_english(text):
    # Load the MarianMT model and tokenizer for Spanish to English
    model_name = 'Helsinki-NLP/opus-mt-es-en'
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)

    # Tokenize the input text and generate translation
    inputs = tokenizer(text, return_tensors='pt', padding=True)
    translated = model.generate(**inputs)

    # Decode the generated tokens back to text
    translated_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
    return translated_text[0]


def transcribe_and_translate(audio_file_path):
    # Transcribe the audio and detect language
    # transcript, detected_language = {'Hello, how are you?','en'}
    transcript, detected_language = {'Hola, ¿cómo estás?','es'}
    
    # If the detected language is Spanish ('es'), translate to English
    if detected_language == 'es':
        translation = translate_spanish_to_english(transcript)
        return translation
    else:
        return transcript
    
# if __name__ == "__main__":
#     audio_path = "path/to/your_audio_file.wav"
#     result = transcribe_and_translate(audio_path)
#     print("Processed Text:")
#     print(result)

from transformers import MarianMTModel, MarianTokenizer

def translate_english_to_spanish(text):
    model_name = 'Helsinki-NLP/opus-mt-en-es'
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)

    inputs = tokenizer(text, return_tensors='pt', padding=True)
    translated = model.generate(**inputs)
    translated_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
    return translated_text[0]