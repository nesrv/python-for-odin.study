import logging
import colorlog

# Настройка логирования в файл с поддержкой кириллицы
file_handler = logging.FileHandler('app.log', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

# Настройка цветного вывода в консоль
console_handler = colorlog.StreamHandler()
console_handler.setFormatter(colorlog.ColoredFormatter(
    '%(log_color)s%(levelname)s: %(message)s'
))

# Создаем логгер и добавляем оба обработчика
logger = logging.getLogger('example')
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)     # Запись в файл
logger.addHandler(console_handler)  # Цветной вывод в консоль

# Тестируем логирование с кириллицей
logger.debug("Подробная информация для отладки")
logger.info("Общая информация о работе")
logger.warning("Предупреждение о проблеме")
logger.error("Ошибка в программе")
logger.critical("Критическая ошибка!")

print("\nЛоги сохранены в файл app.log с поддержкой кириллицы")