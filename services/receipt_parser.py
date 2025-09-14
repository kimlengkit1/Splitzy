import json
import ast
from utils.helpers import remove_json_block

def parse_receipt(response: str):
    cleaned = remove_json_block(response)

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError as e:
        try:
            return ast.literal_eval(cleaned)
        except Exception as e:
            print("Failed to parse receipt JSON:", e)
            print("Raw response was:", cleaned)
        return None