### Imports ###
from BirdBrain import Finch
from math import inf
bird = Finch("A")

# Global Variables
poly_sides = 3
MIN_POLY_SIDES = 3
MAX_POLY_SIDES = 8
SIDE_LENGTH = 10
REFRESH_RATE_MS = 20
MS_PER_S = 1000
REFRESH_RATE_S = REFRESH_RATE_MS / MS_PER_S

### defs ###
cycle = 0
def polyangle(n_sides):
    if n_sides < 0:
        raise f"Cannot make a polygon with less than 3 sides ({n_sides})"
    external = (n_sides - 2) * 180
    internal = (180 - external) / n_sides
    return internal

def forward(length_cm):
    bird.setMove("F", length_cm, 100)

def left(ang):
    while ang < 0:
        ang += 360
    ang %= 360
    if ang > 180:
        right(360 - ang)
    else:
        bird.setTurn("L", ang, 100)

def right(ang):
    while ang < 0:
        ang += 360
    ang %= 360
    if ang > 180:
        left(360 - ang)
    else:
        bird.setTurn("R", ang, 100)

def polygon(n_sides):
    if n_sides < 3:
        raise f"Cannot make a polygon with less than 3 sides ({n_sides})"
    bird.print(n_sides)
    ang = polyangle(n_sides)
    for _ in range(n_sides):
        forward(SIDE_LENGTH)
        right(ang)

### code ###
print("Running!")
while True:
    a = bird.getButton("A")
    b = bird.getButton("B")
    if a and b:
        polygon(poly_sides)
    else:
        if a and poly_sides > MIN_POLY_SIDES:
            poly_sides -= 1
        elif b and poly_sides < MAX_POLY_SIDES:
            poly_sides += 1
        bird.print(poly_sides)
    time.sleep(REFRESH_RATE_MS)
