from google import genai
from .config import API_KEY

def get_client():
    """Returns an authenticated Gemini client."""
    return genai.Client(api_key=API_KEY)