import json
from utils.helpers import remove_json_block

def parse_receipt(response: str):
    cleaned = remove_json_block(response)

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError as e:
        print("JSON Decode Error:", e)
        print("Raw output:", cleaned)
        return None