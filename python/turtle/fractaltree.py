from turtle import Turtle

t = Turtle()
ANGLE_LEFT = 20
ANGLE_RIGHT = 20
LENGTH_FACTOR = 0.8

def branch(length, children):
    t.pendown()
    t.forward(length)
    t.penup()
    if children > 1:
        pos = t.pos()
        ang = t.heading()
        t.left(ANGLE_LEFT)
        branch(length*LENGTH_FACTOR, children-1)
        t.teleport(*pos)
        t.seth(ang)
        t.right(ANGLE_RIGHT)
        branch(length*LENGTH_FACTOR, children-1)

def main():
    branch(100, 7)

if __name__ == "__main__":
    t.screen.title("Fractal Tree")
    t.screen.screensize(600, 600)
    t.teleport(0, -300)
    t.seth(90)
    main()
    t.screen.mainloop()
