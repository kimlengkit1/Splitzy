def remove_json_block(raw_string: str):
    if raw_string.startswith("```json") and raw_string.endswith("```"):
        return raw_string[7:-3].strip()
    return raw_string