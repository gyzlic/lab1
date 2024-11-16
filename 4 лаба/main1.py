import json


def task():
    # Загружаем данные из строки JSON
    with open('input.json', 'r') as file:
        data = json.load(file)

    # Вычисляем сумму произведений
    total_sum = sum(item["score"] * item["weight"] for item in data)

    # Возвращаем результат, округленный до 3 знаков
    return round(total_sum, 3)



print(task())
