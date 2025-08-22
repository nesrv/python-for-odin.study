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

# logger.debug("Подробная информация для отладки")      # СЕРЫЙ
# logger.info("Общая информация о работе")              # БЕЛЫЙ  
# logger.warning("Предупреждение о проблеме")           # ЖЕЛТЫЙ
# logger.error("Ошибка в программе")                    # КРАСНЫЙ
# logger.critical("Критическая ошибка!")                # КРАСНЫЙ жирный

from typing import Union


def add_numbers(a:Union[int, str, float], b:Union[int, str, float]) -> Union[float, None]:
    """Функция с примерами логгирования"""
    logger.debug(f"Начало выполнения add_numbers с параметрами: a={a}, b={b}") 
    # if type(a) != int or type(b) != int:            
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):            
        try:
            logger.warning(f"Попытка преобразовать к числу : {a}={type(a)}, {b}={type(b)}")
            a = float(a)
            b = float(b)
        except :
            logger.critical(f"Неудалось преобразовать к числу : {a}={type(a)}, {b}={type(b)}")   
            return None    
            
    logger.info(f"Сложение чисел: {a} и {b}")
    return a + b

logger.debug("Программа запущена")
result = add_numbers(5, 3)
logger.info(f"Результат: {result}")

result = add_numbers(5, '30')
logger.info(f"Результат: {result}")

result = add_numbers("5.5", '30')
logger.info(f"Результат: {result}")

result = add_numbers("hello", '30')
logger.info(f"Результат: {result}")

name:str = "John"

def add_a_b(a: int, b: int) -> float:
    """Функция с примерами логгирования"""
    logger.debug(f"Начало выполнения add_numbers с параметрами: a={a}, b={b}")
    return a + b

result =  add_a_b(5, 10)