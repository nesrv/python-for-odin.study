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

def add_numbers(a,b):
    """Функция с примерами логгирования"""
    logger.debug(f"Начало выполнения add_numbers с параметрами: a={a}, b={b}") 
    if type(a) != int or type(b) != int:            
        try:
            a = int(a)
            b = int(b)
        except:
            logger.error(f"Неудалось преобразовать к числу : a={type(a)}, b={type(b)}")   
            return None    
            
    logger.info(f"Сложение чисел: {a} и {b}")
    return a + b

logger.debug("Программа запущена")
result = add_numbers(5, 3)
logger.info(f"Результат: {result}")
result = add_numbers(5, '30')

result = add_numbers("5.5", '30')
