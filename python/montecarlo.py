import tkinter
import random
from math import sqrt, pi, inf

WIDTH = 600
HEIGHT = 600

root = tkinter.Tk("Monte-carlo Approximation of Pi")
frame = tkinter.Frame(root)
canvas = tkinter.Canvas(frame, width=WIDTH, height=HEIGHT)
label_text = tkinter.StringVar()  # Use a StringVar to update the text dynamically
label_text.set("Approximation: 0")  # Initial text
label = tkinter.Label(frame, textvariable=label_text, font=("Arial", 12))
label.pack()  # Pack the label into the frame

bestof_text = tkinter.StringVar()  # Use a StringVar to update the text
bestof_text.set("Best Approximation: 0")  # Initial text
bestof_label = tkinter.Label(frame, textvariable=bestof_text, font=("Arial", 12))
bestof_label.pack()  # Pack the label into the frame

best_percent = inf

canvas.pack()
frame.pack()

n_total = 0
n_inside = 0

def point(x, y, color):
    x1, y1 = (x-1), (y-1)
    x2, y2 = (x+1), (y+1)
    canvas.create_oval(x1, y1, x2, y2, fill = color, outline = color)

def randpoint():
    return (random.randint(0, WIDTH), random.randint(0, HEIGHT))

def dist(point1, point2):
    return sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

def cdist(x, y):
    radius = WIDTH / 2
    return dist((WIDTH/2,HEIGHT/2), (x,y)) / radius

def approximate(n_inside, n_total):
    approximation = (n_inside / (n_total))*4
    error = abs(approximation - pi)
    poe = error / pi
    return (approximation, poe)

def place_random_point():
    global n_total, n_inside, best_percent
    x, y = randpoint()
    if cdist(x, y) > 1:
        point(x, y, "blue")
    else:
        n_inside += 1
        point(x, y, "red")
    n_total += 1
    approximation, poe = approximate(n_inside, n_total)
    if poe < best_percent:
        best_percent = poe
        bestof_text.set(f"Best Approximation: {approximation:.4f}... ({n_inside*4}/{n_total}) [Error: {poe:.1f}%]")
    poe *= 100
    label_text.set(f"Current Approximation: {approximation:.4f}... ({n_inside*4}/{n_total}) [Error: {poe:.1f}%]")

def main_loop():
    place_random_point()
    root.after(20, main_loop)
    
main_loop()
root.mainloop()
