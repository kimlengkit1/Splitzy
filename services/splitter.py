import google.generativeai as genai
from config.settings import model
import json

def even_split(receipt_data: dict, num_people: int):
    total = receipt_data.get("total", 0.0)
    per_person = round(total / num_people, 2) if num_people > 0 else 0
    return {f"Person {i+1}": per_person for i in range(num_people)}

def smart_split(receipt_data: dict, num_people: int):
    receipt_json = json.dumps(receipt_data)


    chat = model.start_chat(history=[
        {
            "role": "user",
            "parts": [
                "You are a bill-splitting assistant. "
                "Ask clarifying questions about who ordered what items "
                "before suggesting a split. "
                "When asking, be specific about item"
                "Output ONLY valid text in this format when done asking clarifying questions:\n"
                "\"Person 1\" float (round it in dollars), ..."
                f"Parsed receipt:\n{receipt_json}"
                f"{num_people} people."
                "Split it fairly based on who ordered what."
                "You can categorize items as 'shared' if user doesn't give enough information.\n"
                "You can ask the users to confirm if someone order a specific category.\n"
                "Avoid asking questions that have already been answered.\n"
                "Start by asking me clarifying questions."
            ]
        }
    ])
    return chat

def continue_smart_split(chat, user_message: str):
    response = chat.send_message(user_message)
    return response.text


# this function could be done by AI

# def item_split(receipt_data: dict, assignments: dict):
#     results = {f"Person {i}": 0.0 for i in assignments.keys()}
#     items = receipt_data.get("items", [])

#     for item in items:
#         for person, person_items in assignments.items():
#             if item['name'] in person_items:
#                 results[f"Person {person}"] += item['price']

#     return {p: round(v, 2) for p, v in results.items()}