import PIL.Image
from config.settings import model

def generate_response_image(img_path: str) -> str:
    img = PIL.Image.open(img_path)

    instructions = (
        "Extract this receipt into JSON only. "
        "Format: {'items': [{'name': 'example', 'price': 0.0}], 'subtotal': 0.0, 'tax': 0.0, 'total': 0.0}"   
    )

    response = model.generate_content([instructions, img]) # stream=False to avoid live streaming
    return response.text

