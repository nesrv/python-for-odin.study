import tkinter as tk

root = tk.Tk()
root.title("Арканоид")
canvas = tk.Canvas(root, width=400, height=300, bg='black')
canvas.pack()

# Создание объектов
paddle = canvas.create_rectangle(150, 280, 250, 290, fill='white')
ball = canvas.create_oval(190, 200, 210, 220, fill='red')
blocks = [canvas.create_rectangle(c*50, r*30, c*50+45, r*30+25, fill='blue') 
          for r in range(3) for c in range(8)]

ball_dx, ball_dy = 2, 2

def move_paddle(event):
    pos = canvas.coords(paddle)
    dx = -20 if event.keysym == 'Left' else 20
    if 0 <= pos[0] + dx <= 300: canvas.move(paddle, dx, 0)

def game_loop():
    global ball_dx, ball_dy
    canvas.move(ball, ball_dx, ball_dy)
    x1, y1, x2, y2 = canvas.coords(ball)
    
    if x1 <= 0 or x2 >= 400: ball_dx = -ball_dx
    if y1 <= 0: ball_dy = -ball_dy
    
    # Столкновение с платформой
    px1, py1, px2, py2 = canvas.coords(paddle)
    if y2 >= py1 and x2 >= px1 and x1 <= px2: ball_dy = -ball_dy
    
    # Столкновение с блоками
    for block in blocks[:]:
        bx1, by1, bx2, by2 = canvas.coords(block)
        if x2 >= bx1 and x1 <= bx2 and y2 >= by1 and y1 <= by2:
            canvas.delete(block)
            blocks.remove(block)
            ball_dy = -ball_dy
            break
    
    if y2 >= 300:
        canvas.create_text(200, 150, text="ИГРА ОКОНЧЕНА", fill='white', font=('Arial', 20))
        return
    
    root.after(20, game_loop)

root.bind('<Key>', move_paddle)
root.focus_set()
game_loop()
root.mainloop()