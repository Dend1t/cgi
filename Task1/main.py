from tkinter import *
from random import randint
import math as m


def crosshair_placement(event):
    global crosshair_radius;
    canvas.moveto('crosshair', event.x - crosshair_radius, event.y - crosshair_radius)


def fire(event):
    global x1, y1, x2, y2, score, target_radius, dx, dy

    center_x = (x1 + x2) / 2
    center_y = (y1 + y2) / 2

    dx = randint(-2,2)
    dy = randint(-2,2)

    if m.sqrt((event.x - center_x) ** 2 + (event.y - center_y) ** 2) < target_radius:
        hole_id = canvas.create_oval(event.x - 5, event.y - 5, event.x + 5, event.y + 5, fill='black', tags="target")
        score += 1
        canvas.itemconfig(score_text, text=f"Points: {score}")
    else:
        hole_id = canvas.create_oval(event.x - 5, event.y - 5, event.x + 5, event.y + 5, fill='black')
        canvas.tag_lower(hole_id)
    display.after(3000, clear_hole, hole_id)


def clear_hole(hole_id):
    canvas.delete(hole_id)


def move_target():
    global dx, x1, y1, x2, y2, dy
    canvas.move("target", dx, dy)
    x1, y1, x2, y2 = canvas.coords("target")
    if x1 <= 0 or x2 >= 720:
        dx = -dx
    if y1 <= 0 or y2 >= 720:
        dy = -dy
    display.after(10, move_target)


display = Tk()
display.title("Тир")

canvas = Canvas(display, width=720, height=720)
canvas.pack()

target_radius = 260
crosshair_radius = 50

dx = 1
dy = 1
x1 = 0
x2 = 0
y1 = 0
y2 = 0
score = 0

for i in range(8):
    canvas.create_oval(0 + 30 * i, target_radius / 2 + 30 * i, target_radius * 2 - 30 * i, target_radius * 2.5 - 30 * i, outline="red",
                       width=10, tags='target', fill='lightgray')

score_text = canvas.create_text(20, 20, text="Points: 0", font=("Terminal", 18, "bold"), fill="black", anchor="nw")

canvas.create_oval(0, 0, crosshair_radius*2, crosshair_radius*2, outline="aqua", width=4, tags='crosshair')
canvas.create_line(crosshair_radius*2, crosshair_radius, 0, crosshair_radius, tags='crosshair', width=2)
canvas.create_line(crosshair_radius, crosshair_radius*2, crosshair_radius, 0, tags='crosshair', width=2)

display.bind("<Motion>", crosshair_placement)
display.bind("<Button-1>", fire)
display.bind("<Button-3>", fire)

move_target()
display.mainloop()
