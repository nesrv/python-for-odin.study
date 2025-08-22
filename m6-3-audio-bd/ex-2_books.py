from sqlalchemy import *

engine = create_engine('sqlite:///books.db')
metadata = MetaData()

# создать 2 таблицы (авторы - книги, связь 1 ко многим)

# # Таблица авторов
authors = Table('authors', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(100), nullable=False),
    Column('birth_year', Integer)
)

# # Таблица книг
books = Table('books', metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String(200), nullable=False),
    Column('year', Integer),
    Column('author_id', Integer, ForeignKey('authors.id'))
)

# # Создаем таблицы в базе данных
# metadata.create_all(engine)

# exit()
# добавить 10 самых популярных русских книг с авторами

with engine.connect() as conn:
    # Добавляем авторов
    authors_data = [
        {'name': 'Лев Толстой', 'birth_year': 1828},
        {'name': 'Федор Достоевский', 'birth_year': 1821},
        {'name': 'Антон Чехов', 'birth_year': 1860},
        {'name': 'Александр Пушкин', 'birth_year': 1799},
        {'name': 'Михаил Булгаков', 'birth_year': 1891},
        {'name': 'Иван Тургенев', 'birth_year': 1818},
        {'name': 'Николай Гоголь', 'birth_year': 1809}
    ]
    
    for author in authors_data:
        conn.execute(insert(authors).values(**author))
    
    # Добавляем книги
    books_data = [
        {'title': 'Война и мир', 'year': 1869, 'author_id': 1},
        {'title': 'Анна Каренина', 'year': 1877, 'author_id': 1},
        {'title': 'Преступление и наказание', 'year': 1866, 'author_id': 2},
        {'title': 'Братья Карамазовы', 'year': 1880, 'author_id': 2},
        {'title': 'Вишневый сад', 'year': 1904, 'author_id': 3},
        {'title': 'Евгений Онегин', 'year': 1833, 'author_id': 4},
        {'title': 'Мастер и Маргарита', 'year': 1967, 'author_id': 5},
        {'title': 'Отцы и дети', 'year': 1862, 'author_id': 6},
        {'title': 'Мертвые души', 'year': 1842, 'author_id': 7},
        {'title': 'Ревизор', 'year': 1836, 'author_id': 7}
    ]
    
    for book in books_data:
        conn.execute(insert(books).values(**book))
    
    conn.commit()
    print("Данные добавлены успешно!")
    
    # Выводим все книги с авторами
    result = conn.execute(
        select(books.c.title, books.c.year, authors.c.name)
        .select_from(books.join(authors))
    )
    
    print("\nВсе книги:")
    for row in result:
        print(f"{row.title} ({row.year}) - {row.name}")

