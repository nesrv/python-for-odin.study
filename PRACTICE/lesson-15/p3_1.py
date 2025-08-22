from sqlalchemy import *

engine = create_engine('sqlite:///books.db')
metadata = MetaData()


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