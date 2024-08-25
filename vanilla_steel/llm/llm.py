import requests
import json
from vanilla_steel.config import logger

def get_llm_output(prompt: str, options: dict = None, format: str = None):
    api_url = "http://localhost:11434/api/generate"
    default_options = {
        "seed": 123,
        "temperature": 0.8
    }
    options = default_options if options is None else options
    payload = {
        "model": "mistral:7b",
        "prompt": prompt,
        "stream": False,
        "options": options
    }
    if format is not None:
        payload["format"] = "json"
    headers = {
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(api_url, headers=headers, data=json.dumps(payload))
        if response.status_code == 200:
            if format:
                output = response.json()["response"]
                return json.loads(output)
            else:
                output = json.loads(response.text)
                return output["response"]
        else:
            logger.error(f"Failed with status code {response.status_code}")
            return response.text
    except Exception as e:
        logger.error(f"An error occurred: {e}")
    return None