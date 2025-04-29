from turtle import Turtle
from math import gcd, ceil

t = Turtle()

# Turn left "angleDegrees" degrees
def left(angleDegrees):
    angleDegrees %= 360
    if angleDegrees > 180:
        right(360 - angleDegrees)
    else:
        t.left(angleDegrees)

# Turn right "angleDegrees" degrees
def right(angleDegrees):
    angleDegrees %= 360
    if angleDegrees > 180:
        left(360 - angleDegrees)
    else:
        t.right(angleDegrees)

def find_skip(num_points):
    if num_points % 2 == 0:
        return 2
    for k in range(2, ceil(num_points / 2) + 1):
        if gcd(num_points, k) == 1:
            return k
    return 1

def make_star_point(side_length, turn_angle):
    left(turn_angle)
    t.forward(side_length)
    right(turn_angle)
    t.forward(side_length)
    left(turn_angle)

def make_star(num_points, side_length):
    point_angle = 180 - (180 / num_points)
    skip = find_skip(num_points)
    turn_angle = (point_angle * skip) % 360

    for _ in range(num_points):
        make_star_point(side_length, turn_angle)

def main():
    make_star(5, 100)

if __name__ == "__main__":
    t.screen.title("Star")
    main()
    t.screen.mainloop()
