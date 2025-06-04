from turtle import Turtle

t = Turtle()

def segment(length, level=0):
    length /= 3
    t.forward(length)
    if level == 0:
        t.forward(length)
    else:
        t.left(60)
        segment(length, level-1)
        t.right(120)
        segment(length, level-1)
        t.left(60)
    t.forward(length)

def main():
    t.speed(0)
    for i in range(3):
        segment(300, 5)
        t.right(120)

if __name__ == "__main__":
    t.screen.title("Koch Snowflake")
    main()
    t.screen.mainloop()
