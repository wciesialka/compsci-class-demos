import tkinter
from enum import Flag, Enum, auto
from itertools import product
from random import Random
from math import sqrt, floor
from io import BytesIO
from PIL import Image

BORDER_OFFSET = 2 # Pixels to offset drawing from the canvas edge

CANVAS_BASE_SIZE_PX = 600
# Adjust the actual canvas size to include space for the border on all sides
CANVAS_SIZE_PX = CANVAS_BASE_SIZE_PX + (2 * BORDER_OFFSET)
WIDTH_PX = CANVAS_SIZE_PX
HEIGHT_PX = CANVAS_SIZE_PX

MAZE_SIZE = 2**12

WALL_LENGTH = CANVAS_BASE_SIZE_PX // sqrt(MAZE_SIZE)

class CellType(Enum):
    NORMAL = auto()
    TERMINAL = auto()
    
class Direction(Flag):
    NORTH = auto()
    EAST = auto()
    SOUTH = auto()
    WEST = auto()

class Cell:

    def __init__(self, x, y = None):
        self.__walls = Direction.NORTH | Direction.EAST | Direction.SOUTH | Direction.WEST
        self.__visited = False
        if y is None:
            y = x[1]
            x = x[0]
        self.__pos = (x, y)
        self.__type = CellType.NORMAL

    @property
    def visited(self):
        return self.__visited

    @property
    def ctype(self):
        return self.__type

    @ctype.setter
    def ctype(self, new_type):
        if not isinstance(new_type, CellType):
            raise TypeError("New CellType must be of type CellType, not {new_type.__class__.__name__}")
        self.__type = new_type

    def is_visited(self):
        return self.visited

    def visit(self):
        self.__visited = True

    @property
    def pos(self):
        return self.__pos

    @property
    def x(self):
        return self.pos[0]

    @property
    def y(self):
        return self.pos[1]

    @property
    def walls(self):
        return self.__walls

    def add_wall(self, wall: Direction):
        if not isinstance(wall, Direction):
            raise TypeError(f"Added wall must be of type Direction, not {wall.__class__.__name__}")
        if wall in self.walls:
            raise ValueError(f"Added wall {wall} already in cell.")
        self.__walls |= wall

    def remove_wall(self, wall: Direction):
        if not isinstance(wall, Direction):
            raise TypeError(f"Removed wall must be of type Direction, not {wall.__class__.__name__}")
        if not wall in self.walls:
            raise ValueError(f"Removed wall {wall} not in cell.")
        self.__walls &= (~wall)

    def direction_to(self, other: "Cell"):
        if not isinstance(other, Cell):
            raise TypeError(f"other must be of type Cell, not {other.__class__.__name__}")
        if self.x > other.x:
            return Direction.WEST
        elif self.x < other.x:
            return Direction.EAST
        elif self.y > other.y:
            return Direction.NORTH
        elif self.y < other.y:
            return Direction.SOUTH
        return None

    def has_wall(self, wall: Direction):
        if not isinstance(wall, Direction):
            raise TypeError(f"wall must be of type Direction, not {wall.__class__.__name__}")
        return wall in self.walls

    def draw(self, canvas):
        wx = self.x * WALL_LENGTH # West X
        ex = wx + WALL_LENGTH # East X
        ny = self.y * WALL_LENGTH # North Y
        sy = ny + WALL_LENGTH # South Y

        wx += BORDER_OFFSET
        ex += BORDER_OFFSET
        ny += BORDER_OFFSET
        sy += BORDER_OFFSET

        if self.ctype == CellType.TERMINAL:
            canvas.create_rectangle(wx, ny, ex, sy, fill='#ddd', width=0)
            
        
        if self.has_wall(Direction.NORTH):
            canvas.create_line(wx, ny, ex, ny)
        if self.has_wall(Direction.EAST):
            canvas.create_line(ex, ny, ex, sy)
        if self.has_wall(Direction.SOUTH):
            canvas.create_line(wx, sy, ex, sy)
        if self.has_wall(Direction.WEST):
            canvas.create_line(wx, ny, wx, sy)


class Maze:

    def __init__(self, size: int):
        if not isinstance(size, int):
            raise TypeError(f"size must be of type int, not type {size.__class__.__name__}")
        if size <= 0:
            raise ValueError(f"size must be >= 0, not {size}")
        self.__size = size
        self.__init_cells()
        self.__random = Random()

    @property
    def size(self):
        return self.__size

    @property
    def random(self):
        return self.__random

    @property
    def width(self):
        return floor(sqrt(self.size))

    @property
    def height(self):
        return floor(sqrt(self.size))

    def __init_cells(self):
        self.__cells = {(x, y): Cell(x, y) for x, y in product(range(self.width), range(self.height))}

    def __getitem__(self, key):
        if key in self.__cells:
            return self.__cells[key]
        raise KeyError(f"Key '{key}' not found")

    def get(self, x, y=None):
        if y is None:
            return self[x]
        return self[(x, y)]

    def get_neighbors(self, x, y=None):
        if y is None:
            return self.get_neighbors(*x)
        neighbors = []
        if x > 0:
            neighbors.append(self.get(x-1, y))
        if x < self.width-1:
            neighbors.append(self.get(x+1, y))
        if y > 0:
            neighbors.append(self.get(x, y-1))
        if y < self.height-1:
            neighbors.append(self.get(x, y+1))
        return tuple(neighbors)

    def get_unvisited_neighbors(self, x, y=None):
        neighbors = self.get_neighbors(x, y)
        filtered = filter(lambda neighbor: not neighbor.visited, neighbors)
        return tuple(filtered)

    def __idfs(self, x, y = None):
        if y is None:
            return self.__idfs(*x)
        starting_cell = self.get(x, y)
        stack = [starting_cell]
        while stack:
            cell = stack[-1]
            
            cell.visit()
            neighbors = self.get_unvisited_neighbors(cell.x, cell.y)
            if len(neighbors) > 0:
                next_cell = self.random.choice(neighbors)

                dir_a = cell.direction_to(next_cell)
                dir_b = next_cell.direction_to(cell)
                cell.remove_wall(dir_a)
                next_cell.remove_wall(dir_b)
                
                stack.append(next_cell)
            else:
                stack.pop()

    def generate(self):
        start = self.random.choice(tuple(self.__cells.keys()))
        self.__idfs(start)
        # Make two random cells the start/end
        for cell in self.random.choices(list(self.__cells.values()), k=2):
            cell.ctype = CellType.TERMINAL

    def draw(self, canvas):
        for cell in self.__cells.values():
            cell.draw(canvas)

def main():
    root = tkinter.Tk("Maze")
    frame = tkinter.Frame(root)
    canvas = tkinter.Canvas(frame, width=WIDTH_PX, height=HEIGHT_PX, bg='#fff')
    
    canvas.pack()
    frame.pack()
        
    maze = Maze(MAZE_SIZE)
    maze.generate()
    maze.draw(canvas)

    root.mainloop()

if __name__ == "__main__":
    main()
