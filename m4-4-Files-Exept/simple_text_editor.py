import tkinter as tk


# Создаем главное окно
root = tk.Tk()
root.title("Простой текстовый редактор")
root.geometry("600x400")


def open_file():
    import os
    print(f"Текущая папка: {os.getcwd()}")
    try:
        with open('txt.txt', 'r', encoding='utf-8') as f:
            content = f.read()
            text.delete(1.0, tk.END)
            text.insert(tk.END, content)
    except FileNotFoundError:
        print("Файл txt.txt не найден")

# Кнопка открыть файл
open_btn = tk.Button(root, text="Открыть файл", command=open_file)
open_btn.pack(pady=5)

# Кнопка сохранить
save_btn = tk.Button(root, text="Сохранить")
save_btn.pack(pady=5)

text = tk.Text(root, height=8, width=40)
text.pack(pady=5)

# Запускаем приложение
root.mainloop()