# Импорт всех классов и функций SQLAlchemy
from sqlalchemy import *
from sqlalchemy import MetaData

# Создаем подключение к SQLite базе данных (файл database.db)
engine = create_engine('sqlite:///database.db')

# Создаем объект метаданных для работы с таблицами
metadata = MetaData()

# Загружаем структуру таблицы 'users' из базы данных
# autoload_with=engine - автоматически определяет колонки и типы

users = Table('users', metadata, autoload_with=engine)

# Получаем всех пользователей из базы данных

# Открываем соединение с базой данных
conn = engine.connect() 

# Выполняем SQL запрос SELECT * FROM users
result = conn.execute(select(users))

# Получаем все строки результата в виде списка
all_users = result.fetchall()
    
# Выводим всех пользователей на экран (каждого с новой строки)
print(*all_users, sep='\n')