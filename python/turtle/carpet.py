from turtle import Turtle

t = Turtle()

def carpet(size, level=0):
    sub_size = size / 3
    if level <= 0:
        t.shapesize(size, size) 
        t.stamp()
        return
    x, y = t.pos()
    for i in range(3):
        for j in range(3):
            if not (i == 1 and j == 1): # Leave center empty
                t.goto(x+j*sub_size, y-i*sub_size)
                carpet(sub_size, level-1)

def main():
    size = 500
    level = 4
    w = (size / 2)
    offset = (w / 3**level)
    t.teleport(-w + offset, w - offset)
    carpet(size, level)

if __name__ == "__main__":
    t.screen.title("Sierpiński Carpet")
    i = 1/2   
    square = ((-i, i), (i, i), (i, -i), (-i, -i))
    t.screen.register_shape('cell', square)
    t.shape('cell')
    t.penup()
    t.speed(10)
    main()
    t.screen.mainloop()
