import os

# Configuration
API_KEY = os.environ.get("GEMINI_API_KEY")
MODEL_ID = "gemini-2.0-flash"
TEMPERATURE = 0.1

if not API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable not set.")