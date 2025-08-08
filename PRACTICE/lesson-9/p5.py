import tkinter as tk

# Создаем главное окно приложения
root = tk.Tk()
root.title("Простой текстовый редактор")
root.geometry("800x600")  # Устанавливаем размер окна

# Основное текстовое поле для отображения содержимого файла
text = tk.Text(root, height=8, width=40)
text.pack(pady=50)

# Поле для вывода результата (количество слов)
text_2 = tk.Text(root, height=1, width=40)
text_2.pack(padx=350)


def open_file():
    """Открывает файл fruit.txt и выводит его содержимое в текстовое поле"""
    f = open("fruit.txt", encoding='utf-8')  # Открываем файл с кодировкой UTF-8
    s = f.read()  # Читаем все содержимое файла
    text.insert(tk.END, s)  # Вставляем текст в конец текстового поля
    f.close()  # Закрываем файл
          

def count_words():
    """Подсчитывает количество слов в текстовом поле"""
    c = text.get("1.0", tk.END)  # Получаем весь текст из поля
    c = c.split()  # Разбиваем текст на слова (по пробелам)
    text_2.delete("1.0", tk.END)  # Очищаем поле результата
    text_2.insert(tk.END, len(c))  # Выводим количество слов
   
# Кнопка для открытия файла
open_btn = tk.Button(root, text="Открыть файл", command=open_file)
open_btn.pack(pady=5)

# Кнопка для подсчета слов
btn_2 = tk.Button(root, text="Посчитать слова", command=count_words)
btn_2.pack(pady=50)

# Запуск главного цикла приложения
root.mainloop()