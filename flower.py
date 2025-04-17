from turtle import Turtle
from math import pi, sin

t = Turtle()

def range_map(n, min_in, max_in, min_out, max_out):
    slope = (max_out - min_out) / (max_in - min_in)
    return min_out + slope * (n - min_in)

def half_petal(length, resolution=1):
    n_steps = length//resolution
    arc_angle = 180 / n_steps
    for i in range(n_steps):
        mapped_i = range_map(i, 0, length, 0, pi)
        step = sin(mapped_i) * resolution
        t.forward(step)
        t.left(arc_angle)


def petal(length, resolution=1):
    half_petal(length, resolution)
    half_petal(length, resolution)

def flower(n_petals, petal_length, resolution=1):
    turn_angle = 360 / n_petals
    for i in range(n_petals):
        petal(300)
        t.right(turn_angle)
        
def main():
    t.pendown()
    t.speed(0)
    flower(8, 100, 20)

if __name__ == "__main__":
    t.screen.title("Flower")
    main()
    t.screen.mainloop()
