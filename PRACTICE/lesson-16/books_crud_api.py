# CRUD API для базы данных books.db на FastAPI для новичков

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import *
from typing import List, Optional

# Подключение к базе данных
engine = create_engine('sqlite:///books.db')
metadata = MetaData()

# Загружаем таблицы
authors = Table('authors', metadata, autoload_with=engine)
books = Table('books', metadata, autoload_with=engine)

# Создаем FastAPI приложение
app = FastAPI(title="Books API", description="Простое API для управления книгами")

# Модели данных (схемы)
class AuthorCreate(BaseModel):
    name: str
    birth_year: int

class Author(BaseModel):
    id: int
    name: str
    birth_year: int

class BookCreate(BaseModel):
    title: str
    year: int
    author_id: int

class Book(BaseModel):
    id: int
    title: str
    year: int
    author_id: int

class BookWithAuthor(BaseModel):
    id: int
    title: str
    year: int
    author_name: str

# === АВТОРЫ (AUTHORS) ===

@app.get("/authors", response_model=List[Author])
def get_all_authors():
    """Получить всех авторов"""
    with engine.connect() as conn:
        result = conn.execute(select(authors))
        return [{"id": row.id, "name": row.name, "birth_year": row.birth_year} 
                for row in result]

@app.get("/authors/{author_id}", response_model=Author)
def get_author(author_id: int):
    """Получить автора по ID"""
    with engine.connect() as conn:
        result = conn.execute(select(authors).where(authors.c.id == author_id))
        row = result.first()
        if not row:
            raise HTTPException(status_code=404, detail="Автор не найден")
        return {"id": row.id, "name": row.name, "birth_year": row.birth_year}

@app.post("/authors", response_model=Author)
def create_author(author: AuthorCreate):
    """Создать нового автора"""
    with engine.connect() as conn:
        result = conn.execute(
            insert(authors).values(name=author.name, birth_year=author.birth_year)
        )
        conn.commit()
        author_id = result.inserted_primary_key[0]
        return {"id": author_id, "name": author.name, "birth_year": author.birth_year}

@app.put("/authors/{author_id}", response_model=Author)
def update_author(author_id: int, author: AuthorCreate):
    """Обновить автора"""
    with engine.connect() as conn:
        result = conn.execute(
            update(authors)
            .where(authors.c.id == author_id)
            .values(name=author.name, birth_year=author.birth_year)
        )
        conn.commit()
        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail="Автор не найден")
        return {"id": author_id, "name": author.name, "birth_year": author.birth_year}

@app.delete("/authors/{author_id}")
def delete_author(author_id: int):
    """Удалить автора"""
    with engine.connect() as conn:
        result = conn.execute(delete(authors).where(authors.c.id == author_id))
        conn.commit()
        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail="Автор не найден")
        return {"message": "Автор удален"}

# === КНИГИ (BOOKS) ===

@app.get("/books", response_model=List[BookWithAuthor])
def get_all_books():
    """Получить все книги с авторами"""
    with engine.connect() as conn:
        result = conn.execute(
            select(books.c.id, books.c.title, books.c.year, authors.c.name.label('author_name'))
            .join(authors)
        )
        return [{"id": row.id, "title": row.title, "year": row.year, "author_name": row.author_name} 
                for row in result]

@app.get("/books/{book_id}", response_model=BookWithAuthor)
def get_book(book_id: int):
    """Получить книгу по ID"""
    with engine.connect() as conn:
        result = conn.execute(
            select(books.c.id, books.c.title, books.c.year, authors.c.name.label('author_name'))
            .join(authors)
            .where(books.c.id == book_id)
        )
        row = result.first()
        if not row:
            raise HTTPException(status_code=404, detail="Книга не найдена")
        return {"id": row.id, "title": row.title, "year": row.year, "author_name": row.author_name}

@app.post("/books", response_model=Book)
def create_book(book: BookCreate):
    """Создать новую книгу"""
    with engine.connect() as conn:
        # Проверяем, существует ли автор
        author_check = conn.execute(select(authors).where(authors.c.id == book.author_id))
        if not author_check.first():
            raise HTTPException(status_code=400, detail="Автор не найден")
        
        result = conn.execute(
            insert(books).values(title=book.title, year=book.year, author_id=book.author_id)
        )
        conn.commit()
        book_id = result.inserted_primary_key[0]
        return {"id": book_id, "title": book.title, "year": book.year, "author_id": book.author_id}

@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book: BookCreate):
    """Обновить книгу"""
    with engine.connect() as conn:
        # Проверяем, существует ли автор
        author_check = conn.execute(select(authors).where(authors.c.id == book.author_id))
        if not author_check.first():
            raise HTTPException(status_code=400, detail="Автор не найден")
        
        result = conn.execute(
            update(books)
            .where(books.c.id == book_id)
            .values(title=book.title, year=book.year, author_id=book.author_id)
        )
        conn.commit()
        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail="Книга не найдена")
        return {"id": book_id, "title": book.title, "year": book.year, "author_id": book.author_id}

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    """Удалить книгу"""
    with engine.connect() as conn:
        result = conn.execute(delete(books).where(books.c.id == book_id))
        conn.commit()
        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail="Книга не найдена")
        return {"message": "Книга удалена"}

# === ДОПОЛНИТЕЛЬНЫЕ ЭНДПОИНТЫ ===

@app.get("/authors/{author_id}/books", response_model=List[Book])
def get_books_by_author(author_id: int):
    """Получить все книги автора"""
    with engine.connect() as conn:
        result = conn.execute(
            select(books).where(books.c.author_id == author_id)
        )
        return [{"id": row.id, "title": row.title, "year": row.year, "author_id": row.author_id} 
                for row in result]

@app.get("/books/search/{title}")
def search_books(title: str):
    """Поиск книг по названию"""
    with engine.connect() as conn:
        result = conn.execute(
            select(books.c.id, books.c.title, books.c.year, authors.c.name.label('author_name'))
            .join(authors)
            .where(books.c.title.like(f'%{title}%'))
        )
        return [{"id": row.id, "title": row.title, "year": row.year, "author_name": row.author_name} 
                for row in result]

@app.get("/")
def root():
    """Главная страница"""
    return {
        "message": "Books API", 
        "docs": "/docs",
        "endpoints": {
            "authors": "/authors",
            "books": "/books",
            "search": "/books/search/{title}"
        }
    }

# Запуск: uvicorn books_crud_api:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)