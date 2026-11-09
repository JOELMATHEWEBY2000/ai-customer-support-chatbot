from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

print("Available Gemini models:\n")

for model in client.models.list():
    print("Model:", model.name)
    print("Methods:", model.supported_actions)
    print("----------------------")