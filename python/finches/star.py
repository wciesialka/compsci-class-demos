from BirdBrain import Finch
from math import ceil, gcd
from time import sleep
bird = Finch("A")

MOVE_SPEED = 10
TURN_SPEED = 50
BLINK_SPEED = 0.3
SIDE_LENGTH_CM = 5
NUM_POINTS = 5

# Move forward "lengthSideCm" centimeters
def forward(lengthSideCm):
    bird.setMove("F", lengthSideCm, MOVE_SPEED)

# Move backward "lengthSideCm" centimeters
def backward(lengthSideCm):
    bird.setMove("B", lengthSideCm, MOVE_SPEED)

# Turn left "angleDegrees" degrees
def left(angleDegrees):
    angleDegrees %= 360
    if angleDegrees > 180:
        right(360 - angleDegrees)
    else:
        bird.setTurn("L", angleDegrees, TURN_SPEED)

# Turn right "angleDegrees" degrees
def right(angleDegrees):
    angleDegrees %= 360
    if angleDegrees > 180:
        left(360 - angleDegrees)
    else:
        bird.setTurn("R", angleDegrees, TURN_SPEED)

def blink():
    bird.playNote(100, BLINK_SPEED)
    bird.setBeak(100, 100, 100)
    sleep(BLINK_SPEED)
    bird.setBeak(0, 0, 0)

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
        blink()

make_star(NUM_POINTS, SIDE_LENGTH_CM)