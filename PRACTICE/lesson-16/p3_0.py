from sqlalchemy import *

engine = create_engine('sqlite:///books.db')
metadata = MetaData()


# # Таблица авторов

authors = Table('authors', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(100), nullable=False),
    Column('birth_year', Integer)
    
)


books = Table('books', metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String(200), nullable=False),
    Column('year', Integer),
    Column('author_id', Integer, ForeignKey('authors.id'))
)

metadata.create_all(engine)