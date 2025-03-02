# from openai import AzureOpenAI

# AZURE_OPENAI_API_KEY = "DWXVJ9PhzqXbwdJMicfbOAjY4aHKb7Mvjiy0qukDrccEAviT9q67JQQJ99BAACYeBjFXJ3w3AAABACOG0CsL"
# AZURE_OPENAI_ENDPOINT = "https://openai-agco-poc.openai.azure.com"

# # Initialize the AzureOpenAI client
# client = AzureOpenAI(
#     api_key=AZURE_OPENAI_API_KEY,
#     api_version="2024-10-21",
#     azure_endpoint=AZURE_OPENAI_ENDPOINT
# )

# # Define the endpoints
# endpoints = {
#     "gpt_40": "gpt-4o-2",
#     "gpt_o1_mini": "o1-mini"
# }

# # Define the payload
# payload = {
#     "messages": [
#         {"role": "user", "content": "Hello, how are you?"}
#     ]
# }

# # Function to test an endpoint
# def test_endpoint(name, deployment_id):
#     response = client.chat.completions.create(
#         model=deployment_id,
#         messages=payload["messages"]
#     )
#     if response:
#         # print(f"{name} endpoint is working. Response: {response}")
#         # Extracting the message content from the response
#         # Extracting the message content from the response
#         message_content = response.choices[0].message.content
#         print(message_content)


#     else:
#         print(f"\n\n{name} endpoint failed. Response: {response}")

# # Test both endpoints
# for name, deployment_id in endpoints.items():
#     test_endpoint(name, deployment_id)


from openai import AzureOpenAI

# Azure OpenAI setup
AZURE_OPENAI_API_KEY = "DWXVJ9PhzqXbwdJMicfbOAjY4aHKb7Mvjiy0qukDrccEAviT9q67JQQJ99BAACYeBjFXJ3w3AAABACOG0CsL"
AZURE_OPENAI_ENDPOINT = "https://openai-agco-poc.openai.azure.com"
azure_client = AzureOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    api_version="2024-10-21",
    azure_endpoint=AZURE_OPENAI_ENDPOINT
)

def generate_farmer_response():
    # Hardcoded weather and news details
    weather = {
        "temperature": "52°F",
        "precipitation": "10%",
        "soil_moisture": "Optimal",
        "wind_speed": "5 mph"
    }

    news = [
        {
            "headline": "New No-Till Techniques Reduce Soil Erosion by 30%",
            "source": "AgriTech Journal",
            "link": "https://example.com/news/no-till"
        }
    ]

    # Simulated LLM output from Azure
    llm_response = """
    Based on current conditions, strip tillage is recommended. 
    This method minimizes soil disturbance, conserves moisture, and improves crop yield.
    """

    # Structuring response using Azure OpenAI
    structured_prompt = f"""
    The following is a recommendation from an AI model providing tillage suggestions for a farmer:
    "{llm_response}"

    The weather conditions are:
    - Temperature: {weather['temperature']}
    - Precipitation: {weather['precipitation']}
    - Soil Moisture: {weather['soil_moisture']}
    - Wind Speed: {weather['wind_speed']}

    Latest agriculture news:
    {news}

    Please structure the response in a presentable manner with the following pointers:
    - Query: What tillage method should I use today?
    - Location: Champaign, IL
    - Date: 2025-03-01
    - Weather: [List the detailed conditions]
    - Latest News: [Summarize key agricultural news]
    - Recommendation: [State the AI's tillage suggestion]
    - Justification: [List reasons for this recommendation]
    - Next Steps: [Provide 3 actionable suggestions for the farmer]

    For each pointer, provide a brief description or list of relevant details.
    """

    # Get the response from the Azure OpenAI model
    response = azure_client.chat.completions.create(
        model="gpt-4o-2",  # Use your Azure deployment model here
        messages=[{"role": "user", "content": structured_prompt}]
    )

    # Extract the content from the response correctly
    response_content = response.choices[0].message.content
    return response_content

# Run function
print(generate_farmer_response())
