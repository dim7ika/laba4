# TODO решите задачу
import json

def task(filepath):
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return 0

    total_sum = sum(product_gen(data))

    return round(total_sum, 3)

def product_gen(data):
    for item in data:
        try:
            score = float(item["score"])
            weight = float(item["weight"])
            yield score * weight
        except (KeyError, ValueError, TypeError):
            continue


filepath = 'input.json'
sum_of_products = task(filepath)
print(sum_of_products)
