# 10 задач для базы данных books.db на SQLAlchemy

from sqlalchemy import *

engine = create_engine('sqlite:///books.db')
metadata = MetaData()

# Загружаем таблицы
authors = Table('authors', metadata, autoload_with=engine)
books = Table('books', metadata, autoload_with=engine)

# ЗАДАЧА 1: Найти все книги автора "Лев Толстой"
print("=== ЗАДАЧА 1: Книги Льва Толстого ===")
with engine.connect() as conn:
    result = conn.execute(
        select(books.c.title, books.c.year)
        .select_from(books.join(authors))
        .where(authors.c.name == 'Лев Толстой')
    )
    for row in result:
        print(f"{row.title} ({row.year})")

# ЗАДАЧА 2: Подсчитать количество книг каждого автора
print("\n=== ЗАДАЧА 2: Количество книг по авторам ===")
with engine.connect() as conn:
    result = conn.execute(
        select(authors.c.name, func.count(books.c.id).label('book_count'))
        .select_from(authors.join(books))
        .group_by(authors.c.name)
    )
    for row in result:
        print(f"{row.name}: {row.book_count} книг")

# ЗАДАЧА 3: Найти самого старого автора
print("\n=== ЗАДАЧА 3: Самый старый автор ===")
with engine.connect() as conn:
    result = conn.execute(
        select(authors.c.name, authors.c.birth_year)
        .where(authors.c.birth_year == select(func.min(authors.c.birth_year)))
    )
    for row in result:
        print(f"{row.name} ({row.birth_year})")

# ЗАДАЧА 4: Найти книги, написанные после 1900 года
print("\n=== ЗАДАЧА 4: Книги после 1900 года ===")
with engine.connect() as conn:
    result = conn.execute(
        select(books.c.title, books.c.year, authors.c.name)
        .select_from(books.join(authors))
        .where(books.c.year > 1900)
        .order_by(books.c.year)
    )
    for row in result:
        print(f"{row.title} ({row.year}) - {row.name}")

# ЗАДАЧА 5: Найти авторов, родившихся в 19 веке
print("\n=== ЗАДАЧА 5: Авторы 19 века ===")
with engine.connect() as conn:
    result = conn.execute(
        select(authors.c.name, authors.c.birth_year)
        .where(and_(authors.c.birth_year >= 1801, authors.c.birth_year <= 1900))
        .order_by(authors.c.birth_year)
    )
    for row in result:
        print(f"{row.name} ({row.birth_year})")

# ЗАДАЧА 6: Найти самую раннюю и самую позднюю книгу
print("\n=== ЗАДАЧА 6: Самая ранняя и поздняя книги ===")
with engine.connect() as conn:
    # Самая ранняя
    result = conn.execute(
        select(books.c.title, books.c.year, authors.c.name)
        .select_from(books.join(authors))
        .where(books.c.year == select(func.min(books.c.year)))
    )
    for row in result:
        print(f"Самая ранняя: {row.title} ({row.year}) - {row.name}")
    
    # Самая поздняя
    result = conn.execute(
        select(books.c.title, books.c.year, authors.c.name)
        .select_from(books.join(authors))
        .where(books.c.year == select(func.max(books.c.year)))
    )
    for row in result:
        print(f"Самая поздняя: {row.title} ({row.year}) - {row.name}")

# ЗАДАЧА 7: Найти авторов, у которых есть книги с названием содержащим "и"
print("\n=== ЗАДАЧА 7: Авторы с книгами содержащими 'и' ===")
with engine.connect() as conn:
    result = conn.execute(
        select(authors.c.name)
        .select_from(authors.join(books))
        .where(books.c.title.like('%и%'))
        .distinct()
    )
    for row in result:
        print(row.name)

# ЗАДАЧА 8: Средний год публикации книг
print("\n=== ЗАДАЧА 8: Средний год публикации ===")
with engine.connect() as conn:
    result = conn.execute(select(func.avg(books.c.year)))
    avg_year = result.scalar()
    print(f"Средний год: {avg_year:.1f}")

# ЗАДАЧА 9: Найти автора с наибольшим количеством книг
print("\n=== ЗАДАЧА 9: Автор с наибольшим количеством книг ===")
with engine.connect() as conn:
    subquery = select(
        authors.c.id,
        authors.c.name,
        func.count(books.c.id).label('book_count')
    ).select_from(authors.join(books)).group_by(authors.c.id).subquery()
    
    result = conn.execute(
        select(subquery.c.name, subquery.c.book_count)
        .where(subquery.c.book_count == select(func.max(subquery.c.book_count)))
    )
    for row in result:
        print(f"{row.name}: {row.book_count} книг")

# ЗАДАЧА 10: Добавить нового автора и его книгу, затем найти их
print("\n=== ЗАДАЧА 10: Добавление и поиск нового автора ===")
with engine.connect() as conn:
    # Добавляем автора
    result = conn.execute(
        insert(authors).values(name='Александр Солженицын', birth_year=1918)
    )
    author_id = result.inserted_primary_key[0]
    
    # Добавляем книгу
    conn.execute(
        insert(books).values(
            title='Архипелаг ГУЛАГ', 
            year=1973, 
            author_id=author_id
        )
    )
    
    conn.commit()
    
    # Находим добавленные данные
    result = conn.execute(
        select(books.c.title, books.c.year, authors.c.name)
        .select_from(books.join(authors))
        .where(authors.c.name == 'Александр Солженицын')
    )
    for row in result:
        print(f"Добавлено: {row.title} ({row.year}) - {row.name}")

print("\n=== ВСЕ ЗАДАЧИ ВЫПОЛНЕНЫ ===")

# БОНУС: Полная статистика базы данных
print("\n=== БОНУС: Статистика базы ===")
with engine.connect() as conn:
    # Общее количество авторов
    authors_count = conn.execute(select(func.count(authors.c.id))).scalar()
    
    # Общее количество книг
    books_count = conn.execute(select(func.count(books.c.id))).scalar()
    
    # Диапазон лет
    min_year = conn.execute(select(func.min(books.c.year))).scalar()
    max_year = conn.execute(select(func.max(books.c.year))).scalar()
    
    print(f"Авторов: {authors_count}")
    print(f"Книг: {books_count}")
    print(f"Период: {min_year} - {max_year}")