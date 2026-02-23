import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
print("API KEY LOADED:", OPENAI_API_KEY)
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

AI_MODE = os.getenv("AI_MODE", "online")
VOICE_MODE = os.getenv("VOICE_MODE", "offline")

WAKE_WORD = os.getenv("WAKE_WORD", "jarvis")

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")