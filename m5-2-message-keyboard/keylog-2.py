import tkinter as tk
from tkinter import scrolledtext
import keyboard

def keylogger():
    root = tk.Tk()
    root.title("Кейлогер")
    root.geometry("400x300")
    
    text_box = scrolledtext.ScrolledText(root, width=50, height=15)
    text_box.pack(pady=10)
    
    def on_key_press(event):
        text_box.insert(tk.END, event.name)
        text_box.see(tk.END)
    
    keyboard.on_press(on_key_press)
    text_box.insert(tk.END, "Кейлогер запущен. Нажмите ESC для остановки.\n")
    
    root.mainloop()

if __name__ == "__main__":
    keylogger()