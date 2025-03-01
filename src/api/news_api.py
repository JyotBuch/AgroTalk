import requests

url = "https://uiuc.chat/api/chat-api/chat"
headers = {
    'Content-Type': 'application/json',
}
data = {
    "model": "llama3.1:8b-instruct-fp16",
    "messages": [
        {
            "role": "system",
            "content": "What is tillage?"
        },
        {
            "role": "user",
            "content": "What is tillage?" # put user input here 
        }
    ],
    "openai_key": "DWXVJ9PhzqXbwdJMicfbOAjY4aHKb7Mvjiy0qukDrccEAviT9q67JQQJ99BAACYeBjFXJ3w3AAABACOG0CsL",
    "temperature": 0.1,
    "course_name": "AgroTalk",
    "stream": True,
    "api_key": "uc_72f58b54966b4f8f956cfbc535b802f7"
}

response = requests.post(url, headers=headers, json=data)
print(response.text)

