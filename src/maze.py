import time
from cell import Cell
from graphics import Window

class Maze:
    def __init__(self, x: int, y: int, num_rows: int, num_cols: int, cell_size_x: int, cell_size_y: int, window: Window = None):
        self.__x = x
        self.__y = y
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__window = window
        self._cells = []
        self.__create_cells()
        self.__break_entrance_and_exit()
    
    def __animate(self):
        if self.__window is None:
            return
        self.__window.redraw()
        time.sleep(0.05)
    
    def __break_entrance_and_exit(self):
        entrance: Cell = self._cells[0][0]
        entrance.has_top_wall = False
        self.__draw_cell(0, 0)
        exit: Cell = self._cells[self.__num_cols - 1][self.__num_rows - 1]
        exit.has_bottom_wall = False
        self.__draw_cell(self.__num_cols - 1, self.__num_rows - 1)
    
    def __create_cells(self):
        for i in range(self.__num_cols):
            col_cells = []
            for j in range(self.__num_rows):
                col_cells.append(Cell(self.__window))
            self._cells.append(col_cells)
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__draw_cell(i, j)
    
    def __draw_cell(self, i: int, j: int):
        x1 = i * self.__cell_size_x + self.__x
        y1 = j * self.__cell_size_y + self.__y
        x2 = x1 + self.__cell_size_x
        y2 = y1 + self.__cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self.__animate()