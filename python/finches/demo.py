from BirdBrain import Finch
from time import sleep

myFinch = Finch("A")
myFinch.playNote(80, 0.1)
sleep(0.2)
myFinch.playNote(80, 0.1)

waiting_for_button = True

def calc_speed(light_level):
    if light_level < 20:
        return -100
    if light_level < 40:
        return -50
    elif light_level < 60:
        return 0
    elif light_level < 80:
        return 50
    else:
        return 100
        
while waiting_for_button:
    if(myFinch.getButton("A")):
        waiting_for_button = False
        for note in [(32+(x*5)) for x in range(8)]:
            myFinch.playNote(note, 1)
            sleep(0.5)
        myFinch.setTurn("R", 360, 100)
        waiting_for_button = True
    if(myFinch.getButton("B")):
        waiting_for_button = False
        myFinch.playNote(80, 0.1)
        sleep(0.2)
        myFinch.playNote(85, 0.1)

        while not myFinch.getButton("B"):
            left_light = myFinch.getLight("L")
            right_light = myFinch.getLight("R")
            left_speed = calc_speed(left_light)
            right_speed = calc_speed(right_light)
            myFinch.setMotors(left_speed, right_speed)
            sleep(0.1)
        myFinch.setMotors(0, 0)
        myFinch.playNote(80, 0.1)
        sleep(0.2)
        myFinch.playNote(75, 0.1)

        waiting_for_button = True