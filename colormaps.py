import matplotlib as plt
from turtle import Turtle

t = Turtle()
colormap = plt.colormaps.get_cmap("Reds")
WIDTH = 1
N_LINES = 255

def main():
    distance = WIDTH * N_LINES
    t.pensize(WIDTH)      
    for i in range(N_LINES):
        percent = i / N_LINES
        color = plt.colors.to_rgb(colormap(percent))
        t.pendown()
        t.pencolor(color)
        t.forward(distance)
        t.penup()
        t.left(90)
        t.forward(WIDTH)
        t.left(90)
        t.forward(distance)
        t.left(180)


if __name__ == "__main__":
    t.speed(0)
    t.screen.title("Colormap Painting")
    main()
    t.screen.mainloop()
    
