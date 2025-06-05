from BirdBrain import Finch
from time import perf_counter
from math import pi

bird = Finch()

TRACK_LENGTH_CM = 10.2 # 10.2cm
WHEEL_DIAMETER_CM = 5 # 5 cm
WHEEL_RADIUS_CM = WHEEL_DIAMETER_CM / 2
WHEEL_CIRCUMFERENCE_CM = WHEEL_RADIUS_CM * 2 * pi

# Go full speed
bird.setMotors(100, 100)
# Wait til top speed reached
sleep(2)
# Reset encoders & get start time
bird.resetEncoders()
start_time_s = perf_counter()
# Wait til one full rotation
left_rotations = 0
right_rotations = 0
while left_rotations < 1 and right_rotations < 1:
    left_rotations = bird.getEncoder("L")
    right_rotations = bird.getEncoder("R")
# Get end time and stop motors
end_time_s = perf_counter()
bird.stop()
# Calculate distance traveled based on wheel circumference
left_distance_traveled = left_rotations * WHEEL_CIRCUMFERENCE_CM 
right_distance_traveled = right_rotations * WHEEL_CIRCUMFERENCE_CM
average_distance_traveled = (left_distance_traveled + right_distance_traveled) / 2
# Find speed using time
time_difference_s = end_time_s - start_time_s
average_wheel_speed_cms = average_distance_traveled / time_difference_s
# Output findings
print(f"Top speed of Finch: {average_wheel_speed_cms:.2f}cm/s")