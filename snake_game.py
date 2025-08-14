import tkinter as tk
import random

# Настройки игры
GAME_WIDTH = 600
GAME_HEIGHT = 600
SPEED = 100
SPACE_SIZE = 20
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

# Глобальные переменные
score = 0
direction = 'down'
snake = []
food = {}

def next_turn():
    """Основной игровой цикл - движение змейки"""
    global snake, food, score, direction
    
    # Получаем координаты головы змейки
    x, y = snake[0]
    
    # Изменяем координаты в зависимости от направления
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE
    
    # Добавляем новую голову
    snake.insert(0, (x, y))
    
    # Проверяем, съела ли змейка еду
    if x == food['x'] and y == food['y']:
        score += 1
        label.config(text="Счет: {}".format(score))
        canvas.delete("food")
        create_food()
    else:
        # Убираем хвост, если еда не съедена
        del snake[-1]
    
    # Очищаем холст и перерисовываем змейку
    canvas.delete("snake")
    for x, y in snake:
        canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, 
                              fill=SNAKE_COLOR, tag="snake")
    
    # Проверяем столкновения
    check_collisions()
    
    # Планируем следующий ход
    window.after(SPEED, next_turn)

def change_direction(new_direction):
    """Изменение направления движения змейки"""
    global direction
    
    # Предотвращаем движение в противоположную сторону
    if new_direction == 'left' and direction != 'right':
        direction = new_direction
    elif new_direction == 'right' and direction != 'left':
        direction = new_direction
    elif new_direction == 'up' and direction != 'down':
        direction = new_direction
    elif new_direction == 'down' and direction != 'up':
        direction = new_direction

def check_collisions():
    """Проверка столкновений со стенами и самой собой"""
    x, y = snake[0]
    
    # Столкновение со стенами
    if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
        game_over()
    
    # Столкновение с самой собой
    for body_part in snake[1:]:
        if x == body_part[0] and y == body_part[1]:
            game_over()

def game_over():
    """Завершение игры"""
    canvas.delete(tk.ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                      font=('Arial', 70), text="ИГРА ОКОНЧЕНА", fill="red")

def create_food():
    """Создание еды в случайном месте"""
    global food
    
    # Генерируем случайные координаты, кратные размеру клетки
    x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
    y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
    
    food = {'x': x, 'y': y}
    
    # Рисуем еду
    canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, 
                      fill=FOOD_COLOR, tag="food")

def start_game():
    """Инициализация игры"""
    global snake, score, direction
    
    # Сброс переменных
    score = 0
    direction = 'down'
    label.config(text="Счет: {}".format(score))
    canvas.delete(tk.ALL)
    
    # Создаем начальную змейку
    snake = []
    for i in range(BODY_PARTS):
        snake.append((0, i * SPACE_SIZE))
    
    # Создаем еду и запускаем игру
    create_food()
    next_turn()

# Создание главного окна
window = tk.Tk()
window.title("Змейка")
window.resizable(False, False)

# Метка для отображения счета
label = tk.Label(window, text="Счет: {}".format(score), font=('Arial', 40))
label.pack()

# Холст для игры
canvas = tk.Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

# Кнопка для начала новой игры
start_button = tk.Button(window, text="Новая игра", font=('Arial', 16), command=start_game)
start_button.pack()

# Центрирование окна на экране
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Привязка клавиш для управления
window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

# Фокус на окне для обработки клавиш
window.focus_set()

# Запуск игры
start_game()
window.mainloop()