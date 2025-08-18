# Урок: Отладка кода с помощью logging

## Что такое logging?

**Logging** - это запись событий программы в файл или консоль для отслеживания работы и поиска ошибок.

**Зачем нужен logging:**

- Отслеживать ошибки в программе
- Понимать, как работает код
- Сохранять историю событий
- Заменить множество `print()` на профессиональный инструмент

## Уровни логирования

```python
import logging

# 5 основных уровней (от менее важного к более важному):
logging.debug("Подробная информация для отладки")      # DEBUG
logging.info("Общая информация о работе")              # INFO  
logging.warning("Предупреждение о проблеме")           # WARNING
logging.error("Ошибка в программе")                    # ERROR
logging.critical("Критическая ошибка!")                # CRITICAL
```

## Базовая настройка

```python
import logging

# Простая настройка - вывод в консоль
logging.basicConfig(level=logging.DEBUG)

logging.debug("Это сообщение для отладки")
logging.info("Программа запущена")
logging.warning("Внимание: низкий заряд батареи")
logging.error("Файл не найден"
```

## Запись в файл

```python
import logging

# Настройка записи в файл
logging.basicConfig(
    filename='app.log',           # Имя файла
    level=logging.DEBUG,          # Минимальный уровень
    format='%(asctime)s - %(levelname)s - %(message)s'  # Формат
)

logging.info("Программа запущена")
logging.error("Произошла ошибка")
```

## Практический пример: Калькулятор с логированием

```python
import logging

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('calculator.log'),  # В файл
        logging.StreamHandler()                 # В консоль
    ]
)

def divide(a, b):
    """Деление с логированием"""
    logging.info(f"Попытка деления {a} на {b}")
  
    if b == 0:
        logging.error("Деление на ноль!")
        return None
  
    result = a / b
    logging.info(f"Результат: {result}")
    return result

def calculator():
    """Простой калькулятор"""
    logging.info("Калькулятор запущен")
  
    try:
        a = float(input("Первое число: "))
        b = float(input("Второе число: "))
      
        result = divide(a, b)
        if result is not None:
            print(f"Результат: {result}")
        else:
            print("Ошибка вычисления")
          
    except ValueError as e:
        logging.error(f"Неверный ввод: {e}")
        print("Введите корректные числа")
  
    logging.info("Калькулятор завершен")

if __name__ == "__main__":
    calculator()
```

## Отладка функции с ошибками

```python
import logging

logging.basicConfig(level=logging.DEBUG, 
                   format='%(levelname)s:%(funcName)s:%(lineno)d - %(message)s')

def find_max_in_list(numbers):
    """Функция с ошибкой для демонстрации отладки"""
    logging.debug(f"Получен список: {numbers}")
  
    if not numbers:
        logging.warning("Пустой список!")
        return None
  
    max_num = numbers[0]
    logging.debug(f"Начальное максимальное значение: {max_num}")
  
    for i, num in enumerate(numbers[1:], 1):
        logging.debug(f"Проверяем элемент {i}: {num}")
      
        if num > max_num:
            logging.debug(f"Найдено новое максимальное: {num}")
            max_num = num
  
    logging.info(f"Максимальное значение: {max_num}")
    return max_num

# Тестирование
test_lists = [
    [1, 5, 3, 9, 2],
    [],
    [-1, -5, -2],
    [42]
]

for test_list in test_lists:
    print(f"\nТест со списком: {test_list}")
    result = find_max_in_list(test_list)
    print(f"Результат: {result}")
```

## Логирование исключений

```python
import logging

logging.basicConfig(level=logging.ERROR)

def risky_function(filename):
    """Функция, которая может вызвать ошибку"""
    try:
        with open(filename, 'r') as file:
            content = file.read()
            logging.info(f"Файл {filename} успешно прочитан")
            return content
    except FileNotFoundError:
        logging.error(f"Файл {filename} не найден", exc_info=True)
    except PermissionError:
        logging.error(f"Нет прав для чтения {filename}", exc_info=True)
    except Exception as e:
        logging.critical(f"Неожиданная ошибка: {e}", exc_info=True)
  
    return None

# Тестирование
risky_function("existing_file.txt")
risky_function("nonexistent_file.txt")
```

## Создание собственного логгера

```python
import logging

# Создаем именованный логгер
logger = logging.getLogger('MyApp')
logger.setLevel(logging.DEBUG)

# Создаем обработчик для файла
file_handler = logging.FileHandler('myapp.log')
file_handler.setLevel(logging.INFO)

# Создаем обработчик для консоли
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)

# Создаем форматтер
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Добавляем обработчики к логгеру
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Использование
logger.debug("Отладочное сообщение")      # Только в файл
logger.info("Информационное сообщение")   # Только в файл  
logger.warning("Предупреждение")          # В файл И консоль
logger.error("Ошибка")                    # В файл И консоль
```

## Практические советы

### 1. Что логировать:

```python
# ✅ Хорошо
logging.info("Пользователь вошел в систему")
logging.error("Не удалось подключиться к базе данных")
logging.debug(f"Обрабатываем файл: {filename}")

# ❌ Плохо
logging.info("i = 1")  # Слишком подробно
logging.error("Ошибка")  # Слишком общо
```

### 2. Уровни для разных ситуаций:

- **DEBUG** - подробная информация для разработчика
- **INFO** - важные события (запуск, завершение)
- **WARNING** - что-то необычное, но не критичное
- **ERROR** - ошибка, но программа продолжает работать
- **CRITICAL** - серьезная ошибка, программа может остановиться

### 3. Форматирование сообщений:

```python
# ✅ Информативно
logging.error(f"Не удалось открыть файл {filename}: {error}")

# ❌ Неинформативно  
logging.error("Ошибка файла")
```

## Заключение

**Logging помогает:**

- Быстро находить ошибки
- Понимать поведение программы
- Отслеживать производительность
- Создавать профессиональные приложения

**Начните с простого:**

1. Добавьте `logging.basicConfig(level=logging.INFO)`
2. Замените `print()` на `logging.info()`
3. Добавьте `logging.error()` в блоки `except`
4. Постепенно изучайте продвинутые возможности
