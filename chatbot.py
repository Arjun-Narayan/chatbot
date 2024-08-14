import requests
from dotenv import load_dotenv
import os
import sys

load_dotenv('.env')
hugging_face_api_key = os.getenv("HUGGING_FACE_API_KEY")


API_URL = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
headers = {"Authorization": f"Bearer {hugging_face_api_key}"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def get_response(question):
    output = query({
            "inputs": question,
            "parameters": {
                "return_full_text": False
            }
    })
    print(output[0]['generated_text'])

get_response(sys.argv[1])