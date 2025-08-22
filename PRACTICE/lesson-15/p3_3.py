from sqlalchemy import *
from sqlalchemy import func

engine = create_engine('sqlite:///books.db')
metadata = MetaData()


authors = Table('authors', metadata, autoload_with=engine)
books = Table('books', metadata, autoload_with=engine)

print("=== ЗАДАЧА 1: Все авторы ===")

conn = engine.connect()
result = conn.execute(select(authors))

for row in result:
    print(row.name)

# print(*result, sep='\n')

# ЗАДАЧА 2: Показать все книги
result = conn.execute(select(books.c.title))
print(*result, sep='\n')

print("\n=== ЗАДАЧА 3: Найти Антона Чехова ===")

res = conn.execute(select(authors).where(authors.c.name == 'Антон Чехов'))
print(*res, sep='\n')


print("\n=== ЗАДАЧА 4: Найти 'Война и мир' ===")

res = conn.execute(select(books).where(books.c.title == 'Война и мир'))
print(*res, sep='\n')

# самостоятельно 

print("\n=== ЗАДАЧА 6: Книги 1833 года ===")

result = conn.execute(select(books.c.title).where(books.c.year > 1869))

print(*result, sep='\n')

print("\n=== ЗАДАЧА 9: Общее количество книг ===")

result = conn.execute(select(func.count()).select_from(books))
result = result.scalar()
print(result)

print ("\n#  Сортировка авторов по алфавиту")

res = conn.execute(select(authors.c.name).order_by(authors.c.name).limit(3))
print(*res, sep='\n')

# отсортируй res по фамилии автора (питоном)

print("=== ЗАДАЧА 1: Книги Льва Толстого ===")


# res = conn.execute(select(books).where(books.c.author_id == 1))

res =  conn.execute(select(books.c.title, books.c.year, authors.c.name)
                    .select_from(books.join(authors))
                    .where(authors.c.name == 'Лев Толстой'))

res = conn.execute(
    select(books.c.title, books.c.year, authors.c.name)
    .join(authors)
    .where(authors.c.name == 'Лев Толстой')
)

res = conn.execute(
    select(books, authors)
    .join(authors)
    .where(authors.c.name == 'Лев Толстой')
)

print(*res, sep='\n')

print("\n=== ЗАДАЧА 10: Количество книг по авторам ===")

res = conn.execute(
    select(authors.c.name, func.count(books.c.id).label('кол-во книг'))
    .select_from(authors.join(books))
    .group_by(authors.c.name)
)

res = conn.execute(
    select(authors.c.name, func.count())
    .join(books)
    .group_by(authors.c.name)
)

print(*res, sep='\n')

print ('-------')
# ЗАДАЧА 11: Найти авторов, у которых есть книги с названием содержащим "и"

res = conn.execute(
    select(authors.c.name, books.c.title)
    .select_from(authors.join(books))
    .where(books.c.title.like('% и %'))
    .group_by(authors.c.name)
)

print(*res, sep='\n')

# ЗАДАЧА 6: Найти самую раннюю книгу

res = conn.execute(
    select(books.c.title,func.min(books.c.year))  
)

print(*res, sep='\n')