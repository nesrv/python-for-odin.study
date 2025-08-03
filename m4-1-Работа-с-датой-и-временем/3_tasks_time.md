# Задачи на time:

### 1. **Секундомер с автостартом**
Задача: Напишите код, который автоматически запускает секундомер, ждет 3.7 секунды, а затем выводит фактически прошедшее время с точностью до миллисекунд.

```python
import time

start = time.perf_counter()
time.sleep(3.7)
end = time.perf_counter()
print(f"Прошло {end - start:.3f} секунд")  # Должно быть близко к 3.700
```

### 2. **Время до Нового Года**
Задача: Рассчитайте, сколько секунд осталось до следующего Нового Года, используя текущее время.

```python
import time

now = time.localtime()
new_year = time.struct_time((now.tm_year + 1, 1, 1, 0, 0, 0, 0, 0, 0))
seconds_left = time.mktime(new_year) - time.time()
print(f"До Нового Года осталось {int(seconds_left)} секунд")
```

### 3. **Рандомная пауза**
Задача: Сделайте паузу в выполнении программы на случайное время от 1 до 5 секунд, используя только модуль `time` (без `random`).

```python
import time

# Используем микросекунды текущего времени для "рандомности"
pause_duration = 1 + (time.time() % 4)  # 1-5 секунд
print(f"Пауза на {pause_duration:.2f} секунд...")
time.sleep(pause_duration)
print("Продолжаем!")
```

### 4. **Часы в формате 24ч**
Задача: Выведите текущее время в формате "HH:MM:SS", обновляя его каждую секунду в течение 5 секунд.

```python
import time

for _ in range(5):
    current = time.localtime()
    print(f"{current.tm_hour:02d}:{current.tm_min:02d}:{current.tm_sec:02d}", end='\r')
    time.sleep(1)
```

### 5. **Сравнение скорости операций**
Задача: Сравните скорость создания списка через генератор и через цикл for, используя `time.perf_counter()`.

```python
import time

# Генератор
start_gen = time.perf_counter()
lst_gen = [x for x in range(1_000_000)]
end_gen = time.perf_counter()

# Цикл
start_loop = time.perf_counter()
lst_loop = []
for x in range(1_000_000):
    lst_loop.append(x)
end_loop = time.perf_counter()

print(f"Генератор: {end_gen - start_gen:.5f} сек")
print(f"Цикл: {end_loop - start_loop:.5f} сек")
```


Сколько времени ты уже в этом мире?"
Задача:
Напишите программу, которая:

Запрашивает дату рождения пользователя

Рассчитывает прожитое время в секундах, минутах, часах и днях

Использует только модуль time (без datetime)

Добавляет визуализацию в виде "прогресс-бара" жизни (условные 90 лет)


```python
import time

# Ввод даты рождения
print("Введите дату рождения в формате ДД.ММ.ГГГГ")
day, month, year = map(int, input().split('.'))

# Получаем текущее время и время рождения в секундах
now = time.time()
birth_time = time.mktime((year, month, day, 0, 0, 0, 0, 0, -1))

# Расчет прожитого времени
seconds_lived = now - birth_time
minutes = seconds_lived / 60
hours = minutes / 60
days = hours / 24
years = days / 365.25

# Вычисляем процент прожитой жизни (условно до 90 лет)
life_percent = (years / 90) * 100 if years < 90 else 100

# Вывод результатов
print("\n=== ВАШ ВОЗРАСТ ===")
print(f"Секунд: {int(seconds_lived):,}")
print(f"Минут: {int(minutes):,}")
print(f"Часов: {int(hours):,}")
print(f"Дней: {int(days):,}")
print(f"Лет: {years:.2f}")

# Визуализация прогресса жизни
print("\n[Прогресс жизни]")
bar_length = 50
filled = int(life_percent * bar_length / 100)
progress_bar = '[' + '#' * filled + '-' * (bar_length - filled) + ']'
print(f"{progress_bar} {life_percent:.1f}%")

# Особые сообщения
if years < 18:
    print("\nВы еще молодой! Впереди целая жизнь :)")
elif years < 40:
    print("\nСамое продуктивное время! Используйте его мудро!")
else:
    print("\nОпыт - ваше главное богатство!")
```

Особенности этого решения:
1. Используется только модуль `time` (без datetime)
2. Нет ни одной пользовательской функции
3. Добавлен графический прогресс-бар жизни
4. Есть персонализированные сообщения в зависимости от возраста
5. Корректно обрабатывает високосные годы (используется 365.25 дней в году)
6. Простой и понятный ввод даты рождения

