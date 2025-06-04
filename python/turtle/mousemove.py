from turtle import Turtle
from math import atan2, degrees, pi

REFRESH_RATE_MS = 20

t = Turtle()
screen = t.screen
screen.listen()

last_point = None
mouse_loc = None

def on_mouse_move(x, y):
    global mouse_loc
    mouse_loc = (x, y)

def fequal(a, b, *, tolerance=0.5):
  if a == b:
    return True
  return abs(a-b) < tolerance

def turtle_move():
    global last_point, mouse_loc, screen

    screen.ontimer(turtle_move, REFRESH_RATE_MS)
    if not mouse_loc:
        return

    x1, y1 = mouse_loc
    t.goto(x1, y1)
    if last_point:
        x2, y2 = last_point
        if fequal(x1, x2) and fequal(y1, y2):
            return
        delta_y = y2 - y1
        delta_x = x2 - x1
        arctan = atan2(delta_y, delta_x)
        ang = (degrees(arctan) + 180) % 360
        t.seth(ang)
    last_point = mouse_loc

def onmove(self, func, add=None):

    if func is None:
        self.cv.unbind('<Motion>')
    else:
        def eventfun(event):
            func(self.cv.canvasx(event.x) / self.xscale, -self.cv.canvasy(event.y) / self.yscale)
        self.cv.bind('<Motion>', eventfun, add)

onmove(screen, on_mouse_move)
turtle_move()
screen.mainloop()
