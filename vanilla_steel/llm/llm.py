import requests
import json

def get_llm_output(prompt: str, options: dict = None):
    api_url = "http://localhost:11434/api/generate"
    default_options = {
        "seed": 123,
        "temperature": 0
    }
    options = default_options if options is None else options
    payload = {
        "model": "mistral:7b",
        "prompt": prompt,
        "context": [1],
        "format": "json",
        "function": "Answer Question", 
        "stream": False,
        "options": options
    }
    headers = {
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(api_url, headers=headers, data=json.dumps(payload))
        if response.status_code == 200:
            print("Request was successful!")
            output = response.json()["response"]
            return json.loads(output)
        else:
            print(f"Failed with status code {response.status_code}")
            return response.text
    except Exception as e:
        print(f"An error occurred: {e}")
    return None