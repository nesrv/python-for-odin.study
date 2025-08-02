# Шпаргалка по модулю `time` в Python

## Основные функции модуля `time`

### 1. Текущее время
```python
import time

# Возвращает текущее время в секундах с начала эпохи (1 января 1970 UTC)
current_time = time.time()
print(current_time)  # Пример: 1634567890.123456
```

### 2. Преобразование времени
```python
# Преобразует время в секундах в строку формата "Day Month Date HH:MM:SS Year"
local_time = time.ctime(current_time)
print(local_time)  # Пример: "Mon Oct 18 12:38:10 2021"

# Преобразует время в секундах в struct_time (локальное время)
local_struct = time.localtime(current_time)
print(local_struct)
# Вывод: time.struct_time(tm_year=2021, tm_mon=10, tm_mday=18, tm_hour=12, ...)

# Преобразует время в секундах в struct_time (UTC)
utc_struct = time.gmtime(current_time)
print(utc_struct)

# Преобразует struct_time обратно в секунды
seconds = time.mktime(local_struct)
print(seconds)
```

### 3. Форматирование времени
```python
# Форматирование struct_time в строку
formatted = time.strftime("%Y-%m-%d %H:%M:%S", local_struct)
print(formatted)  # Пример: "2021-10-18 12:38:10"

# Парсинг строки времени в struct_time
parsed = time.strptime("2021-10-18", "%Y-%m-%d")
print(parsed)
```

### 4. Задержки
```python
# Приостанавливает выполнение программы на указанное количество секунд
time.sleep(2.5)  # Спит 2.5 секунды
```

### 5. Измерение времени выполнения
```python
start = time.perf_counter()  # Наиболее точный таймер
# Код, время выполнения которого нужно измерить
end = time.perf_counter()
print(f"Время выполнения: {end - start:.4f} секунд")

# Альтернатива (менее точная)
start = time.time()
# Код...
end = time.time()
print(f"Время выполнения: {end - start:.4f} секунд")
```

## Форматы для strftime и strptime

| Код | Значение                     | Пример         |
|-----|------------------------------|----------------|
| %Y  | Год с веком                  | 2021           |
| %y  | Год без века (00-99)         | 21             |
| %m  | Месяц (01-12)                | 10             |
| %d  | День месяца (01-31)          | 18             |
| %H  | Час (00-23)                  | 14             |
| %I  | Час (01-12)                  | 02             |
| %M  | Минуты (00-59)               | 38             |
| %S  | Секунды (00-59)              | 10             |
| %A  | Полное название дня недели   | Monday         |
| %a  | Сокращенное название дня     | Mon            |
| %B  | Полное название месяца       | October        |
| %b  | Сокращенное название месяца  | Oct            |
| %p  | AM/PM                        | PM             |
| %Z  | Название часового пояса      | MSK            |
| %z  | Смещение часового пояса      | +0300          |
| %j  | День года (001-366)          | 291            |
| %U  | Номер недели в году (00-53)  | 42             |
| %c  | Локальное представление даты/времени | Mon Oct 18 14:38:10 2021 |
| %x  | Локальное представление даты | 10/18/21       |
| %X  | Локальное представление времени | 14:38:10    |

## Примеры использования

### Таймер обратного отсчета
```python
for i in range(5, 0, -1):
    print(i)
    time.sleep(1)
print("Время вышло!")
```

### Измерение скорости выполнения функции
```python
def some_function():
    time.sleep(0.5)  # Имитация работы

start = time.perf_counter()
some_function()
end = time.perf_counter()
print(f"Функция выполнилась за {end - start:.4f} секунд")
```

### Форматирование времени выполнения
```python
def format_elapsed_time(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{int(hours):02d}:{int(minutes):02d}:{seconds:06.3f}"

elapsed = 3678.456
print(format_elapsed_time(elapsed))  # 01:01:18.456
```