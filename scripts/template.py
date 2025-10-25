import os
from pathlib import Path
import requests
from prompts import EMOTIONS


def create_labeling_prompt(emotion, ...) -> str:
    """
    Build a prompt
    """
    base_prompt = (
        ""
    )

    tail = (
        ""
    )
    

    prompt = (
        f"{base_prompt}\n\n"
        f"{EMOTIONS[emotion]}\n\n"
        f"{tail}"
    )

    return prompt


def call_api(prompt, model, api, DEFAULT_MAX_TOK, DEFAULT_TEMP) -> str:
    """
    Send the prompt to the api
    """
    payload = {
        "model": ,
        "prompt": ,
        "max_tokens": DEFAULT_MAX_TOK,
        "temperature": DEFAULT_TEMP,
        "stream": False
    }
    try:
        r = requests.post(api_url, json=payload, timeout=45)
        r.raise_for_status()
        resp = r.json().get("response", "").strip()
        
    except Exception:
        return "" #default value on error

    return ""


def run():
    #putting it all together

if __name__ == "__main__":
    BASE_DIR = Path(__file__).resolve().parent.parent

    api = ""
    model = ""
    DEFAULT_MAX_TOK = ""
    DEFAULT_TEMP = ""

    run()
