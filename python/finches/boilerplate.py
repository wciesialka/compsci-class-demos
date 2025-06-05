from BirdBrain import Finch
bird = Finch("A")

MOVE_SPEED = 10
TURN_SPEED = 50

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
