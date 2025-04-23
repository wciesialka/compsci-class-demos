from turtle import Turtle

t = Turtle()

def polygon(n_sides, side_length):
    sum_angles = (n_sides-2) * 180
    exterior_angle = sum_angles / n_sides
    interior_angle = 180 - exterior_angle
    for _ in range(n_sides):
        t.forward(side_length)
        t.right(interior_angle)

def main():
    polygon(7, 100)

if __name__ == "__main__":
    t.screen.title("Polygon")
    main()
    t.screen.mainloop()
