from BirdBrain import Finch
bird = Finch("A")

MOVE_SPEED = 50
TURN_SPEED = 50
NUM_SIDES = 8
ANGLE_SUM = (NUM_SIDES - 2) * 180
INTERNAL_ANGLE = ANGLE_SUM / NUM_SIDES
EXTERNAL_ANGLE = 180 - INTERNAL_ANGLE
SIDE_LENGTH_CM = 5

# Move forward "lengthSideCm" centimeters
def forward(lengthSideCm):
    bird.setMove("F", lengthSideCm, MOVE_SPEED)

# Move backward "lengthSideCm" centimeters
def backward(lengthSideCm):
    bird.setMove("B", lengthSideCm, MOVE_SPEED)

# Turn left "angleDegrees" degrees
def left(angleDegrees):
    while angleDegrees < 0:
        angleDegrees = 360 + angleDegrees
    angleDegrees %= 360
    if angleDegrees > 180:
        right(360 - angleDegrees)
    else:
        bird.setTurn("L", angleDegrees, TURN_SPEED)

# Turn right "angleDegrees" degrees
def right(angleDegrees):
    while angleDegrees < 0:
        angleDegrees = 360 + angleDegrees
    angleDegrees %= 360
    if angleDegrees > 180:
        left(360 - angleDegrees)
    else:
        bird.setTurn("R", angleDegrees, TURN_SPEED)

for _ in range(NUM_SIDES):
    forward(SIDE_LENGTH_CM)
    right(EXTERNAL_ANGLE)