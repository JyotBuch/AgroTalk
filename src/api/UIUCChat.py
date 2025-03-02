# import requests

# # API endpoint and headers
# url = "https://uiuc.chat/api/chat-api/chat"
# headers = {'Content-Type': 'application/json'}

# # Initialize conversation history
# conversation_history = [
#     {"role": "system", "content": "You are AgroTalk, a chatbot that helps with agricultural queries."}
# ]

# def chat_with_bot(user_input):
#     """
#     Sends user input to the chatbot and returns the response while maintaining conversation history.
#     """
#     # Append user message to conversation history
#     conversation_history.append({"role": "user", "content": user_input})

#     # Prepare request payload
#     data = {
#         "model": "llama3.1:8b-instruct-fp16",
#         "messages": conversation_history,
#         "openai_key": "DWXVJ9PhzqXbwdJMicfbOAjY4aHKb7Mvjiy0qukDrccEAviT9q67JQQJ99BAACYeBjFXJ3w3AAABACOG0CsL",
#         "temperature": 0.1,
#         "course_name": "AgroTalk",
#         "stream": False,  # Change to False for non-streaming responses
#         "api_key": "uc_72f58b54966b4f8f956cfbc535b802f7"
#     }

#     try:
#         # Send request
#         response = requests.post(url, headers=headers, json=data, timeout=50)

#         # Log the raw response text for debugging
#         print("Raw Response Text:", response.text)

#         # Check if response is valid
#         if response.status_code == 200:
#             try:
#                 json_response = response.json()  # Parse JSON
#                 # Debugging: Print full API response to see structure
#                 print("Full API Response:", json_response)

#                 # Extract the message directly from the "message" key
#                 bot_reply = json_response.get("message", "No response received.")

#                 # Append the assistant's reply to conversation history
#                 conversation_history.append({"role": "assistant", "content": bot_reply})
#                 return bot_reply

#             except ValueError as e:
#                 return f"Failed to parse JSON: {e}"

#         else:
#             return f"Error: {response.status_code}, {response.text}"

#     except requests.RequestException as e:
#         return f"Request failed: {str(e)}"

# # # Conversation loop
# # print("Chatbot: Hello! Ask me anything about agriculture. Type 'exit' to end the chat.")
# # while True:
# #     user_input = input("You: ")
# #     if user_input.lower() in ["exit", "quit", "bye"]:
# #         print("Chatbot: Goodbye!")
# #         break

# #     bot_response = chat_with_bot(user_input)
# #     print(f"Chatbot: {bot_response}")

# import requests
# from PIL import Image
# import io
# import base64

# # API endpoint and headers
# url = "https://uiuc.chat/api/chat-api/chat"
# headers = {'Content-Type': 'application/json'}

# # Initialize conversation history
# conversation_history = [
#     {"role": "system", "content": "You are AgroTalk, a chatbot that helps with agricultural queries."}
# ]

# # Image recognition API endpoint (example placeholder, replace with your actual endpoint)
# image_recognition_url = "https://some-image-recognition-api.com/analyze"

# def image_to_base64(image_path):
#     """Converts image to base64 string."""
#     with open(image_path, "rb") as img_file:
#         return base64.b64encode(img_file.read()).decode('utf-8')

# def get_image_description(image_path):
#     """Send the image to an image recognition API and get a description."""
#     # Convert image to base64
#     image_data = image_to_base64(image_path)
    
#     # Prepare the data for the image recognition request
#     image_data_payload = {
#         "image": image_data,
#         "api_key": "YOUR_IMAGE_RECOGNITION_API_KEY"
#     }

#     try:
#         # Send request to the image recognition API
#         response = requests.post(image_recognition_url, json=image_data_payload)
#         if response.status_code == 200:
#             # Parse response and return the description of the image
#             result = response.json()
#             return result.get('description', 'No description available.')
#         else:
#             return f"Error: {response.status_code}, {response.text}"
#     except requests.RequestException as e:
#         return f"Request failed: {str(e)}"

