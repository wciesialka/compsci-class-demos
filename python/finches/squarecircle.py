import turtle
from math import sqrt, pi, sin, cos

turt = turtle.Turtle()

def square(sideLength):
    for _ in range(4):
        turt.forward(sideLength)
        turt.right(90)

def main():
    SIDE_LENGTH = 20
    N_SQUARES = 20
    ANGLE = 360 / N_SQUARES
    half_angle_rad = (ANGLE / 2) * (pi / 180)
    radius = (SIDE_LENGTH / 2) / sin(half_angle_rad)
    distance_between_squares = 2 * radius * sin(half_angle_rad)

    for i in range(N_SQUARES):
        turt.pendown()
        square(SIDE_LENGTH)
        turt.penup()
        turt.left(ANGLE)
        turt.forward(distance_between_squares + i)

if __name__ == "__main__":
    turtle.setup(600, 600, None, None)
    turt.penup()
    turt.speed(0)
    turt.goto(0, 0)
    turt.showturtle()
    turt.pendown()
    main()
    turt.screen.mainloop()