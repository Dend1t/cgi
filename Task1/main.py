from tkinter import *
import math as m

def crosshair_placement(event):
    canvas.moveto('crosshair', event.x-35, event.y-35)

def fire(event):
    global x1, y1, x2, y2, score, radius

    center_x = (x1 + x2) / 2
    center_y = (y1 + y2) / 2
    if m.sqrt((event.x-center_x)**2 + (event.y-center_y)**2) < radius:
        hole_id = canvas.create_oval(event.x - 5, event.y - 5, event.x + 5, event.y + 5, fill='black', tags="target")
        score+=1
        canvas.itemconfig(score_text, text=f"Points: {score}")
    else:
        hole_id = canvas.create_oval(event.x - 5, event.y - 5, event.x + 5, event.y + 5, fill='black')
        canvas.tag_lower(hole_id)
    display.after(3000, clear_hole, hole_id)


def clear_hole(hole_id):
    canvas.delete(hole_id)

def move_target():
    global dx, x1, y1, x2, y2
    canvas.move("target", dx, 0)
    x1, y1, x2, y2=canvas.coords("target")
    if x1 <= 0 or x2 >= 720:
        dx = -dx
    display.after(10, move_target)


display = Tk()
display.title("Тир")

canvas = Canvas(display, width = 720, height = 720)
canvas.pack()

radius = 250

dx = 1
x1 = 0
x2 = 0
y1 = 0
y2 = 0
score = 0

for i in range(8):
    canvas.create_oval(0+30*i, 110+30*i, radius*2-30*i, radius*2+110-30*i, outline="blue", width=10, tags='target',fill='lightgray')

score_text = canvas.create_text(20, 20, text="Points: 0", font=("Terminal", 18, "bold"), fill="black", anchor="nw")

canvas.create_oval(0, 0, 70, 70, outline="red", width=2, tags='crosshair')
canvas.create_line(70, 35, 0, 35, tags='crosshair', width=2)
canvas.create_line(35, 70, 35, 0, tags='crosshair', width=2)


display.bind("<Motion>", crosshair_placement)
display.bind("<Button-1>", fire)
display.bind("<Button-3>", fire)

move_target()
display.mainloop()