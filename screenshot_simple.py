# Импорт необходимых библиотек
import tkinter as tk          # GUI интерфейс
from PIL import ImageGrab     # Для создания скриншотов
import threading              # Многопоточность (чтобы GUI не зависал)
import time                   # Для задержки между скриншотами
from datetime import datetime # Для создания уникальных имен файлов
import zipfile               # Для создания архивов
import glob                  # Для поиска файлов по маске
import smtplib               # Для отправки email
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os                    # Для работы с файлами

# Создание главного окна приложения
root = tk.Tk()
root.title("Screenshot App")  # Заголовок окна
root.geometry("300x200")      # Увеличиваем размер окна для новых элементов

# Глобальные переменные для управления состоянием
running = False  # Флаг: работает ли процесс создания скриншотов
counter = 0      # Счетчик сделанных скриншотов

def take_screenshot():
    """Функция для создания одного скриншота и сохранения в файл"""
    global counter  # Используем глобальную переменную
    
    # Создаем скриншот всего экрана
    screenshot = ImageGrab.grab()
    
    # Создаем уникальное имя файла с текущей датой и временем
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  # Формат: 20241201_143052
    filename = f"screenshot_{timestamp}_{counter:03d}.png"  # :03d - трехзначный номер (001, 002, ...)
    
    # Сохраняем скриншот в файл
    screenshot.save(filename)
    counter += 1  # Увеличиваем счетчик
    
    # Обновляем статус на экране (показываем количество сделанных скриншотов)
    status_label.config(text=f"Сохранено: {counter}")

def screenshot_loop():
    """Основной цикл - делает скриншоты каждые 10 секунд"""
    while running:  # Пока флаг running = True
        take_screenshot()  # Делаем скриншот
        time.sleep(10)     # Ждем 10 секунд до следующего

def start():
    """Функция запуска процесса создания скриншотов"""
    global running, counter
    
    # Устанавливаем флаги и сбрасываем счетчик
    running = True
    counter = 0
    
    # Обновляем состояние кнопок (делаем Старт неактивной, Стоп активной)
    start_btn.config(state="disabled")
    stop_btn.config(state="normal")
    status_label.config(text="Запущено...")
    
    # Запускаем цикл скриншотов в отдельном потоке
    # daemon=True - поток завершится при закрытии программы
    threading.Thread(target=screenshot_loop, daemon=True).start()

def stop():
    """Функция остановки процесса создания скриншотов"""
    global running
    
    # Останавливаем цикл
    running = False
    
    # Обновляем состояние кнопок (делаем Старт активной, Стоп неактивной)
    start_btn.config(state="normal")
    stop_btn.config(state="disabled")
    status_label.config(text="Остановлено")

def send_email():
    """Функция для отправки последних 5 скриншотов на email"""
    email = email_entry.get()  # Получаем email из поля ввода
    
    if not email:
        status_label.config(text="Введите email!")
        return
    
    try:
        # Находим последние 5 файлов скриншотов
        files = glob.glob("screenshot_*.png")
        files.sort(key=os.path.getmtime, reverse=True)  # Сортируем по времени создания
        latest_files = files[:5]  # Берем последние 5
        
        if not latest_files:
            status_label.config(text="Нет файлов для отправки")
            return
        
        # Создаем архив с последними скриншотами
        zip_filename = f"screenshots_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
        with zipfile.ZipFile(zip_filename, 'w') as zipf:
            for file in latest_files:
                zipf.write(file)
        
        # Отправляем архив на email (упрощенная версия - нужны настройки SMTP)
        status_label.config(text=f"Архив {zip_filename} создан")
        
    except Exception as e:
        status_label.config(text=f"Ошибка: {str(e)[:20]}...")

# === СОЗДАНИЕ GUI ЭЛЕМЕНТОВ ===

# Кнопка "Старт" - запускает процесс создания скриншотов
start_btn = tk.Button(root, text="Старт", command=start, bg="green")
start_btn.pack(pady=5)

# Кнопка "Стоп" - останавливает процесс (изначально неактивна)
stop_btn = tk.Button(root, text="Стоп", command=stop, bg="red", state="disabled")
stop_btn.pack(pady=5)

# Поле для ввода email адреса
tk.Label(root, text="Email:").pack()
email_entry = tk.Entry(root, width=30)
email_entry.pack(pady=5)

# Кнопка для отправки архива на email
send_btn = tk.Button(root, text="Отправить на почту", command=send_email, bg="blue", fg="white")
send_btn.pack(pady=5)

# Метка для отображения текущего статуса программы
status_label = tk.Label(root, text="Остановлено")
status_label.pack(pady=5)

# Запуск главного цикла приложения (обработка событий GUI)
root.mainloop()