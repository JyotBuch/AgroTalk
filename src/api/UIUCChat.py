# import requests

# url = "https://uiuc.chat/api/chat-api/chat"
# headers = {
#     'Content-Type': 'application/json',
# }
# data = {
#     "model": "llama3.1:8b-instruct-fp16",
#     "messages": [
#         {
#             "role": "system",
#             "content": "What is tillage?"
#         },
#         {
#             "role": "user",
#             "content": "What is tillage?" # put user input here 
#         }
#     ],
#     "openai_key": "DWXVJ9PhzqXbwdJMicfbOAjY4aHKb7Mvjiy0qukDrccEAviT9q67JQQJ99BAACYeBjFXJ3w3AAABACOG0CsL",
#     "temperature": 0.1,
#     "course_name": "AgroTalk",
#     "stream": True,
#     "api_key": "uc_72f58b54966b4f8f956cfbc535b802f7"
# }

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
        response = requests.post(url, headers=headers, json=data)

        # Ensure valid response
        if response.status_code == 200:
            bot_reply = response.json().get("content", "No response received.")
            conversation_history.append({"role": "assistant", "content": bot_reply})  # Keep chat history
            return bot_reply
        else:
            return f"Error: {response.status_code}, {response.text}"

    except requests.RequestException as e:
        return f"Request failed: {str(e)}"

# Conversation loop
print("Chatbot: Hello! Ask me anything about agriculture. Type 'exit' to end the chat.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Chatbot: Goodbye!")
        break

    bot_response = chat_with_bot(user_input)
    print(f"Chatbot: {bot_response}")
