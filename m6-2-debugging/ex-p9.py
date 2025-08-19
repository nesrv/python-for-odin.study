def add_numbers(a, b):
    result = a + b
    return result


numbers = [5, 3]  # Ошибка: строка вместо числа
total = add_numbers(numbers[0], numbers[1])
print(total)


numbers = [5, "3"]  # Ошибка: строка вместо числа
total = add_numbers(numbers[0], numbers[1])
print(total)