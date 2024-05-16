import random
import time
from cell import Cell
from graphics import Window

class Maze:
    def __init__(self, x: int, y: int, num_rows: int, num_cols: int, cell_size_x: int, cell_size_y: int, window: Window = None, seed = None):
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
        if seed:
            random.seed(seed)
        self.__break_walls(0, 0)
        self.__reset_cells_visited()
    
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
    
    def __break_walls(self, i: int, j: int):
        self._cells[i][j].visited = True
        while True:
            next_index_list = []
            # Check adjacent cells for possible directions
            # Left
            if i > 0 and not self._cells[i - 1][j].visited:
                next_index_list.append((i - 1, j))
            # Right
            if i < self.__num_cols - 1 and not self._cells[i + 1][j].visited:
                next_index_list.append((i + 1, j))
            # Top
            if j > 0 and not self._cells[i][j - 1].visited:
                next_index_list.append((i, j - 1))
            # Bottom
            if j < self.__num_rows - 1 and not self._cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))
            # Return if no possible direction is available
            if len(next_index_list) == 0:
                self.__draw_cell(i, j)
                return
            # Pick random direction
            next_index = next_index_list[random.randrange(len(next_index_list))]
            # Break the wall between the current and next cell
            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[next_index[0]][next_index[1]].has_right_wall = False
            elif next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[next_index[0]][next_index[1]].has_left_wall = False
            elif next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[next_index[0]][next_index[1]].has_bottom_wall = False
            elif next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[next_index[0]][next_index[1]].has_top_wall = False
            self.__break_walls(next_index[0], next_index[1])
    
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
    
    def __reset_cells_visited(self):
        for column in self._cells:
            for cell in column:
                cell.visited = False
    
    def solve(self):
        return self.__solve_r(0, 0)

    def __solve_r(self, i: int, j: int):
        self.__animate()
        self._cells[i][j].visited = True
        if i == self.__num_cols - 1 and j == self.__num_rows - 1:
            return True
        # Move to adjacent cell if it has not been visited and there is no wall
        if i > 0 and not self._cells[i - 1][j].visited and not self._cells[i][j].has_left_wall:
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self.__solve_r(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], True)
        if i < self.__num_cols - 1 and not self._cells[i + 1][j].visited and not self._cells[i][j].has_right_wall:
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self.__solve_r(i + 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], True)
        if j > 0 and not self._cells[i][j - 1].visited and not self._cells[i][j].has_top_wall:
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self.__solve_r(i, j - 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], True)
        if j < self.__num_rows - 1 and not self._cells[i][j + 1].visited and not self._cells[i][j].has_bottom_wall:
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self.__solve_r(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], True)
        return False