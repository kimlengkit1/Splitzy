import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv() #loads .env

genai.configure(api_key=os.getenv("API_KEY"))

generation_config = {
    "temperature": 0, # deterministic output
    "top_p": 0.95, # nucleus sampling -> more flexibility in recognizing weird names
    "top_k": 64, # look at top 64 possible words
    "max_output_tokens": 8192, # max tokens
    #"response_mime_type": "text/plain", # json
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

# model setup
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    safety_settings=safety_settings,
    system_instruction=(
        "You are an AI that extracts structured data from receipts. "
        "Always return JSON only with no extra text or explanations, formatted as: "
        "{'items': [{'name': 'example', 'price': 0.0}], 'subtotal': 0.0, 'tax': 0.0, 'total': 0.0}"
    ),
)