import base64
from io import BytesIO
from PIL import Image
from openai import AzureOpenAI

AZURE_OPENAI_API_KEY = "DWXVJ9PhzqXbwdJMicfbOAjY4aHKb7Mvjiy0qukDrccEAviT9q67JQQJ99BAACYeBjFXJ3w3AAABACOG0CsL"
AZURE_OPENAI_ENDPOINT = "https://openai-agco-poc.openai.azure.com"

client = AzureOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    api_version="2024-10-21",
    azure_endpoint=AZURE_OPENAI_ENDPOINT
)

endpoints = {
    "gpt_40": "gpt-4o-2",
    "gpt_o1_mini": "o1-mini"
}

def describe_image(image_path):
    """
    Reads an image and sends it to OpenAI for description without compression.
    """
    print("image_path", image_path)
    try:
        # Read the image as binary
        with open(image_path, "rb") as img_file:
            image_bytes = img_file.read()

        # Convert to base64
        base64_image = base64.b64encode(image_bytes).decode("utf-8")
        
        # Send request to OpenAI
        response = client.chat.completions.create(
            model=endpoints["gpt_40"],
            messages=[
                {"role": "system", "content": "Describe the given image in 1 - 2 lines."},
                {"role": "user", "content": f"data:image/jpeg;base64,{base64_image}"}
            ]
        )
        print(response)

        if response.choices:
            return response.choices[0].message.content.strip()
        else:
            return "Sorry, I couldn't generate a description for this image."

    except Exception as e:
        return f"Error processing image: {str(e)}"
