# 10 простых задач для новичков по базе данных books.db

from sqlalchemy import *

engine = create_engine('sqlite:///books.db')
metadata = MetaData()

# Загружаем таблицы
authors = Table('authors', metadata, autoload_with=engine)
books = Table('books', metadata, autoload_with=engine)

# ЗАДАЧА 1: Показать всех авторов
print("=== ЗАДАЧА 1: Все авторы ===")
with engine.connect() as conn:
    result = conn.execute(select(authors))
    for row in result:
        print(f"{row.name}")

# ЗАДАЧА 2: Показать все книги
print("\n=== ЗАДАЧА 2: Все книги ===")
with engine.connect() as conn:
    result = conn.execute(select(books.c.title))
    for row in result:
        print(f"{row.title}")

# ЗАДАЧА 3: Найти автора по имени "Антон Чехов"
print("\n=== ЗАДАЧА 3: Найти Антона Чехова ===")
with engine.connect() as conn:
    result = conn.execute(
        select(authors).where(authors.c.name == 'Антон Чехов')
    )
    for row in result:
        print(f"{row.name} ({row.birth_year})")

# ЗАДАЧА 4: Найти книгу "Война и мир"
print("\n=== ЗАДАЧА 4: Найти 'Война и мир' ===")
with engine.connect() as conn:
    result = conn.execute(
        select(books).where(books.c.title == 'Война и мир')
    )
    for row in result:
        print(f"{row.title} ({row.year})")

# ЗАДАЧА 5: Показать только названия и годы книг
print("\n=== ЗАДАЧА 5: Названия и годы книг ===")
with engine.connect() as conn:
    result = conn.execute(select(books.c.title, books.c.year))
    for row in result:
        print(f"{row.title} - {row.year}")

# ЗАДАЧА 6: Найти книги 1869 года
print("\n=== ЗАДАЧА 6: Книги 1869 года ===")
with engine.connect() as conn:
    result = conn.execute(
        select(books.c.title).where(books.c.year == 1869)
    )
    for row in result:
        print(f"{row.title}")

# ЗАДАЧА 7: Показать авторов и их годы рождения
print("\n=== ЗАДАЧА 7: Авторы и годы рождения ===")
with engine.connect() as conn:
    result = conn.execute(select(authors.c.name, authors.c.birth_year))
    for row in result:
        print(f"{row.name} - {row.birth_year}")

# ЗАДАЧА 8: Найти книги старше 1850 года
print("\n=== ЗАДАЧА 8: Книги старше 1850 года ===")
with engine.connect() as conn:
    result = conn.execute(
        select(books.c.title, books.c.year)
        .where(books.c.year < 1850)
    )
    for row in result:
        print(f"{row.title} ({row.year})")

# ЗАДАЧА 9: Посчитать общее количество книг
print("\n=== ЗАДАЧА 9: Общее количество книг ===")
with engine.connect() as conn:
    result = conn.execute(select(func.count(books.c.id)))
    count = result.scalar()
    print(f"Всего книг: {count}")

# ЗАДАЧА 10: Посчитать общее количество авторов
print("\n=== ЗАДАЧА 10: Общее количество авторов ===")
with engine.connect() as conn:
    result = conn.execute(select(func.count(authors.c.id)))
    count = result.scalar()
    print(f"Всего авторов: {count}")

print("\n=== ВСЕ ПРОСТЫЕ ЗАДАЧИ ВЫПОЛНЕНЫ ===")

# ДОПОЛНИТЕЛЬНЫЕ ПРОСТЫЕ ПРИМЕРЫ:

# Пример 1: Сортировка авторов по алфавиту
print("\n=== ДОПОЛНИТЕЛЬНО: Авторы по алфавиту ===")
with engine.connect() as conn:
    result = conn.execute(
        select(authors.c.name).order_by(authors.c.name)
    )
    for row in result:
        print(f"{row.name}")

# Пример 2: Первые 3 книги
print("\n=== ДОПОЛНИТЕЛЬНО: Первые 3 книги ===")
with engine.connect() as conn:
    result = conn.execute(
        select(books.c.title).limit(3)
    )
    for row in result:
        print(f"{row.title}")

# Пример 3: Книги в диапазоне лет
print("\n=== ДОПОЛНИТЕЛЬНО: Книги 1860-1880 годов ===")
with engine.connect() as conn:
    result = conn.execute(
        select(books.c.title, books.c.year)
        .where(and_(books.c.year >= 1860, books.c.year <= 1880))
    )
    for row in result:
        print(f"{row.title} ({row.year})")