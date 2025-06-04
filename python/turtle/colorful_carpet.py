import matplotlib as plt
from turtle import Turtle

t = Turtle()
SIZE = 500
LEVELS = 4
NUM_SQUARES = 8 ** LEVELS
colormap = plt.colormaps.get_cmap("RdPu")
w = (SIZE / 2)
offset = (w / 3**LEVELS)
start = (-w + offset, w - offset)
color_center = (0, 0)

def distance_from_start(point):
    x, y, _ = point
    return ((color_center[0]-x)**2 + (color_center[1]-y)**2)**0.5

def num_digits(num):
    n_digits = 0
    while num > 0:
        num //= 10
        n_digits += 1
    return n_digits

NUM_SQUARES_DIGITS = num_digits(NUM_SQUARES)

def carpet(size, level=0, pos=None):
    if pos is None:
        pos = start
    sub_size = size / 3
    if level <= 0:
        return [(pos[0], pos[1], size)]
    x, y = pos
    locations = []
    for i in range(3):
        for j in range(3):
            if not (i == 1 and j == 1): # Leave center empty
                npos = (x+j*sub_size, y-i*sub_size)
                loc = carpet(sub_size, level-1, npos)
                if loc:
                    locations.extend(loc)
    return locations

def main():
    global current_square
    t.teleport(*start)
    locations = carpet(SIZE, LEVELS)
    locations.sort(key=distance_from_start) 
    for current_square, pos in enumerate(locations):
        x, y, s = pos
        t.teleport(x, y)
        percent = current_square / NUM_SQUARES
        color = plt.colors.to_rgb(colormap(1-percent))
        t.color(color)
        t.shapesize(s, s) 
        t.stamp()

if __name__ == "__main__":
    t.screen.title("Sierpiński Carpet in color")
    i = 1/2   
    square = ((-i, i), (i, i), (i, -i), (-i, -i))
    t.screen.register_shape('cell', square)
    t.shape('cell')
    t.penup()
    t.speed(0)
    main()
    t.screen.mainloop()
