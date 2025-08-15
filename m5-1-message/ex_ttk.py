import tkinter as tk
from tkinter import ttk

# Создание главного окна
root = tk.Tk()
root.title("Демонстрация TTK виджетов")
root.geometry("500x600")  # Устанавливаем размер окна

# Создаем контейнер с вкладками (Notebook)
notebook = ttk.Notebook(root)
notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# === ВКЛАДКА 1: ОСНОВНЫЕ ЭЛЕМЕНТЫ ===
frame1 = ttk.Frame(notebook, padding="10")  # Создаем фрейм для первой вкладки
notebook.add(frame1, text="Основные")  # Добавляем вкладку в notebook

# Entry - однострочное поле ввода текста
# Методы: get() - получить текст, set() - установить, delete() - удалить
# Параметры: width - ширина, show="*" - скрыть символы (пароль)
ttk.Label(frame1, text="Entry (поле ввода):").grid(row=0, column=0, sticky=tk.W, pady=2)
ttk.Entry(frame1, width=20).grid(row=0, column=1, pady=2)

# Button - кнопка для выполнения действий
# Параметры: text - текст, command - функция при нажатии, state - состояние
# Состояния: 'normal' - активна, 'disabled' - неактивна
ttk.Label(frame1, text="Button (кнопка):").grid(row=1, column=0, sticky=tk.W, pady=2)
ttk.Button(frame1, text="Нажми меня").grid(row=1, column=1, pady=2)

# Checkbutton - чекбокс для вкл/выкл опций (можно отмечать несколько)
# Параметры: variable - переменная BooleanVar(), command - функция
# Методы: get() - получить состояние (True/False)
ttk.Label(frame1, text="Checkbutton (чекбокс):").grid(row=2, column=0, sticky=tk.W, pady=2)
ttk.Checkbutton(frame1, text="Отметь меня").grid(row=2, column=1, pady=2)

# Radiobutton - радиокнопки для выбора ОДНОГО варианта из группы
# Особенность: все кнопки с одинаковой variable связаны
# Параметры: variable - общая переменная, value - уникальное значение
ttk.Label(frame1, text="Radiobutton (радио):").grid(row=3, column=0, sticky=tk.W, pady=2)
radio_var = tk.StringVar(value="1")  # Общая переменная для всех радиокнопок
ttk.Radiobutton(frame1, text="Опция 1", variable=radio_var, value="1").grid(row=3, column=1, sticky=tk.W, pady=2)
ttk.Radiobutton(frame1, text="Опция 2", variable=radio_var, value="2").grid(row=4, column=1, sticky=tk.W, pady=2)

# === ВКЛАДКА 2: СПИСКИ И ВЫБОР ===
frame2 = ttk.Frame(notebook, padding="10")
notebook.add(frame2, text="Списки")

# Combobox - выпадающий список с возможностью ручного ввода
# Особенность: можно выбрать из списка ИЛИ ввести свое значение
# Методы: get() - получить, set() - установить, current() - индекс выбранного
# Параметры: values - список вариантов, state - 'readonly' запрещает ввод
ttk.Label(frame2, text="Combobox (выпадающий список):").grid(row=0, column=0, sticky=tk.W, pady=2)
combo = ttk.Combobox(frame2, values=["Питон", "Java", "C++", "JavaScript"])  # Список вариантов
combo.grid(row=0, column=1, pady=2)
combo.set("Питон")  # Устанавливаем значение по умолчанию

# Listbox - список для выбора одного или нескольких элементов (НЕ TTK!)
# Особенность: отображает все элементы одновременно, можно прокручивать
# Методы: insert() - добавить, delete() - удалить, curselection() - выбранные
# Параметры: selectmode - SINGLE/MULTIPLE, height - кол-во видимых строк
ttk.Label(frame2, text="Listbox (список):").grid(row=1, column=0, sticky=tk.W, pady=2)
listbox = tk.Listbox(frame2, height=4)  # Создаем список высотой 4 строки
# Заполняем список элементами
for item in ["Элемент 1", "Элемент 2", "Элемент 3", "Элемент 4"]:
    listbox.insert(tk.END, item)  # tk.END - в конец, можно указать индекс
listbox.grid(row=1, column=1, pady=2)

