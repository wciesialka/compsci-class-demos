from BirdBrain import Finch
from time import sleep
bird = Finch("A")

# Move forward "lengthSideCm" centimeters
def forward(lengthSideCm):
    bird.setMove("F", lengthSideCm, 100)

# Move backward "lengthSideCm" centimeters
def backward(lengthSideCm):
    bird.setMove("B", lengthSideCm, 100)

# Turn left "angleDegrees" degrees
def left(angleDegrees):
    bird.setTurn("L", angleDegrees, 100)

# Turn right "angleDegrees" degrees
def right(angleDegrees):
    bird.setTurn("R", angleDegrees, 100)

def snowflake(lengthSideCm, levels): 
    if levels == 0: 
        forward(lengthSideCm) 
        return
    lengthSideCm /= 3.0
    snowflake(lengthSideCm, levels-1) 
    left(60) 
    snowflake(lengthSideCm, levels-1) 
    right(120) 
    snowflake(lengthSideCm, levels-1) 
    left(60) 
    snowflake(lengthSideCm, levels-1) 
    
def blink():
    bird.setBeak(100, 100, 100)
    bird.playNote(100, 0.5)
    sleep(0.3)
    bird.setBeak(0, 0, 0)

length = 15
level = 2

for _ in range(3):     
    snowflake(length, level) 
    right(120) 
    blink()