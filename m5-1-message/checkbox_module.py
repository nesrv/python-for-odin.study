import tkinter as tk
from tkinter import messagebox

def study_checkbox():
    """Изучение чекбоксов"""
    window = tk.Toplevel()
    window.title("Чекбоксы")
    window.geometry("300x200")
    
    var1 = tk.BooleanVar()
    var2 = tk.BooleanVar()
    var3 = tk.BooleanVar()
    
    tk.Label(window, text="Выберите навыки:").pack(pady=5)
    tk.Checkbutton(window, text="HTML", variable=var1).pack()
    tk.Checkbutton(window, text="CSS", variable=var2).pack()
    tk.Checkbutton(window, text="JavaScript", variable=var3).pack()
    
    def show_selected():
        skills = []
        if var1.get(): skills.append("HTML")
        if var2.get(): skills.append("CSS")
        if var3.get(): skills.append("JavaScript")
        messagebox.showinfo("Результат", f"Выбрано: {', '.join(skills) if skills else 'Ничего'}")
    
    tk.Button(window, text="Показать", command=show_selected).pack(pady=10)