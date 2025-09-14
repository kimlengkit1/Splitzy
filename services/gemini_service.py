import PIL.Image
from config.settings import model

def generate_response_image(img_path: str) -> str:
    img = PIL.Image.open(img_path)

    instructions = (
        "Return JSON only."
        "List each item separately (no stacking). "
        "Apply discounts to items (final price only)"
        "Don't add items with negative number to the JSON. that's a discount"
        "Split stacked names like '2 Md Ice Cof' into separate entries."
        "Any negative is a discount on the item above it"
        "Format: {'items': [{'name': 'example', 'price': 0.0}], 'subtotal': 0.0, 'tax': 0.0, 'total': 0.0}"   
    )

    response = model.generate_content([instructions, img]) # stream=False to avoid live streaming
    return response.text

