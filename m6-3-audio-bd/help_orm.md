# Шпаргалка по SQLAlchemy ORM для новичков

## Установка
```bash
pip install sqlalchemy
```

## Базовые компоненты

### 1. Подключение к БД
```python
from sqlalchemy import create_engine

# SQLite
engine = create_engine('sqlite:///database.db')

# PostgreSQL
engine = create_engine('postgresql://user:password@localhost/dbname')
```

### 2. Определение моделей
```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True)
    
    # Связь один-ко-многим
    posts = relationship("Post", back_populates="author")

class Post(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    content = Column(String)
    author_id = Column(Integer, ForeignKey('users.id'))
    
    # Обратная связь
    author = relationship("User", back_populates="posts")
```

### 3. Создание таблиц
```python
Base.metadata.create_all(engine)
```

## Сессии и работа с данными

### 4. Создание сессии
```python
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()
```

### 5. CRUD операции

**Create (Создание):**
```python
new_user = User(name="John", email="john@example.com")
session.add(new_user)
session.commit()
```

**Read (Чтение):**
```python
# Получить все записи
users = session.query(User).all()

# Фильтрация
user = session.query(User).filter_by(name="John").first()
user = session.query(User).filter(User.email.like("%@example.com")).all()

# Получить по ID
user = session.get(User, 1)
```

**Update (Обновление):**
```python
user = session.query(User).filter_by(name="John").first()
user.email = "new_email@example.com"
session.commit()
```

**Delete (Удаление):**
```python
user = session.query(User).filter_by(name="John").first()
session.delete(user)
session.commit()
```

## Запросы

### 6. Базовые запросы
```python
# SELECT * FROM users;
users = session.query(User).all()

# SELECT name, email FROM users;
results = session.query(User.name, User.email).all()

# SELECT * FROM users WHERE name = 'John';
users = session.query(User).filter(User.name == 'John').all()

# LIMIT и OFFSET
users = session.query(User).limit(10).offset(5).all()
```

### 7. Сортировка
```python
# ORDER BY name ASC
users = session.query(User).order_by(User.name).all()

# ORDER BY name DESC
users = session.query(User).order_by(User.name.desc()).all()
```

### 8. Связи между таблицами
```python
# Получить посты пользователя
user = session.query(User).first()
posts = user.posts

# Получить автора поста
post = session.query(Post).first()
author = post.author

# JOIN запрос
results = session.query(User, Post).join(Post).filter(User.name == "John").all()
```

## Полезные методы

### 9. Работа с сессией
```python
# Добавить несколько объектов
session.add_all([user1, user2, user3])

# Откатить изменения
session.rollback()

# Закрыть сессию
session.close()
```

### 10. Агрегатные функции
```python
from sqlalchemy import func

# COUNT
count = session.query(func.count(User.id)).scalar()

# MAX, MIN, AVG
max_id = session.query(func.max(User.id)).scalar()
avg_id = session.query(func.avg(User.id)).scalar()
```

## Важные моменты

- Всегда закрывайте сессии после использования
- Используйте `try-except` для обработки ошибок
- Для production используйте пулы соединений
- Миграции схемы лучше делать через Alembic

Это основы SQLAlchemy ORM. Для более сложных сценариев изучайте:
- relationship (один-ко-многим, многие-ко-многим)
- гибридные свойства
- события (events)
- сложные запросы с подзапросами