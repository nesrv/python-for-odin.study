Для компиляции в exe используйте PyInstaller:

1. Установка:

pip install pyinstaller

Copy
bash
2. Компиляция:

pyinstaller --onefile keylog_mini.py

Copy
bash
3. Дополнительные опции:

# Без консольного окна (только GUI)
pyinstaller --onefile --windowed keylog_mini.py

# С иконкой
pyinstaller --onefile --windowed --icon=icon.ico keylog_mini.py

# Скрытый запуск
pyinstaller --onefile --noconsole keylog_mini.py

Copy
bash
Результат:

Exe-файл будет в папке dist/

Временные файлы в build/ (можно удалить)

Альтернативы:

cx_Freeze: pip install cx_freeze

auto-py-to-exe: GUI для PyInstaller

Примечание: Для keyboard может потребоваться запуск от администратора.