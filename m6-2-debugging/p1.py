import logging
import colorlog

# Настройка цветного логирования
handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter(
    '%(log_color)s%(levelname)s:%(name)s:%(message)s'
))

logger = colorlog.getLogger('example')
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

# Теперь логи будут цветными
logger.debug("Подробная информация для отладки")      # СЕРЫЙ
logger.info("Общая информация о работе")              # БЕЛЫЙ  
logger.warning("Предупреждение о проблеме")           # ЖЕЛТЫЙ
logger.error("Ошибка в программе")                    # КРАСНЫЙ
logger.critical("Критическая ошибка!")                # КРАСНЫЙ жирный
               # CRITICAL