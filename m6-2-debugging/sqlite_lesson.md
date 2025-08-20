# Урок: Работа с базами данных SQLite и SQLAlchemy для новичков

## Что такое база данных?

**База данных** - это место для хранения информации в виде таблиц (как Excel, но мощнее).

**SQLite** - простая база данных в одном файле  
**SQLAlchemy** - инструмент для удобной работы с базами данных

## Часть 1: Чистый SQLite

### Создание базы и таблицы

```python
import sqlite3

# Подключаемся к базе (файл создастся автоматически)
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Создаем таблицу студентов
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        grade REAL
    )
''')

conn.commit()  # Сохраняем изменения
print("Таблица создана!")
```

### Добавление данных

```python
# Добавляем одного студента
cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", 
               ("Иван Петров", 20, 4.5))

# Добавляем несколько студентов
students_data = [
    ("Мария Сидорова", 19, 5.0),
    ("Петр Иванов", 21, 3.8),
    ("Анна Козлова", 18, 4.2)
]

cursor.executemany("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", 
                   students_data)

conn.commit()
print("Студенты добавлены!")
```

### Чтение данных

```python
# Получаем всех студентов
cursor.execute("SELECT * FROM students")
all_students = cursor.fetchall()

print("Все студенты:")
for student in all_students:
    print(f"ID: {student[0]}, Имя: {student[1]}, Возраст: {student[2]}, Оценка: {student[3]}")

# Поиск по условию
cursor.execute("SELECT * FROM students WHERE grade >= ?", (4.0,))
good_students = cursor.fetchall()

print("\nОтличники:")
for student in good_students:
    print(f"{student[1]} - {student[3]}")
```

### Обновление и удаление

```python
# Обновляем оценку студента
cursor.execute("UPDATE students SET grade = ? WHERE name = ?", (4.8, "Иван Петров"))

# Удаляем студента
cursor.execute("DELETE FROM students WHERE age < ?", (19,))

conn.commit()
print("Данные обновлены!")

# Закрываем соединение
conn.close()
```

## Часть 2: SQLAlchemy (упрощенный подход)

### Установка и подключение

```bash
pip install sqlalchemy
```

```python
from sqlalchemy import create_engine, text
import pandas as pd

# Создаем подключение к базе
engine = create_engine('sqlite:///school.db')
```

### Создание таблицы через SQL

```python
# Создаем таблицу учителей
with engine.connect() as conn:
    conn.execute(text('''
        CREATE TABLE IF NOT EXISTS teachers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            subject TEXT,
            salary REAL
        )
    '''))
    conn.commit()

print("Таблица учителей создана!")
```

### Работа с данными

```python
# Добавляем учителей
teachers_data = [
    {"name": "Елена Васильева", "subject": "Математика", "salary": 45000},
    {"name": "Сергей Петров", "subject": "Физика", "salary": 48000},
    {"name": "Ольга Смирнова", "subject": "Химия", "salary": 46000}
]

with engine.connect() as conn:
    for teacher in teachers_data:
        conn.execute(text(
            "INSERT INTO teachers (name, subject, salary) VALUES (:name, :subject, :salary)"
        ), teacher)
    conn.commit()

print("Учителя добавлены!")
```

### Чтение данных с pandas

```python
# Читаем данные в DataFrame (как таблица Excel)
df = pd.read_sql("SELECT * FROM teachers", engine)
print("Все учителя:")
print(df)

# Фильтрация данных
high_salary = pd.read_sql("SELECT * FROM teachers WHERE salary > 46000", engine)
print("\nУчителя с высокой зарплатой:")
print(high_salary)
```

## Практический пример: Система учета книг

