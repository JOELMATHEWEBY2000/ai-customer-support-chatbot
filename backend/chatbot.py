import os
import time

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = os.getenv("GEMINI_MODEL", "gemini-3.5-flash-lite")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY is missing from .env")

client = genai.Client(api_key=API_KEY)

SYSTEM_PROMPT = """
You are a professional AI customer support assistant.

Your responsibilities:
1. Answer customer questions politely.
2. Provide simple and clear explanations.
3. Help customers with orders, payments, shipping,
   cancellations and returns.
4. Do not invent company policies or order information.
5. If information is unavailable, tell the customer
   to contact human customer support.
6. Keep responses concise and helpful.
"""

def generate_response(message: str, history: list):

    contents = []

    for item in history:
        contents.append(
            types.Content(
                role=item["role"],
                parts=[
                    types.Part.from_text(text=item["content"])
                ]
            )
        )

    contents.append(
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=message)]
        )
    )

    for attempt in range(3):

        try:

            response = client.models.generate_content(
                model=MODEL,
                contents=contents,
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM_PROMPT,
                    temperature=0.4,
                    max_output_tokens=500
                )
            )

            if not response.text:
                raise RuntimeError("Empty Gemini response")

            return response.text

        except Exception as e:

            error = str(e)

            if "503" in error and attempt < 2:

                wait_time = 2 ** (attempt + 1)

                print(
                    f"Gemini temporarily unavailable. "
                    f"Retrying in {wait_time} seconds..."
                )

                time.sleep(wait_time)

            else:
                raise