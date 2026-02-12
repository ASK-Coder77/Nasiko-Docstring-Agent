import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

API_KEY = os.environ.get("GEMINI_API_KEY")
MODEL_ID = "gemini-2.0-flash"
TEMPERATURE = 0.1

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found. Make sure you have a .env file with your key!")