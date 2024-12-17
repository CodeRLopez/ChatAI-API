import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

def gemini_ai_client() -> genai:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("API key not found")
    try:
        print("Gemini AI client configured successfully.")
        genai.configure(api_key=api_key)
        return genai
    except Exception as e:
        raise ValueError(f"Error creating GeminiAI client: {e}")
