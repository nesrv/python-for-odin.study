import tkinter as tk

# Словари для переключения раскладки
en_to_ru = {
    'q': 'й', 'w': 'ц', 'e': 'у', 'r': 'к', 't': 'е', 'y': 'н', 'u': 'г', 'i': 'ш', 'o': 'щ', 'p': 'з',
    '[': 'х', ']': 'ъ', 'a': 'ф', 's': 'ы', 'd': 'в', 'f': 'а', 'g': 'п', 'h': 'р', 'j': 'о', 'k': 'л',
    'l': 'д', ';': 'ж', "'": 'э', 'z': 'я', 'x': 'ч', 'c': 'с', 'v': 'м', 'b': 'и', 'n': 'т', 'm': 'ь',
    ',': 'б', '.': 'ю', '/': '.', '`': 'ё'
}

ru_to_en = {v: k for k, v in en_to_ru.items()}

def switch_layout():
    """Переключает раскладку текста"""
    text = entry.get()
    result = ""
    
    for char in text:
        if char.lower() in en_to_ru:
            # Английский -> Русский
            new_char = en_to_ru[char.lower()]
            result += new_char.upper() if char.isupper() else new_char
        elif char.lower() in ru_to_en:
            # Русский -> Английский
            new_char = ru_to_en[char.lower()]
            result += new_char.upper() if char.isupper() else new_char
        else:
            result += char
    
    entry.delete(0, tk.END)
    entry.insert(0, result)

# Создаем окно
root = tk.Tk()
root.title("Punto Switcher")
root.geometry("400x150")

# Поле ввода
entry = tk.Entry(root, width=50, font=("Arial", 12))
entry.pack(pady=20)

# Кнопка переключения
switch_btn = tk.Button(root, text="Переключить раскладку", command=switch_layout, font=("Arial", 10))
switch_btn.pack(pady=10)

# Привязка горячей клавиши Ctrl+Space
root.bind('<Control-space>', lambda e: switch_layout())

# Инструкция
label = tk.Label(root, text="Введите текст и нажмите кнопку или Ctrl+Space", font=("Arial", 9))
label.pack(pady=5)

root.mainloop()