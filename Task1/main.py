from tkinter import *

def on_mouse_motion(event):
    canvas.moveto('smile', event.x, event.y )


display = Tk()
display.title("Простой Рисунок")

canvas = Canvas(display, width = 720, height = 720)
canvas.pack()

radius = 100

canvas.create_oval(0, 0, radius, radius, fill="yellow", tags='smile')
display.bind("<Motion>", on_mouse_motion)



display.mainloop()