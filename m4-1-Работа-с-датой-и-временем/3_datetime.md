
### **1. Основные методы класса `datetime`**  
- `now()` — текущая дата и время (локальные)  
- `utcnow()` — текущая дата и время (UTC)  
- `strptime(date_string, format)` — парсит строку в `datetime`  
- `strftime(format)` — форматирует `datetime` в строку  
- `timestamp()` — преобразует в UNIX-время (секунды с 1970-01-01)  
- `fromtimestamp(ts)` — создаёт `datetime` из UNIX-времени  
- `combine(date, time)` — объединяет `date` и `time` в `datetime`  

### **2. Методы объектов `datetime`**  
- `date()` — возвращает объект `date` (без времени)  
- `time()` — возвращает объект `time` (без даты)  
- `replace()` — заменяет указанные компоненты (год, месяц и т.д.)  
- `timetz()` — возвращает `time` с часовым поясом  
- `toordinal()` — преобразует в количество дней от 1-го года  
- `weekday()` — день недели (0=понедельник, 6=воскресенье)  
- `isoweekday()` — день недели (1=понедельник, 7=воскресенье)  
- `isocalendar()` — кортеж `(год, номер недели, день недели)`  

### **3. Арифметика с `timedelta`**  
- `+ timedelta` — прибавляет интервал времени  
- `- timedelta` — вычитает интервал времени  
- `- datetime` — возвращает `timedelta` между датами  

### **4. Атрибуты `datetime`**  
- `.year` — год (например, `2023`)  
- `.month` — месяц (1–12)  
- `.day` — день (1–31)  
- `.hour` — час (0–23)  
- `.minute` — минуты (0–59)  
- `.second` — секунды (0–59)  
- `.microsecond` — микросекунды (0–999999)  
- `.tzinfo` — информация о часовом поясе  

### **Примеры использования**  
```python
from datetime import datetime, timedelta

dt = datetime.now()  # текущая дата и время
print(dt.strftime("%d.%m.%Y"))  # форматирование
delta = timedelta(days=7)
new_date = dt + delta  # дата через 7 дней
```

Это основные методы, которые покрывают 90% задач работы с датой и временем в Python. Для сложных операций (часовые пояса) используйте `pytz` или `zoneinfo`.


```python
from datetime import datetime, timedelta, date, time

# 1. Текущая дата и время
now = datetime.now()  # datetime(2023, 12, 15, 14, 30, 45)

# 2. Создание конкретной даты
dt = datetime(2023, 12, 31, 23, 59)  # datetime(2023, 12, 31, 23, 59)

# 3. Разбор строки в datetime
parsed = datetime.strptime("2023-12-25", "%Y-%m-%d")  # datetime(2023, 12, 25)

# 4. Форматирование datetime в строку
formatted = dt.strftime("%d.%m.%Y %H:%M")  # "31.12.2023 23:59"

# 5. Получение отдельных компонентов
year, month, day = now.year, now.month, now.day  # (2023, 12, 15)

# 6. Операции с timedelta
future = now + timedelta(days=7)  # datetime(2023, 12, 22, 14, 30, 45)

# 7. Разница между датами
diff = future - now  # timedelta(days=7)

# 8. Только дата (без времени)
today = date.today()  # date(2023, 12, 15)

# 9. Только время (без даты)
t = time(14, 30)  # time(14, 30)

# 10. Замена компонентов
modified = now.replace(year=2024)  # datetime(2024, 12, 15, 14, 30, 45)

# 11. UNIX timestamp
timestamp = datetime.timestamp(now)  # 1671103845.0

# 12. Из timestamp
from_ts = datetime.fromtimestamp(1671103845)  # datetime(2023, 12, 15, 14, 30, 45)

# 13. День недели (0-6, понедельник=0)
weekday = now.weekday()  # 4 (если пятница)

# 14. Проверка даты на валидность
is_valid = date(2023, 2, 28)  # Корректная дата (не вызовет ошибку)

# 15. Максимальные/минимальные даты
max_date = datetime.max  # datetime(9999, 12, 31, 23, 59, 59, 999999)
```

