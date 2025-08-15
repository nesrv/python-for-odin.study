# Шпаргалка по ttk (Themed Tkinter)

`ttk` (Themed Tkinter) - это расширение стандартного Tkinter, предоставляющее более современные и стильные виджеты с поддержкой тем оформления.

## Основные виджеты ttk

### Импорт модуля
```python
from tkinter import ttk
# или
from tkinter.ttk import *
```

### 1. Основные виджеты

**Button** - стилизованная кнопка:
```python
ttk.Button(parent, text="Кнопка", command=callback)
```

**Label** - метка с современным оформлением:
```python
ttk.Label(parent, text="Текст", background='white')
```

**Entry** - поле ввода:
```python
ttk.Entry(parent, width=20, show="*")
```

### 2. Виджеты выбора

**Combobox** - выпадающий список:
```python
ttk.Combobox(parent, values=["Вариант 1", "Вариант 2"])
```

**Checkbutton** - флажок:
```python
ttk.Checkbutton(parent, text="Согласен", variable=BooleanVar())
```

**Radiobutton** - переключатель:
```python
ttk.Radiobutton(parent, text="Вариант", variable=var, value=1)
```

### 3. Специальные виджеты

**Progressbar** - индикатор прогресса:
```python
ttk.Progressbar(parent, orient="horizontal", length=200, mode="determinate")
```

**Notebook** - панель с вкладками:
```python
notebook = ttk.Notebook(parent)
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Вкладка 1")
```

**Treeview** - табличное представление с возможностью сортировки:
```python
tree = ttk.Treeview(parent, columns=("Name", "Age"))
tree.heading("#0", text="ID")
tree.heading("Name", text="Имя")
tree.heading("Age", text="Возраст")
```

**Separator** - разделитель:
```python
ttk.Separator(parent, orient="horizontal")
```

## Стилизация ttk

### Настройка стилей
```python
style = ttk.Style()
```

### Доступные темы
```python
print(style.theme_names())  # Показать доступные темы
style.theme_use("clam")    # Установить тему ('clam', 'alt', 'default', 'classic' и др.)
```

### Настройка конкретного стиля
```python
style.configure("TButton", padding=6, relief="flat", background="#ccc")
style.map("TButton", background=[("active", "#ddd")])
```

### Имена стандартных стилей:
- `TButton` - для кнопок
- `TLabel` - для меток
- `TEntry` - для полей ввода
- `TCheckbutton` - для флажков
- `TRadiobutton` - для переключателей
- `TCombobox` - для выпадающих списков
- `TProgressbar` - для индикаторов прогресса
- `TNotebook` - для панелей с вкладками
- `TFrame` - для фреймов

## Пример использования ttk

```python
from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("Пример ttk")

style = ttk.Style()
style.theme_use("clam")

frame = ttk.Frame(root, padding="10")
frame.pack(fill=BOTH, expand=True)

ttk.Label(frame, text="Имя пользователя:").grid(column=0, row=0, sticky=W)
name_entry = ttk.Entry(frame, width=15)
name_entry.grid(column=1, row=0)

ttk.Label(frame, text="Пароль:").grid(column=0, row=1, sticky=W)
pass_entry = ttk.Entry(frame, width=15, show="*")
pass_entry.grid(column=1, row=1)

ttk.Checkbutton(frame, text="Запомнить меня").grid(columnspan=2, row=2, pady=5)

ttk.Button(frame, text="Войти", command=root.quit).grid(columnspan=2, row=3)

root.mainloop()
```

## Преимущества ttk перед стандартными виджетами:
1. Более современный внешний вид
2. Поддержка тем оформления
3. Кроссплатформенное единообразие
4. Дополнительные виджеты (Combobox, Notebook, Treeview и др.)
5. Лучшая интеграция с системным оформлением

## Ограничения:
1. Некоторые параметры стандартных виджетов недоступны в ttk
2. Меньше возможностей для кастомизации
3. Некоторые виджеты (как Text, Canvas) доступны только в стандартном Tkinter