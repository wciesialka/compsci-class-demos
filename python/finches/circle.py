from BirdBrain import Finch
from time import perf_counter
from math import pi

bird = Finch()

TRACK_LENGTH_CM = 10.2 # 10.2cm
WHEEL_DIAMETER_CM = 5 # 5 cm
WHEEL_RADIUS_CM = WHEEL_DIAMETER_CM / 2
WHEEL_CIRCUMFERENCE_CM = WHEEL_RADIUS_CM * 2 * pi
BIRD_SPEED_CM_S = 50 # Top speed ~ 50 cm/s

def circle(radius, speed=1):
    max_speed = 200 / TRACK_LENGTH_CM
    if speed < 0 or speed > (max_speed):
        raise ValueError(f"Invalid speed: {speed}")
    if radius < (TRACK_LENGTH_CM / 2):
        raise ValueError(f"Invalid radius: {radius}")
    half_track = TRACK_LENGTH_CM / 2
    v_l = speed * (radius - half_track)
    v_2 = speed * (radius + half_track)
    bird.setMotors(v_1, v_2)
    # Circumference of circle / speed should be good...
    circle_circumference_cm = 2 * pi * radius
    time_for_circle = circle_circumference_cm / BIRD_SPEED_CM_S
    sleep(time_for_circle)
    