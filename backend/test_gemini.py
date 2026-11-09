import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = os.getenv("GEMINI_MODEL", "gemini-3.5-flash-lite")

client = genai.Client(api_key=API_KEY)

try:
    print(f"Testing model: {MODEL}")

    response = client.models.generate_content(
        model=MODEL,
        contents="Hello! Introduce yourself as a customer support assistant."
    )

    print("\nGemini Response:")
    print(response.text)

except Exception as e:
    print("\nGemini Error:")
    print(e)