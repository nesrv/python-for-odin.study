import tkinter as tk
from PIL import ImageGrab
import threading
import time
from datetime import datetime

class ScreenshotApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Screenshot App")
        self.root.geometry("200x100")
        
        self.running = False
        self.counter = 0
        
        # Кнопки
        self.start_btn = tk.Button(self.root, text="Старт", command=self.start, bg="green")
        self.start_btn.pack(pady=10)
        
        self.stop_btn = tk.Button(self.root, text="Стоп", command=self.stop, bg="red", state="disabled")
        self.stop_btn.pack(pady=5)
        
        # Статус
        self.status_label = tk.Label(self.root, text="Остановлено")
        self.status_label.pack(pady=5)
    
    def take_screenshot(self):
        """Делает скриншот и сохраняет в файл"""
        screenshot = ImageGrab.grab()
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"screenshot_{timestamp}_{self.counter:03d}.png"
        screenshot.save(filename)
        self.counter += 1
        
        # Обновляем статус в главном потоке
        self.root.after(0, lambda: self.status_label.config(text=f"Сохранено: {filename}"))
    
    def screenshot_loop(self):
        """Цикл создания скриншотов каждые 10 секунд"""
        while self.running:
            self.take_screenshot()
            time.sleep(10)
    
    def start(self):
        """Запуск создания скриншотов"""
        self.running = True
        self.counter = 0
        self.start_btn.config(state="disabled")
        self.stop_btn.config(state="normal")
        self.status_label.config(text="Запущено...")
        
        # Запускаем в отдельном потоке
        self.thread = threading.Thread(target=self.screenshot_loop, daemon=True)
        self.thread.start()
    
    def stop(self):
        """Остановка создания скриншотов"""
        self.running = False
        self.start_btn.config(state="normal")
        self.stop_btn.config(state="disabled")
        self.status_label.config(text="Остановлено")
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = ScreenshotApp()
    app.run()