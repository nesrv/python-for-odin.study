# Справка по GUI элементам в Tkinter

## Основные элементы (виджеты)

### 1. Основные виджеты

**Label** - метка для отображения текста или изображения:
```python
Label(parent, text="Текст", font=("Arial", 12), fg="blue", bg="white")
```

**Button** - кнопка:
```python
Button(parent, text="Нажми меня", command=callback_function)
```

**Entry** - однострочное поле ввода:
```python
Entry(parent, width=20, show="*")  # show="*" для скрытия ввода
```

**Text** - многострочное текстовое поле:
```python
Text(parent, width=40, height=10, wrap="word")
```

### 2. Виджеты выбора

**Checkbutton** - флажок:
```python
Checkbutton(parent, text="Согласен", variable=BooleanVar())
```

**Radiobutton** - переключатель:
```python
Radiobutton(parent, text="Вариант 1", variable=var, value=1)
```

**Listbox** - список для выбора:
```python
Listbox(parent, height=4, selectmode="multiple")
```

**Combobox** (из ttk) - выпадающий список:
```python
from tkinter.ttk import Combobox
Combobox(parent, values=["Вариант 1", "Вариант 2"])
```

### 3. Контейнеры

**Frame** - контейнер для группировки виджетов:
```python
Frame(parent, padx=5, pady=5, relief="groove")
```

**LabelFrame** - рамка с заголовком:
```python
LabelFrame(parent, text="Группа", padx=10, pady=10)
```

**PanedWindow** - разделяемая панель:
```python
PanedWindow(parent, orient="horizontal")
```

**Notebook** (из ttk) - вкладки:
```python
from tkinter.ttk import Notebook
Notebook(parent)
```

### 4. Специальные виджеты

**Scale** - шкала (ползунок):
```python
Scale(parent, from_=0, to=100, orient="horizontal")
```

**Scrollbar** - полоса прокрутки:
```python
Scrollbar(parent, orient="vertical")
```

**Spinbox** - поле с кнопками вверх/вниз:
```python
Spinbox(parent, from_=1, to=10)
```

**Progressbar** (из ttk) - индикатор прогресса:
```python
from tkinter.ttk import Progressbar
Progressbar(parent, mode="determinate", maximum=100, value=50)
```

**Treeview** (из ttk) - табличное представление:
```python
from tkinter.ttk import Treeview
Treeview(parent, columns=("name", "age"), show="headings")
```

## Общие параметры виджетов

- `text` - текст на виджете
- `fg` / `foreground` - цвет текста
- `bg` / `background` - цвет фона
- `font` - шрифт (например, `("Arial", 12)`)
- `width`, `height` - размеры
- `padx`, `pady` - отступы
- `relief` - стиль рамки ("flat", "raised", "sunken", "ridge", "groove", "solid")
- `command` - функция, вызываемая при действии
- `state` - состояние ("normal", "disabled", "readonly")

## Размещение виджетов

**pack()** - автоматическое размещение:
```python
widget.pack(side="left", fill="both", expand=True, padx=5, pady=5)
```

**grid()** - размещение по сетке:
```python
widget.grid(row=0, column=0, rowspan=2, columnspan=2, sticky="nsew")
```

**place()** - точное позиционирование:
```python
widget.place(x=10, y=20, width=100, height=50)
```

## Пример простого окна

```python
from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("Пример GUI")

frame = LabelFrame(root, text="Панель")
frame.pack(padx=10, pady=10)

Label(frame, text="Имя:").grid(row=0, column=0)
Entry(frame).grid(row=0, column=1)

Button(frame, text="OK", command=root.quit).grid(row=1, columnspan=2)

root.mainloop()
```
