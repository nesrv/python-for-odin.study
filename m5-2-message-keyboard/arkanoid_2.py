
import tkinter as tk

root = tk.Tk()
root.title("Арканоид")
root.attributes("-topmost", True)
canvas = tk.Canvas(root, width=400, height=300, bg='black')
canvas.pack()


paddle = canvas.create_rectangle(150, 280, 250, 290, fill='white')
ball = canvas.create_oval(190, 200, 210, 220, fill='red')

c = 0
r = 0
blocks = []
for r in range(4):
    for c in range(10):
        blocks.append(canvas.create_rectangle(
            c*50, r*30, c*50+45, r*30+25, fill='blue'))


def move_paddle(event):
    pos = canvas.coords(paddle)
    if event.keysym == 'Left' and pos[0] > 0:
        canvas.move(paddle, -20, 0)
    elif event.keysym == 'Right' and pos[2] < 400:
        canvas.move(paddle, 20, 0)


ball_dx, ball_dy = 2, -2


def game_loop():
    global ball_dx, ball_dy
    canvas.move(ball, ball_dx, ball_dy)
    x1, y1, x2, y2 = canvas.coords(ball)

    if x1 <= 0 or x2 >= 400:
        ball_dx = -ball_dx
    if y1 <= 0:
        ball_dy = -ball_dy

    # Столкновение с платформой
    px1, py1, px2, py2 = canvas.coords(paddle)
    if y2 >= py1 and x2 >= px1 and x1 <= px2:
        ball_dy = -ball_dy

    for block in blocks:
        bx1, by1, bx2, by2 = canvas.coords(block)
        if x2 >= bx1 and x1 <= bx2 and y2 >= by1 and y1 <= by2:
            canvas.delete(block)
            blocks.remove(block)
            ball_dy = -ball_dy
            break

    root.after(20, game_loop)  # Повторяем каждые 20мс


root.bind('<Key>', move_paddle)
root.focus_set()
game_loop()
root.mainloop()
