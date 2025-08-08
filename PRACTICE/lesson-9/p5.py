import tkinter as tk

root = tk.Tk()
root.title("Простой текстовый редактор")
root.geometry("800x600")

text = tk.Text(root, height=8, width=40)
text.pack(pady=50)

text_2 = tk.Text(root, height=1, width=40)
text_2.pack(padx=350)


def open_file():
    f = open("fruit.txt", encoding='utf-8')
    s = f.read()
    text.insert(tk.END, s)
          

def count_words():
    c = text.get("1.0", tk.END)
    c = c.split()
    text_2.insert(tk.END, len(c))
   

open_btn = tk.Button(root, text="Открыть файл", command=open_file)
open_btn.pack(pady=5)

btn_2 = tk.Button(root, text="Посчитать слова", command=count_words)
btn_2.pack(pady=50)



root.mainloop()