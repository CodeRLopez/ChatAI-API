import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def open_ai_client() -> OpenAI:
    api_key = os.getenv("OPEN_AI_KEY")
    if not api_key:
        raise ValueError("API key not found")
    try:
        print("OpenAI client configured successfully.")
        return OpenAI(api_key=api_key)
    except Exception as e:
        raise ValueError(f"Error creating OpenAI client: {e}")
