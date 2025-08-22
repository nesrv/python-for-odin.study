from sqlalchemy import *

engine = create_engine('sqlite:///database.db')
metadata = MetaData()
# Загружаем структуру таблицы 'users' из базы данных
# autoload_with=engine - автоматически определяет колонки и типы

users = Table('users', metadata, autoload_with=engine)

conn = engine.connect() 
result = conn.execute(select(users))

all_users = result.fetchall()
    
# Выводим всех пользователей на экран (каждого с новой строки)
print(*all_users, sep='\n')