import json
from services.gemini_service import generate_response_image
from services.receipt_parser import parse_receipt
from services.splitter import even_split, item_split

def main():
    img_path = "examples/Example1.jpg" 

    # will add an upload feature later

    raw_response = generate_response_image(img_path)
    receipt_data = parse_receipt(raw_response)

    if not receipt_data:
        print("Failed to parse receipt data.")
        return
    
    print("Parsed Receipt Data:", json.dumps(receipt_data, indent=2))

    num_people = 3

    print(even_split(receipt_data, num_people))

    assignments = {
        1: [receipt_data["items"][0]["name"]],
        2: [receipt_data["items"][1]["name"]],
        3: [item["name"] for item in receipt_data["items"][2:]],
    }
    print(item_split(receipt_data, assignments))


if __name__ == "__main__":
    main()