import time

print(1, time.time())  # текущее время в секундах с начала эпохи (Unix-время)
time.sleep(0.2)  # Программа "засыпает" на 2 секунды

print(2, time.ctime())  # преобразует время в секундах в читаемую строку

local_time = time.localtime()

# возвращает struct_time (локальное время): time.struct_time(tm_year=2025, tm_mon=8, ...)
print(3, local_time)

# преобразует struct_time обратно в секунды: 1722684432.0
print(4, time.mktime(local_time))

# struct_time, но в UTC (Гринвич): time.struct_time(tm_year=2025, tm_mon=8, ...)
print(5, time.gmtime())

# Разбирает дату из строки в struct_time
print(6, time.strptime("2025-08-04", "%Y-%m-%d"))

# форматирует время: "04.08.2025 14:30"
formatted_time = time.strftime("%d.%m.%Y %H:%M")
print(7, formatted_time)

asc_time = time.asctime(local_time) 
print(8, asc_time)
# аналог ctime(), но принимает struct_time.Например: "Sun Aug  4 14:30:15 2025"
