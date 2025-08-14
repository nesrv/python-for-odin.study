import tkinter as tk
from entry_module import study_entry
from radio_module import study_radio
from checkbox_module import study_checkbox

if __name__ == '__main__':
    # Главное окно
    root = tk.Tk()
    root.title("Изучение элементов GUI")
    root.geometry("400x300")
    
    # Кнопки
    tk.Button(root, text="Изучение полей ввода", command=study_entry, width=25).pack(pady=20)
    tk.Button(root, text="Изучение радиокнопок", command=study_radio, width=25).pack(pady=20)
    tk.Button(root, text="Изучение чекбоксов", command=study_checkbox, width=25).pack(pady=20)
    
    root.mainloop()