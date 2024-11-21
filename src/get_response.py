import os
import json
import requests
from utils import load_config


def get_response_from_API(message:str):
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    config = load_config("config/config.json")
    API_URL = config["API_URL"]
    headers = config["headers"]
    headers['Authorization'] = headers['Authorization'].replace("{OPENAI_API_KEY}",OPENAI_API_KEY)
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
             {
            "role": "system", 
            "content": "you are a smart chatbot."
            },
            {
            "role": "user",
            "content": message
            }],
        "temperature": 0.7
        }

    # Make the POST request
    response = requests.post(API_URL, headers=headers, data=json.dumps(data))

    # Handle the response
    if response.status_code == 200:
        response_data = response.json()
    else:
        print(f"Error {response.status_code}: {response.text}")
    

    return response_data