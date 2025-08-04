# 1. Создать список из 20 случайных чисел (от - 100 до 100)

import random
random.seed(123)
lst = []

while len(lst) < 20:
    x = random.randint(-100, 100)
    lst.append(x)

# Посчитать количество чисел в диапазоне от 10 до 100

c, i = 0, 0

while i < len(lst):
    if 10 <= lst[i] <= 100:
        c += 1
    i += 1

print("кол-во: ", c)

