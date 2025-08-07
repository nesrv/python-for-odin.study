Основные элементы (виджеты) библиотеки `tkinter` в Python:

### 1. **Основные виджеты**
- **`Label`** – метка для отображения текста или изображения.
  ```python
  label = tk.Label(root, text="Привет, мир!")
  ```

- **`Button`** – кнопка, выполняющая действие при нажатии.
  ```python
  button = tk.Button(root, text="Нажми меня", command=callback)
  ```

- **`Entry`** – однострочное поле ввода.
  ```python
  entry = tk.Entry(root)
  ```

- **`Text`** – многострочное текстовое поле.
  ```python
  text = tk.Text(root, height=5, width=30)
  ```

- **`Checkbutton`** – флажок (чекбокс).
  ```python
  check = tk.Checkbutton(root, text="Согласен", variable=var)
  ```

- **`Radiobutton`** – переключатель (радиокнопка).
  ```python
  radio1 = tk.Radiobutton(root, text="Вариант 1", variable=var, value=1)
  ```

- **`Scale`** – шкала (слайдер).
  ```python
  scale = tk.Scale(root, from_=0, to=100, orient="horizontal")
  ```

- **`Listbox`** – список для выбора одного или нескольких элементов.
  ```python
  listbox = tk.Listbox(root)
  ```

- **`Spinbox`** – поле с выбором из предустановленных значений.
  ```python
  spinbox = tk.Spinbox(root, from_=1, to=10)
  ```

- **`Combobox`** (из `ttk`) – выпадающий список.
  ```python
  from tkinter import ttk
  combo = ttk.Combobox(root, values=["Вариант 1", "Вариант 2"])
  ```

### 2. **Контейнеры (для группировки виджетов)**
- **`Frame`** – контейнер для группировки других виджетов.
  ```python
  frame = tk.Frame(root)
  ```

- **`LabelFrame`** – рамка с заголовком.
  ```python
  labelframe = tk.LabelFrame(root, text="Группа")
  ```

- **`PanedWindow`** – контейнер с изменяемыми разделами.
  ```python
  paned = tk.PanedWindow(root, orient="vertical")
  ```

- **`Notebook`** (из `ttk`) – вкладки.
  ```python
  notebook = ttk.Notebook(root)
  ```

### 3. **Диалоговые окна**
- **`messagebox`** – окна сообщений (информация, ошибка, вопрос).
  ```python
  from tkinter import messagebox
  messagebox.showinfo("Заголовок", "Сообщение")
  ```

- **`filedialog`** – диалог открытия/сохранения файлов.
  ```python
  from tkinter import filedialog
  filedialog.askopenfilename()
  ```

- **`colorchooser`** – выбор цвета.
  ```python
  from tkinter import colorchooser
  colorchooser.askcolor()
  ```

### 4. **Меню**
- **`Menu`** – главное меню окна.
  ```python
  menubar = tk.Menu(root)
  root.config(menu=menubar)
  ```

- **`Popup Menu`** (контекстное меню) – вызывается правой кнопкой мыши.
  ```python
  popup = tk.Menu(root, tearoff=0)
  ```

### 5. **Дополнительные виджеты (ttk)**
- **`Progressbar`** – индикатор выполнения.
  ```python
  progress = ttk.Progressbar(root, mode="determinate")
  ```

- **`Treeview`** – таблица или древовидный список.
  ```python
  tree = ttk.Treeview(root, columns=("Name", "Age"))
  ```

- **`Separator`** – разделительная линия.
  ```python
  separator = ttk.Separator(root, orient="horizontal")
  ```

### 6. **Размещение виджетов (геометрия)**
- **`pack()`** – автоматическое размещение.
  ```python
  label.pack()
  ```

- **`grid()`** – размещение в сетке (строка/столбец).
  ```python
  button.grid(row=0, column=0)
  ```

- **`place()`** – точное позиционирование (x/y).
  ```python
  entry.place(x=10, y=20)
  ```

### Пример простого окна:
```python
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Пример Tkinter")

label = tk.Label(root, text="Привет, Tkinter!")
label.pack()

button = tk.Button(root, text="Нажми", command=lambda: print("Кнопка нажата!"))
button.pack()

root.mainloop()
```

Это основные элементы `tkinter`. Библиотека также поддерживает стилизацию (`ttk`), привязку событий (`bind`) и многое другое.