# TODO решите задачу
import json

def task(filepath):
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return 0

    total_sum = 0
    for item in data:
        try:
            score = float(item["score"])
            weight = float(item["weight"])
            total_sum += score * weight
        except (KeyError, ValueError, TypeError):
            continue

    return round(total_sum, 3)

filepath = 'input.json'
sum_of_products = task(filepath)
print(sum_of_products)