```python
import sqlite3
import pandas as pd
from datetime import datetime

# Создаем базу данных библиотеки
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

# Создаем таблицу книг
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        year INTEGER,
        available BOOLEAN DEFAULT 1,
        added_date TEXT
    )
''')

def add_book(title, author, year):
    """Добавляем книгу в библиотеку"""
    cursor.execute(
        "INSERT INTO books (title, author, year, added_date) VALUES (?, ?, ?, ?)",
        (title, author, year, datetime.now().strftime("%Y-%m-%d"))
    )
    conn.commit()
    print(f"Книга '{title}' добавлена!")

def find_books(search_term):
    """Ищем книги по названию или автору"""
    cursor.execute(
        "SELECT * FROM books WHERE title LIKE ? OR author LIKE ?",
        (f"%{search_term}%", f"%{search_term}%")
    )
    return cursor.fetchall()

def borrow_book(book_id):
    """Выдаем книгу (делаем недоступной)"""
    cursor.execute("UPDATE books SET available = 0 WHERE id = ?", (book_id,))
    conn.commit()
    print("Книга выдана!")

def return_book(book_id):
    """Возвращаем книгу"""
    cursor.execute("UPDATE books SET available = 1 WHERE id = ?", (book_id,))
    conn.commit()
    print("Книга возвращена!")

def show_available_books():
    """Показываем доступные книги"""
    cursor.execute("SELECT * FROM books WHERE available = 1")
    books = cursor.fetchall()
    
    print("Доступные книги:")
    for book in books:
        print(f"{book[0]}. {book[1]} - {book[2]} ({book[3]})")

# Тестируем систему
add_book("Война и мир", "Лев Толстой", 1869)
add_book("Преступление и наказание", "Федор Достоевский", 1866)
add_book("Мастер и Маргарита", "Михаил Булгаков", 1967)

show_available_books()

# Выдаем книгу
borrow_book(1)
show_available_books()

# Возвращаем книгу
return_book(1)
show_available_books()

conn.close()
```

## Простой веб-интерфейс с Flask

```python
from flask import Flask, render_template_string, request, redirect
import sqlite3

app = Flask(__name__)

def get_db():
    return sqlite3.connect('library.db')

@app.route('/')
def index():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books WHERE available = 1")
    books = cursor.fetchall()
    conn.close()
    
    html = '''
    <h1>Библиотека</h1>
    <h2>Добавить книгу</h2>
    <form method="POST" action="/add">
        <input name="title" placeholder="Название" required><br><br>
        <input name="author" placeholder="Автор" required><br><br>
        <input name="year" type="number" placeholder="Год" required><br><br>
        <button type="submit">Добавить</button>
    </form>
    
    <h2>Доступные книги</h2>
    <ul>
    {% for book in books %}
        <li>{{ book[1] }} - {{ book[2] }} ({{ book[3] }}) 
            <a href="/borrow/{{ book[0] }}">Взять</a>
        </li>
    {% endfor %}
    </ul>
    '''
    
    return render_template_string(html, books=books)

@app.route('/add', methods=['POST'])
def add_book():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO books (title, author, year, added_date) VALUES (?, ?, ?, ?)",
        (request.form['title'], request.form['author'], 
         request.form['year'], datetime.now().strftime("%Y-%m-%d"))
    )
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/borrow/<int:book_id>')
def borrow_book(book_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE books SET available = 0 WHERE id = ?", (book_id,))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
```

## Основные команды SQL

```sql
-- Создание таблицы
CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, email TEXT);

-- Добавление данных
INSERT INTO users (name, email) VALUES ('Иван', 'ivan@mail.ru');

-- Чтение данных
SELECT * FROM users;                    -- Все записи
SELECT name FROM users WHERE id = 1;   -- По условию

-- Обновление
UPDATE users SET email = 'new@mail.ru' WHERE id = 1;

-- Удаление
DELETE FROM users WHERE id = 1;
```

## Полезные советы

1. **Всегда используйте параметры** вместо строк:
   ```python
   # ✅ Правильно
   cursor.execute("SELECT * FROM users WHERE name = ?", (name,))
   
   # ❌ Опасно (SQL-инъекции)
   cursor.execute(f"SELECT * FROM users WHERE name = '{name}'")
   ```

2. **Не забывайте commit()**:
   ```python
   cursor.execute("INSERT INTO ...")
   conn.commit()  # Без этого данные не сохранятся!
   ```

3. **Закрывайте соединения**:
   ```python
   conn.close()  # Освобождаем ресурсы
   ```

4. **Используйте pandas для анализа**:
   ```python
   df = pd.read_sql("SELECT * FROM table", conn)
   print(df.describe())  # Статистика
   ```

## Заключение

**SQLite подходит для:**
- Небольших проектов
- Локальных приложений
- Обучения и прототипов

**SQLAlchemy упрощает:**
- Работу с разными базами данных
- Сложные запросы
- Интеграцию с pandas

**Начните с простого:**
1. Создайте таблицу
2. Добавьте данные
3. Научитесь читать и фильтровать
4. Постепенно изучайте сложные запросы