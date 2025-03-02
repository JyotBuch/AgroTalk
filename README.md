# AgroTalk: AI-Powered Agricultural Chatbot

## Overview
AgroTalk is an AI-powered chatbot designed to assist users with agricultural queries. The system integrates advanced NLP models, image recognition, and weather APIs to provide insightful recommendations, field analysis, and weather forecasts to farmers and agricultural professionals.

## Features
- **Chatbot Assistance**: Uses OpenAI's GPT models to respond to user queries related to farming, crops, and soil conditions.
- **Speech-to-Text Processing**: Converts spoken queries into text using Google Cloud Speech-to-Text API.
- **Image Recognition**: Analyzes images using OpenAI's vision models to provide insights about crops, soil quality, and pests.
- **Weather Forecasting**: Fetches real-time weather data from OpenWeatherMap to assist farmers in decision-making.
- **Multilingual Support**: Translates queries and responses between English and Spanish using MarianMT models.

## Technology Stack
- **Programming Language**: Python
- **APIs & Services**:
  - OpenAI GPT models for chatbot responses
  - Google Cloud Speech-to-Text for voice input
  - OpenAI Vision for image analysis
  - OpenWeatherMap API for weather forecasting
- **Libraries Used**:
  - Flask (for the web API)
  - Transformers (for language translation)
  - PIL (for image handling)
  - Requests (for API calls)

## Installation
### Prerequisites
Ensure you have Python installed (recommended: Python 3.8+). Install dependencies using:

```bash
pip install -r requirements.txt
```

### Environment Variables
Before running the project, set up the required API keys as environment variables:

```bash
export ACCUWEATHER_API_KEY="your_accuweather_api_key"
export AGROTALK_API_KEY="your_agrotalk_api_key"
export AZURE_OPENAI_API_KEY="your_azure_openai_api_key"
export AZURE_OPENAI_ENDPOINT="your_azure_openai_endpoint"
```

## Usage
### Running the Flask App
To start the application, run:

```bash
python app.py
```

### Example API Requests
#### Chatbot Query:
```bash
curl -X POST "http://localhost:5000/chat" -H "Content-Type: application/json" -d '{"user_input": "What is the best fertilizer for wheat?"}'
```

#### Upload Image for Analysis:
```bash
curl -X POST "http://localhost:5000/upload_image" -F "image=@path/to/your/image.jpg"
```

#### Upload Audio Query:
```bash
curl -X POST "http://localhost:5000/upload_audio" -F "audio=@path/to/your/audio.wav"
```

## Project Structure
```
├── app.py                   # Main application file
├── config.py                # Configuration file for API keys
├── requirements.txt         # Dependencies
├── static/                  # Static assets (images, CSS, JS)
├── templates/               # HTML templates
├── data/                    # Storage for processed data
└── models/                  # ML models for language and image processing
```

## Contributors
- **[Jyot Buch, Nidhi Baheti]** - Lead Developers

## License
This project is licensed under the MIT License. See `LICENSE` for details.

---
For inquiries or contributions, contact us at [your email] or visit our GitHub repository.

