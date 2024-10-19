numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# Находим среднее арифметическое всех элементов, кроме None
valid_numbers = [num for num in numbers if num is not None]
average = sum(valid_numbers) / (len(valid_numbers)+1)

# Заменяем None на среднее арифметическое
for i in range(len(numbers)):
    if numbers[i] is None:
        numbers[i] = average

# Вывод измененного списка
print("Измененный список:", numbers)
