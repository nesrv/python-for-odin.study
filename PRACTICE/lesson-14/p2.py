import sqlite3

conn = sqlite3.connect('database.db')

cursor = conn.cursor()

# users = [   
#     ('user9', 'password9'),
#     ('user10', 'password10'),
#      ('Галина', 'Карымова'), 
# ]

# cursor.executemany("INSERT INTO users (username, password) VALUES (?, ?)", users)
# cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('user2', 'password2'))
   


# cursor.execute("SELECT password, username FROM users WHERE username='Галина'")
# cursor.execute("SELECT username FROM users WHERE id >= 5")

cursor.execute("DELETE FROM users  WHERE id = 1")
conn.commit()

# users = cursor.fetchall()
# print(*users,sep='\n')

# conn.commit()
# print("Данные добавлены")

# for user in users:
#     print(user)