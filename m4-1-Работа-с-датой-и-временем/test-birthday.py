import time

# Ввод даты рождения
print("Введите дату рождения в формате ДД.ММ.ГГГГ")
# date_input = input("Дата: ")
date_input = "18.12.1978"
day, month, year = map(int, date_input.split('.'))

# Получаем текущее время и время рождения в секундах
now = time.time()
# birth_time = time.mktime((year, month, day, 0, 0, 0, 0, 0, 0))
birth_time = time.time((year, month, day))
print(now)
print(birth_time)

# print(f"Возраст в секундах: {int(now - birth_time)}")
# print(f"Возраст в днях: {int((now - birth_time) / 86400)}")
# print(f"Возраст в годах: {int((now - birth_time) / (86400 * 365.25))}")