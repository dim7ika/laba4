# TODO импортировать необходимые молули

import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    try:
        with open(INPUT_FILENAME, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            data = list(reader)

        with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=4)
    except FileNotFoundError:
        print(f"Ошибка: Файл '{INPUT_FILENAME}' не найден.")

if __name__ == '__main__':
  # Для проверки
    task()
    try:
        with open(OUTPUT_FILENAME) as output_f:
            for line in output_f:
                print(line, end="")
    except FileNotFoundError:
        print(f"Ошибка: Выходной файл '{OUTPUT_FILENAME}' не найден")