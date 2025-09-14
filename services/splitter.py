def even_split(receipt_data: dict, num_people: int):
    total = receipt_data.get("total", 0.0)
    per_person = round(total / num_people, 2) if num_people > 0 else 0
    return {f"Person {i+1}": per_person for i in range(num_people)}

def item_split(receipt_data: dict, assignments: dict):
    results = {f"Person {i}": 0.0 for i in assignments.keys()}
    items = receipt_data.get("items", [])

    for item in items:
        for person, person_items in assignments.items():
            if item['name'] in person_items:
                results[f"Person {person}"] += item['price']

    return {p: round(v, 2) for p, v in results.items()}

def smart_split():
    "need to implement"
    return None
