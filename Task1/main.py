from tkinter import *

def crosshair_placement(event):
    canvas.moveto('crosshair', event.x-radius/2, event.y-radius/2 )

def fire(event):
    hole_id = canvas.create_oval(event.x - 5, event.y - 5, event.x + 5, event.y + 5, fill='black')
    display.after(3000, clear_hole, hole_id)

def clear_hole(hole_id):
    canvas.delete(hole_id)


display = Tk()
display.title("Тир")

canvas = Canvas(display, width = 720, height = 720)
canvas.pack()

radius = 100

canvas.create_oval(0, 0, radius, radius, outline="red", width=2, tags='crosshair')
canvas.create_line(radius, radius/2, 0, radius/2, tags='crosshair', width=2)
canvas.create_line(radius/2, radius, radius/2, 0, tags='crosshair', width=2)

display.bind("<Motion>", crosshair_placement)
display.bind("<Button-1>", fire)



display.mainloop()