# === ВКЛАДКА 3: ПРОГРЕСС И ШКАЛЫ ===
frame3 = ttk.Frame(notebook, padding="10")
notebook.add(frame3, text="Прогресс")

# Progressbar - полоса прогресса для отображения хода выполнения операций
# Режимы: 'determinate' - с конкретным %, 'indeterminate' - бесконечная анимация
# Методы: start() - запуск, stop() - остановка, step() - увеличить на шаг
# Параметры: maximum - макс значение (по умолчанию 100)
ttk.Label(frame3, text="Progressbar (прогресс-бар):").grid(row=0, column=0, sticky=tk.W, pady=2)
progress = ttk.Progressbar(frame3, length=200, mode='determinate')  # Режим 'determinate' - с определенным значением
progress.grid(row=0, column=1, pady=2)
progress['value'] = 70  # Устанавливаем значение прогресса 70%

# Scale - ползунок для плавного выбора числового значения в диапазоне
# Ориентация: HORIZONTAL (горизонтально) или VERTICAL (вертикально)
# Методы: get() - получить значение, set() - установить
# Параметры: from_, to - диапазон, command - функция при изменении
ttk.Label(frame3, text="Scale (ползунок):").grid(row=1, column=0, sticky=tk.W, pady=2)
scale = ttk.Scale(frame3, from_=0, to=100, orient=tk.HORIZONTAL, length=200)  # Горизонтальный ползунок от 0 до 100
scale.grid(row=1, column=1, pady=2)
scale.set(50)  # Устанавливаем начальное значение 50

# Spinbox - поле ввода с кнопками вверх/вниз для изменения значения
# Особенность: можно вводить вручную ИЛИ использовать кнопки
# Методы: get() - получить, set() - установить
# Параметры: from_, to - диапазон, values - список значений, increment - шаг
ttk.Label(frame3, text="Spinbox (счетчик):").grid(row=2, column=0, sticky=tk.W, pady=2)
ttk.Spinbox(frame3, from_=0, to=100, width=10).grid(row=2, column=1, pady=2)  # Счетчик от 0 до 100

# === ВКЛАДКА 4: КОНТЕЙНЕРЫ ===
frame4 = ttk.Frame(notebook, padding="10")
notebook.add(frame4, text="Контейнеры")

# LabelFrame - рамка с заголовком для группировки элементов
ttk.Label(frame4, text="LabelFrame (рамка с заголовком):").grid(row=0, column=0, sticky=tk.W, pady=2)
labelframe = ttk.LabelFrame(frame4, text="Настройки", padding="10")  # Создаем рамку с заголовком
labelframe.grid(row=1, column=0, columnspan=2, pady=5, sticky=tk.W+tk.E)
# Добавляем элементы внутрь рамки
ttk.Checkbutton(labelframe, text="Опция 1").pack(anchor=tk.W)
ttk.Checkbutton(labelframe, text="Опция 2").pack(anchor=tk.W)

# Separator - горизонтальная или вертикальная линия-разделитель
ttk.Label(frame4, text="Separator (разделитель):").grid(row=2, column=0, sticky=tk.W, pady=2)
ttk.Separator(frame4, orient=tk.HORIZONTAL).grid(row=3, column=0, columnspan=2, sticky=tk.W+tk.E, pady=5)  # Горизонтальная линия

# Treeview - мощный виджет для отображения иерархических данных и таблиц
# Возможности: дерево папок, таблица с колонками, сортировка
# Методы: insert() - добавить, delete() - удалить, selection() - выбранные
# Параметры: columns - колонки, show - что показывать ('tree', 'headings')
ttk.Label(frame4, text="Treeview (дерево):").grid(row=4, column=0, sticky=tk.W, pady=2)
tree = ttk.Treeview(frame4, height=4)  # Создаем дерево высотой 4 строки
tree.grid(row=5, column=0, columnspan=2, pady=2)
# Добавляем элементы: insert(родитель, позиция, text=текст)
tree.insert('', 'end', text='Корень')  # '' - корень, 'end' - в конец
child = tree.insert('', 'end', text='Родитель')  # Сохраняем ID для дочерних
tree.insert(child, 'end', text='Дочерний элемент')  # child - родитель

# Запуск главного цикла приложения
root.mainloop()