import turtle, math, random, json

# Настройка черепашки
t = turtle.Turtle()
t.speed(3)  # Скорость рисования

# Рисуем 5-конечную звезду
for _ in range(5):
    t.forward(100)  # Длина луча звезды
    t.right(144)    # Угол поворота для 5-конечной звезды (144 градуса)

# Оставляем окно открытым
turtle.done()