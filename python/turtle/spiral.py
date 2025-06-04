from turtle import Turtle

t = Turtle()

def left(angDeg):
    if angDeg < 0:
        return right(abs(angDeg))
    
    angDeg %= 360
    if angDeg > 180:
        return right(360 - angDeg)
    t.left(angDeg)

def right(angDeg):
    if angDeg < 0:
        return left(abs(angDeg))
    angDeg %= 360
    if angDeg > 180:
        return left(360 - angDeg)
    t.right(angDeg)
    

def main():
    i = 0
    x, y = t.pos()
    t.speed(0)

    width = t.screen.window_width()
    height = t.screen.window_height()
    x_lim = width * 2
    y_lim = height * 2

    while (x < x_lim and x > -x_lim) or (y < y_lim and y > -y_lim):
        t.penup()
        ang = 360 / (i + 1)
        i += 1
        right(ang)
        t.pendown()
        t.forward(1)
        print(x, y)
        x, y = t.pos()

    print("Done!")
        
if __name__ == "__main__":
    t.screen.title("Spiral")
    main()
    t.screen.mainloop()