# def chat_with_bot(user_input, image_path=None):
#     """
#     Sends user input to the chatbot and returns the response while maintaining conversation history.
#     Optionally accepts an image path and includes a description of the image.
#     """
#     # Append user message to conversation history
#     conversation_history.append({"role": "user", "content": user_input})

#     # If image is provided, get the description of the image
#     if image_path:
#         image_description = get_image_description(image_path)
#         conversation_history.append({"role": "user", "content": f"Image Description: {image_description}"})
    
#     # Prepare request payload
#     data = {
#         "model": "llama3.1:8b-instruct-fp16",
#         "messages": conversation_history,
#         "openai_key": "DWXVJ9PhzqXbwdJMicfbOAjY4aHKb7Mvjiy0qukDrccEAviT9q67JQQJ99BAACYeBjFXJ3w3AAABACOG0CsL",
#         "temperature": 0.1,
#         "course_name": "AgroTalk",
#         "stream": False,
#         "api_key": "uc_72f58b54966b4f8f956cfbc535b802f7"
#     }

#     try:
#         # Send request to chatbot
#         response = requests.post(url, headers=headers, json=data, timeout=50)

#         # Check if response is valid
#         if response.status_code == 200:
#             try:
#                 json_response = response.json()  # Parse JSON response
#                 bot_reply = json_response.get("message", "No response received.")
#                 conversation_history.append({"role": "assistant", "content": bot_reply})
#                 return bot_reply
#             except ValueError as e:
#                 return f"Failed to parse JSON: {e}"

#         else:
#             return f"Error: {response.status_code}, {response.text}"

#     except requests.RequestException as e:
#         return f"Request failed: {str(e)}"
    

    # use detailed comments and  check for best practices and hide and paths and api from this code

import requests

# API endpoint and headers
url = "https://uiuc.chat/api/chat-api/chat"
headers = {'Content-Type': 'application/json'}

# Initialize conversation history
conversation_history = [
    {"role": "system", "content": "You are AgroTalk, a chatbot that helps with agricultural queries."}
]

def chat_with_bot(user_input):
    """
    Sends user input to the chatbot and returns the response while maintaining conversation history.
    """
    # Append user message to conversation history
    conversation_history.append({"role": "user", "content": user_input})

    # Prepare request payload
    data = {
        "model": "llama3.1:8b-instruct-fp16",
        "messages": conversation_history,
        "openai_key": "DWXVJ9PhzqXbwdJMicfbOAjY4aHKb7Mvjiy0qukDrccEAviT9q67JQQJ99BAACYeBjFXJ3w3AAABACOG0CsL",
        "temperature": 0.1,
        "course_name": "AgroTalk",
        "stream": False,  # Change to False for non-streaming responses
        "api_key": "uc_72f58b54966b4f8f956cfbc535b802f7"
    }

    try:
        # Send request
        response = requests.post(url, headers=headers, json=data, timeout=50)

        # Log the raw response text for debugging
        print("Raw Response Text:", response.text)

        # Check if response is valid
        if response.status_code == 200:
            try:
                json_response = response.json()  # Parse JSON
                # Debugging: Print full API response to see structure
                print("Full API Response:", json_response)

                # Extract the message directly from the "message" key
                bot_reply = json_response.get("message", "No response received.")

                # Append the assistant's reply to conversation history
                conversation_history.append({"role": "assistant", "content": bot_reply})
                return bot_reply

            except ValueError as e:
                return f"Failed to parse JSON: {e}"

        else:
            return f"Error: {response.status_code}, {response.text}"

    except requests.RequestException as e:
        return f"Request failed: {str(e)}"

# # Conversation loop
# print("Chatbot: Hello! Ask me anything about agriculture. Type 'exit' to end the chat.")
# while True:
#     user_input = input("You: ")
#     if user_input.lower() in ["exit", "quit", "bye"]:
#         print("Chatbot: Goodbye!")
#         break

#     bot_response = chat_with_bot(user_input)
#     print(f"Chatbot: {bot_response}")