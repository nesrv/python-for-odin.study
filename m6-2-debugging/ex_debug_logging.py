import logging
import colorlog

# Настройка цветного логирования
handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter(
    '%(log_color)s%(levelname)s: %(message)s'
))

logger = colorlog.getLogger('example')
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)  # Изменил на DEBUG для показа всех сообщений

def add_numbers(a, b):
    """Function with logging examples"""
    logger.debug(f"Начало выполнения add_numbers с параметрами: a={a}, b={b}")
    
    # Проверяем типы данных
    if not isinstance(a, (int, float)):
        logger.warning(f"Параметр 'a' не является числом: {type(a)}")
        try:
            a = float(a)
            logger.info(f"Преобразовал 'a' в число: {a}")
        except ValueError:
            logger.error(f"Не удалось преобразовать 'a' в число: {a}")
            return None
    
    if not isinstance(b, (int, float)):
        logger.warning(f"Параметр 'b' не является числом: {type(b)}")
        try:
            b = float(b)
            logger.info(f"Преобразовал 'b' в число: {b}")
        except ValueError:
            logger.error(f"Не удалось преобразовать 'b' в число: {b}")
            return None
    
    result = a + b
    logger.debug(f"Вычисление: {a} + {b} = {result}")
    logger.info(f"Успешно выполнено сложение, результат: {result}")
    return result

def divide_numbers(a, b):
    """Function demonstrating critical error logging"""
    logger.debug(f"Начало деления: {a} / {b}")
    
    if b == 0:
        logger.critical("Критическая ошибка: деление на ноль!")
        raise ZeroDivisionError("Деление на ноль")
    
    result = a / b
    logger.info(f"Результат деления: {result}")
    return result

# Примеры использования
logger.info("Программа запущена")

# Пример 1: Обычное сложение
print("\n=== Пример 1: Обычное сложение ===")
result1 = add_numbers(5, 3)
print(f"Результат: {result1}")

# Пример 2: Сложение со строкой (преобразование)
print("\n=== Пример 2: Сложение со строкой ===")
numbers = [5, "3"]  # Ошибка: строка вместо числа
result2 = add_numbers(numbers[0], numbers[1])
print(f"Результат: {result2}")

# Пример 3: Непреобразуемая строка
print("\n=== Пример 3: Непреобразуемая строка ===")
result3 = add_numbers(10, "abc")
print(f"Результат: {result3}")

# Пример 4: Критическая ошибка
print("\n=== Пример 4: Критическая ошибка ===")
try:
    result4 = divide_numbers(10, 0)
except ZeroDivisionError as e:
    logger.error(f"Обработано исключение: {e}")
    print("Ошибка обработана")

logger.info("Программа завершена")