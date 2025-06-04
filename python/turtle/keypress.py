from turtle import Turtle

MOVE_SPEED = 5
TURN_SPEED = 5

t = Turtle()
t.speed(0)
screen = t.screen
screen.listen()  # Start listening for key events

class KeyTracker:

    def __init__(self, key, my_screen):
        self.__key = key
        self.__screen = my_screen
        self.__pressed = False
        self.__bind()

    def __bind(self):
        self.__screen.onkeypress(lambda: self.__press(), self.__key)
        self.__screen.onkeyrelease(lambda: self.__release(), self.__key)

    def is_down(self):
        return self.__pressed

    @property
    def key(self):
        return self.__key

    @property
    def pressed(self):
        return self.__pressed

    @property
    def screen(self):
        return self.__screen

    def __press(self):
        self.__pressed = True

    def __release(self):
        self.__pressed = False

    def __call__(self):
        return self.pressed

keys = {}

def register_key(key):
    global keys, scren
    tracker = KeyTracker(key, screen)
    keys[key] = tracker
    return tracker

def get_tracker(key):
    global keys
    if key in keys:
        return keys[key]
    return register_key(key)

w_key = register_key("w")
a_key = register_key("a")
s_key = register_key("s")
d_key = register_key("d")
space_key = register_key("space")

def bind_key(key, *, refresh_rate=20):
    def decorator(func):
        key_tracker = get_tracker(key)
        
        def wrapper(*args, **kwargs):
            if key_tracker():
                func(*args, **kwargs)
            screen.ontimer(wrapper, refresh_rate)
        wrapper()
        return wrapper
    return decorator

@bind_key("w")
def forward():
    t.forward(MOVE_SPEED)

@bind_key("a")
def left():
    t.left(TURN_SPEED)

@bind_key("d")
def right():
    t.right(TURN_SPEED)

@bind_key("s")
def backward():
    t.backward(MOVE_SPEED)

@bind_key("space", refresh_rate=250)
def pen_toggle():
    if t.isdown():
        t.penup()
        t.color("red")
    else:
        t.color("black")
        t.pendown()
        


screen.mainloop()  # Keep the window open
