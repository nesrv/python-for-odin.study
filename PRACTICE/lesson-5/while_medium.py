# Начав тренировки, лыжник в первый день пробежал 10 км.
# Каждый следующий день он увеличивал пробег на 10 %
# от пробега предыдущего дня
#
# Определить в какой день он пробежит больше
# 50 км (натуральное число x вводится с клавиатуры).

import random
import time


# Датчик температуры каждую секунду передает значение.
# Если 5 раз подряд температура превышает 70 °C,
# и прекратить мониторинг.

import random
import time

# c = 0
# while True:
#     t = random.randint(30, 100)
#     if t > 70:
#         c += 1
#         print(f"{c})Температура {t}°C")
#     if c == 5:
#         print(f"Критический перегрев устройства ! {t}°C")
#         break
#     time.sleep(0.2)


lst = [True, True, False, True]
# `True` — успешная транзакция, `False` — ошибка
# Нужно обрабатывать их, пока не встретится первая неудачная

# i = 0
# while i < len(lst):
#     if not lst[i]:
#         print("неудача")
#         break
#     print(f"удача {i}")
#     i += 1

# print ('-' * 10)

# while lst:
#     if lst.pop(0) == False:
#         print("неудача")
#         break
#     print(f"удача ")


lst = [True, True, None, True]

# any all

# print(any(lst))
# print("удача" if all(lst) else "неудача")
'''
xxx
0x0
0x0
'''

lst = [5, 2, 4, 2, 3, 5, 2, 4]
# Нужно посчитать средний балл, исключая двойки
s, c = 0, 0

# while lst:
#     x = lst.pop(0)
#     if x == 2:
#         continue
#     s += x
#     c += 1

# print(s / c)


passwords = ["123",  "password",  "abcdefg",  "strongPass1",  "12",
             "Secure@123",  "Admin#2036",  "aaaBcd@1",   "qwerty", " Admin#2024"
      ]
# Длина пароля > 6 символов
# Не содержит словарных слов `password`, `admin`, `qwerty`
# Не содержит 2х одинаковых символов 

stop_words = ["password", "admin", "qwerty"]


for password in passwords:
    if len(password) > 6 \
        and password not in stop_words \
            and len(password) == len(set(password)) :
        print(f'{password} - сильный')


x = '12345'
print(x, set(x))