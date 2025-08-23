# Простое CRUD API для books.db без Pydantic

from fastapi import FastAPI, HTTPException
from sqlalchemy import *

# Подключение к базе данных
engine = create_engine('sqlite:///books.db')
metadata = MetaData()

# Загружаем таблицы
authors = Table('authors', metadata, autoload_with=engine)
books = Table('books', metadata, autoload_with=engine)

app = FastAPI()

# === АВТОРЫ ===

@app.get("/authors")
def get_authors():
    """Все авторы"""
    with engine.connect() as conn:
        result = conn.execute(select(authors))
        return [dict(row._mapping) for row in result]

@app.get("/authors/{author_id}")
def get_author(author_id: int):
    """Автор по ID"""
    with engine.connect() as conn:
        result = conn.execute(select(authors).where(authors.c.id == author_id))
        row = result.first()
        if not row:
            raise HTTPException(404, "Автор не найден")
        return dict(row._mapping)

@app.post("/authors")
def create_author(name: str, birth_year: int):
    """Создать автора"""
    with engine.connect() as conn:
        result = conn.execute(
            insert(authors).values(name=name, birth_year=birth_year)
        )
        conn.commit()
        return {"id": result.inserted_primary_key[0], "name": name, "birth_year": birth_year}

@app.put("/authors/{author_id}")
def update_author(author_id: int, name: str, birth_year: int):
    """Обновить автора"""
    with engine.connect() as conn:
        result = conn.execute(
            update(authors)
            .where(authors.c.id == author_id)
            .values(name=name, birth_year=birth_year)
        )
        conn.commit()
        if result.rowcount == 0:
            raise HTTPException(404, "Автор не найден")
        return {"id": author_id, "name": name, "birth_year": birth_year}

@app.delete("/authors/{author_id}")
def delete_author(author_id: int):
    """Удалить автора"""
    with engine.connect() as conn:
        result = conn.execute(delete(authors).where(authors.c.id == author_id))
        conn.commit()
        if result.rowcount == 0:
            raise HTTPException(404, "Автор не найден")
        return {"message": "Автор удален"}

# === КНИГИ ===

@app.get("/books")
def get_books():
    """Все книги с авторами"""
    with engine.connect() as conn:
        result = conn.execute(
            select(books.c.id, books.c.title, books.c.year, authors.c.name.label('author'))
            .join(authors)
        )
        return [dict(row._mapping) for row in result]

@app.get("/books/{book_id}")
def get_book(book_id: int):
    """Книга по ID"""
    with engine.connect() as conn:
        result = conn.execute(
            select(books.c.id, books.c.title, books.c.year, authors.c.name.label('author'))
            .join(authors)
            .where(books.c.id == book_id)
        )
        row = result.first()
        if not row:
            raise HTTPException(404, "Книга не найдена")
        return dict(row._mapping)

@app.post("/books")
def create_book(title: str, year: int, author_id: int):
    """Создать книгу"""
    with engine.connect() as conn:
        result = conn.execute(
            insert(books).values(title=title, year=year, author_id=author_id)
        )
        conn.commit()
        return {"id": result.inserted_primary_key[0], "title": title, "year": year, "author_id": author_id}

@app.put("/books/{book_id}")
def update_book(book_id: int, title: str, year: int, author_id: int):
    """Обновить книгу"""
    with engine.connect() as conn:
        result = conn.execute(
            update(books)
            .where(books.c.id == book_id)
            .values(title=title, year=year, author_id=author_id)
        )
        conn.commit()
        if result.rowcount == 0:
            raise HTTPException(404, "Книга не найдена")
        return {"id": book_id, "title": title, "year": year, "author_id": author_id}

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    """Удалить книгу"""
    with engine.connect() as conn:
        result = conn.execute(delete(books).where(books.c.id == book_id))
        conn.commit()
        if result.rowcount == 0:
            raise HTTPException(404, "Книга не найдена")
        return {"message": "Книга удалена"}

# === ДОПОЛНИТЕЛЬНО ===

@app.get("/authors/{author_id}/books")
def get_author_books(author_id: int):
    """Книги автора"""
    with engine.connect() as conn:
        result = conn.execute(select(books).where(books.c.author_id == author_id))
        return [dict(row._mapping) for row in result]

@app.get("/")
def home():
    """Главная"""
    return {"message": "Books API", "docs": "/docs"}

# Запуск: uvicorn books_simple_api:app --reload