# Функции высшего порядка и паттерны программирования

## Задача 1: Рекурсивная сумма вложенных списков

**Описание:** Вычислить сумму всех чисел во вложенном списке любой глубины.

```python
lst = [1, 2, [1, 2, 3], 4, [1, 2, 3, [1, 2, 3, [1, 2, 3]]]]

def sum_list(lst):
    total = 0
    for item in lst:
        if isinstance(item, list):  # Проверяем, является ли элемент списком
            total += sum_list(item)  # Рекурсивный вызов для вложенного списка
        else:
            total += item  # Добавляем число к общей сумме
    return total

print(sum_list(lst))  # Результат: 30
```

## Задача 2: Количество программ исполнителя

**Описание:** Исполнитель может прибавлять 1 или 3. Найти количество способов получить 17 из 1, проходя через 9.

```python
def count_paths(start, target):
    """Подсчет количества путей от start до target"""
    if start == target:
        return 1  # Достигли цели
    if start > target:
        return 0  # Превысили цель
    # Суммируем пути через команды +1 и +3
    return count_paths(start + 1, target) + count_paths(start + 3, target)

# Количество путей от 1 до 17 через 9
result = count_paths(1, 9) * count_paths(9, 17)
print(f"Количество программ: {result}")
```

## Задача 3: Фильтрация строк с помощью функций высшего порядка

### 3.1 Проверка отсутствия русских букв

```python
string = '1 a1 фb2  c3 abc100 10'

# Используем all() и map() для проверки каждого символа
has_no_russian = all(map(lambda char: not ('а' <= char.lower() <= 'я'), string))
print(f"Нет русских букв: {has_no_russian}")  # False (есть 'ф')
```

### 3.2 Фильтрация файлов Python

```python
file_names = 'main.py run.py app.py fastapi.py'

# Используем filter() для отбора файлов .py
py_files = list(filter(lambda name: name.endswith('.py'), file_names.split()))
print("Python файлы:", py_files)
```

### 3.3 Фильтрация городов без спецсимволов

```python
cities = 'Анапа \nАнадырь \nАбакан Альметьевск'

# Фильтруем города, убирая те, что содержат спецсимволы
clean_cities = list(filter(lambda city: '\\' not in city, cities.split()))
print("Города без спецсимволов:", clean_cities)
```

### 3.4 Фильтрация полных квадратов

```python
import math

quad = '10 25 49 81 100'

# Проверяем, является ли число полным квадратом
def is_perfect_square(n):
    sqrt_n = int(math.sqrt(n))
    return sqrt_n * sqrt_n == n

# Фильтруем полные квадраты
perfect_squares = list(filter(lambda x: is_perfect_square(int(x)), quad.split()))
print("Полные квадраты:", perfect_squares)  # ['25', '49', '81', '100']
```

## Задача 4: Площадь квартиры с map и reduce

```python
from functools import reduce

rooms = [
    {"name": "кухня", "length": 6, "width": 4},
    {"name": "комната 1", "length": 5.5, "width": 4.5},
    {"name": "комната 2", "length": 5, "width": 4},
    {"name": "комната 3", "length": 7, "width": 6.3},
]

# Используем map для вычисления площади каждой комнаты
areas = map(lambda room: room["length"] * room["width"], rooms)

# Используем reduce для суммирования всех площадей
total_area = reduce(lambda x, y: x + y, areas)

print(f"Общая площадь квартиры: {total_area} кв.м")  # 88.25 кв.м
```

## Задача 5: Обработка списка предметов

```python
items_data = [
    "зонт=1000",
    "палатка=10000", 
    "спички=22",
    "котелок=543"
]

# Преобразуем строки в кортежи (название, вес)
items_tuples = tuple(map(lambda item: tuple(item.split('=')), items_data))

# Фильтруем предметы с весом >= 500
heavy_items = filter(lambda item: int(item[1]) >= 500, items_tuples)

# Извлекаем только названия и выводим через пробел
result = ' '.join(map(lambda item: item[0], heavy_items))
print(result)  # зонт палатка котелок
```

## Задача 6: Анализ текста

```python
text = '''     
1. Последнее королевство 2015
2. Рим 2005
3. Версаль 2015
4. Тюдоры 2007
5. Террор 2018
6. Человек в высоком замке 2015
7. Белая королева 2013
8. Братья по оружию 2001
9. Медичи 2016
10. Спартак 2010
'''

# Подсчет строк
lines = list(filter(lambda line: line.strip(), text.split('\n')))
line_count = len(lines)

# Подсчет слов (исключаем цифры)
words = []
for line in lines:
    words.extend(filter(lambda word: not word.isdigit(), line.split()))
word_count = len(words)

# Подсчет символов (без пробелов и точек)
char_count = len(list(filter(lambda char: char not in ' .', text)))

print(f"Количество строк: {line_count}")
print(f"Количество слов: {word_count}")
print(f"Число символов: {char_count}")
```

## Задача 7: Сортировка военнослужащих по званиям

```python
# Данные о военнослужащих
military_data = [
    "Иванов=лейтенант",
    "Петров=прапорщик", 
    "Сидоров=капитан",
    "Егоров=лейтенант",
    "Смирнов=рядовой"
]

# Порядок званий
ranks_order = [
    "рядовой", "сержант", "старшина", "прапорщик", 
    "лейтенант", "капитан", "майор", "подполковник", "полковник"
]

# Преобразуем в список списков [фамилия, звание]
lst = list(map(lambda item: item.split('='), military_data))

# Сортируем по индексу звания в списке ranks_order
lst_sorted = sorted(lst, key=lambda person: ranks_order.index(person[1]))

# Выводим результат
for person in lst_sorted:
    print(person)
```

## Основные паттерны функций высшего порядка

1. **map()** - применяет функцию к каждому элементу
2. **filter()** - отбирает элементы по условию
3. **reduce()** - сворачивает последовательность в одно значение
4. **all()/any()** - проверяют условия для всех/любого элемента
5. **sorted()** с key - сортировка по пользовательскому критерию