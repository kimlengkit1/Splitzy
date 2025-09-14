import json
from services.gemini_service import generate_response_image
from services.receipt_parser import parse_receipt, parse_split_response
from services.splitter import even_split, smart_split, continue_smart_split

def ai_suggestion(receipt_data: dict, num_people: int):
    chat = smart_split(receipt_data, num_people)

    # force gemini to initiate the chat
    ai_response = continue_smart_split(chat, 
        "Start by asking clarifying question. One at a time. Tell the user one time that they can exit the chat by saying done or exit.")
    print("Splitzy:", ai_response)

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["done", "exit"]:
            break
        ai_response = continue_smart_split(chat, user_input)
        print("Splitzy", ai_response)


def main():

    # Change the image here
    img_path = "examples/Example1.jpg" 

    # will add an upload feature later

    raw_response = generate_response_image(img_path)
    receipt_data = parse_receipt(raw_response)

    if not receipt_data:
        print("Failed to parse receipt data.")
        return
    
    print("Parsed Receipt Data:", json.dumps(receipt_data, indent=2))

    # ask for how many people to split
    while True:
        num_people = input("How many people to split the bill? ")
        if num_people.isdigit() and int(num_people) > 0:
            num_people = int(num_people)
            break
        else:
            print("Please enter a valid positive integer.")

    valid_method = [1, 2]
    while True:
        split_method = input("Split method: \n1. Evenly \n2. Smart_ai \nInput the integer corresponding to the choice: ")
        if split_method.isdigit() and int(split_method) in valid_method:
            split_method = int(split_method)
            break
        else:
            print("Please enter a valid positive integer.")

    if split_method == 1:
        result = even_split(receipt_data, num_people)
        print("Even Split Result:", json.dumps(result, indent=2))
    elif split_method == 2:
        ai_suggestion(receipt_data, num_people)


if __name__ == "__main__":
    main()