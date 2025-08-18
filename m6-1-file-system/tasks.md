Вот 5 практических заданий по работе с файловой системой в Python с использованием модуля `os` с решениями:

---

### **Задание 1. Создание и удаление временной папки**
**Условие:**  
Создайте временную папку `temp_dir` в текущей директории, проверьте её существование, а затем удалите.

**Решение:**
```python
import os

# Создаем папку
os.mkdir("temp_dir")

# Проверяем существование
if os.path.exists("temp_dir"):
    print("Папка создана успешно!")
else:
    print("Ошибка при создании папки.")

# Удаляем папку
os.rmdir("temp_dir")
print("Папка удалена.")
```

---

### **Задание 2. Переименование файлов в директории**
**Условие:**  
В текущей директории найдите все файлы с расширением `.txt` и переименуйте их, добавив префикс `new_`.

**Решение:**
```python
import os

for filename in os.listdir("."):
    if filename.endswith(".txt"):
        new_name = "new_" + filename
        os.rename(filename, new_name)
        print(f"Файл {filename} переименован в {new_name}")
```

---

### **Задание 3. Рекурсивный подсчёт файлов в директории**
**Условие:**  
Напишите скрипт, который рекурсивно обходит указанную папку и выводит количество файлов в ней (и во всех подпапках).

**Решение:**
```python
import os

def count_files(directory):
    total = 0
    for root, dirs, files in os.walk(directory):
        total += len(files)
    return total

path = input("Введите путь к папке: ")
print(f"Всего файлов: {count_files(path)}")
```

---

### **Задание 4. Копирование всех изображений в отдельную папку**
**Условие:**  
Создайте папку `images`, затем скопируйте в неё все файлы с расширениями `.jpg`, `.png` и `.gif` из текущей директории.

**Решение:**
```python
import os
import shutil

# Создаем папку images, если её нет
if not os.path.exists("images"):
    os.mkdir("images")

# Копируем изображения
for filename in os.listdir("."):
    if filename.lower().endswith((".jpg", ".png", ".gif")):
        shutil.copy(filename, os.path.join("images", filename))
        print(f"Скопирован: {filename}")
```

---

### **Задание 5. Поиск самого большого файла в директории**
**Условие:**  
Найдите файл с максимальным размером в указанной директории (и её подпапках) и выведите его имя и размер в мегабайтах.

**Решение:**
```python
import os

def find_largest_file(directory):
    max_size = 0
    largest_file = ""

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            size = os.path.getsize(file_path)
            if size > max_size:
                max_size = size
                largest_file = file_path

    return largest_file, max_size / (1024 * 1024)  # Размер в МБ

path = input("Введите путь к папке: ")
file, size = find_largest_file(path)
print(f"Самый большой файл: {file}, размер: {size:.2f} МБ")
```

---

Эти задания охватывают основные операции с файловой системой: создание, удаление, переименование, рекурсивный обход, копирование и анализ файлов. 🚀