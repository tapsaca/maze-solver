import sys
from graphics import Window
from maze import Maze

def main():
    num_rows = 10
    num_cols = 10
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = 50
    cell_size_y = 50

    sys.setrecursionlimit(10000)
    window = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, window)
    print("Maze created")
    is_solveable = maze.solve()
    if not is_solveable:
        print("Maze can not be solved!")
    else:
        print("Maze solved!")
    window.wait_for_close()

main()