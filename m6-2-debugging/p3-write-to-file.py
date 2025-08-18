import logging
import colorlog

# Настройка цветного логирования
handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter(
    '%(log_color)s%(levelname)s: %(message)s'
))

logger = colorlog.getLogger('example')
logger.addHandler(handler)
logger.setLevel(logging.ERROR)

logging.basicConfig(
    filename='app.log',           # Имя файла
    level=logging.DEBUG,          # Минимальный уровень
    format='%(asctime)s - %(levelname)s - %(message)s'  # Формат
)


# Теперь логи будут цветными
logger.debug("Подробная информация для отладки")      # СЕРЫЙ
logger.info("Общая информация о работе")              # БЕЛЫЙ  
logger.warning("Предупреждение о проблеме")           # ЖЕЛТЫЙ
logger.error("Error in program")                    # КРАСНЫЙ
logger.critical("Critical error!")                # КРАСНЫЙ жирный