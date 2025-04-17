# Import everything from the turtle library.
from turtle import *

# Move the turtle to it's home position
home()

# Set the turtle to "pen down" mode so it can draw
pendown()

# Draw a shape
for _ in range(5):
    forward(100)
    right(72)

# Run turtle code without closing the window after execution.
mainloop()
