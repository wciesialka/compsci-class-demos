from turtle import Turtle

t = Turtle()
CELL_SIZE = 10

def main():
    t.speed(6)
    t.penup()
    i = CELL_SIZE//2
    square = ((-i, i), (i, i), (i, -i), (-i, -i))
    t.screen.register_shape('ant', square)
    t.shape('ant')

    squares = {}
    while True:
        #t.speed(0)  
        x, y = t.pos()
        pos = (round(x), round(y))
        if pos in squares:
            t.clearstamp(squares[pos])
            del squares[pos]
            t.right(90)
        else:
            t.color("black")
            stamp_id = t.stamp()
            t.color("red")
            squares[pos] = stamp_id
            t.left(90)
        #t.speed(6)  
        t.forward(CELL_SIZE)
            
        
if __name__ == "__main__":
    t.screen.title("Langton's Ant")
    main()
    t.screen.mainloop()
