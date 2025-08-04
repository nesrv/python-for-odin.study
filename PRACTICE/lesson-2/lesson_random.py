# RANDOM + циклы
from random import *

# print(randint(1, 100))
# print(random())
# print(randrange(0, 100, 10))

# print(choice("питон"))
# print(shuffle("питон"))

import time

i = 0
while (i := i + 1) <= 10:  # проверка на истинность
    print(f"работаю ... {i}")
    time.sleep(0.1)
    if i == 5:
        break
else:
    print("все ок")    
print("the end")
   
while (password := input()) != "123":   
    print(f"пароль неверный - {password}")

print("доступ разрешен")

# CTRL + C

# ALT + SHIFT + F
