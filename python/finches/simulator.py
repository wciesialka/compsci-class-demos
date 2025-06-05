import turtle
from math import gcd, ceil

turt = turtle.Turtle()

# Move forward "lengthSideCm" centimeters
def forward(lengthSideCm):
    turt.down()
    turt.forward(lengthSideCm)
    turt.up()

# Move backward "lengthSideCm" centimeters
def backward(lengthSideCm):
    turt.down()
    turt.back(lengthSideCm)
    turt.up()

# Turn left "angleDegrees" degrees
def left(angleDegrees):
    angleDegrees %= 360
    if angleDegrees > 180:
        right(360 - angleDegrees)
    else:
        turt.left(angleDegrees)

# Turn right "angleDegrees" degrees
def right(angleDegrees):
    angleDegrees %= 360
    if angleDegrees > 180:
        left(360 - angleDegrees)
    else:
        turt.right(angleDegrees)

def find_skip(num_points):
    if num_points % 2 == 0:
        return 2
    for k in range(2, ceil(num_points / 2) + 1):
        if gcd(num_points, k) == 1:
            return k
    return 1

def make_star_point(side_length, turn_angle):
    right(turn_angle)
    forward(side_length)
    left(turn_angle)
    forward(side_length)
    right(turn_angle)

def make_star(num_points, side_length):
    point_angle = 180 - (180 / num_points)
    skip = find_skip(num_points)
    turn_angle = (point_angle * skip) % 360

    for _ in range(num_points):
        make_star_point(side_length, turn_angle)

def main():
    turtle.setup(600, 600, None, None)
    turt.home()
    turt.showturtle()
    
    make_star(7, 15)

if __name__ == "__main__":
    main()
    turt.screen.mainloop()