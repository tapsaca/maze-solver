from graphics import Line, Point, Window

class Cell:
    def __init__(self, window: Window = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = None
        self.__y1 = None
        self.__x2 = None
        self.__y2 = None
        self.__window = window
    
    def __cell_center(self):
        x_center = self.__x1 + (abs(self.__x2 - self.__x1) // 2)
        y_center = self.__y1 + (abs(self.__y2 - self.__y1) // 2)
        return Point(x_center, y_center)
    
    def draw(self, x1: int, y1: int, x2: int, y2: int):
        if self.__window is None:
            return
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        if self.has_left_wall:
            line = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
            self.__window.draw_line(line)
        else:
            line = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
            self.__window.draw_line(line, "white")
        if self.has_right_wall:
            line = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
            self.__window.draw_line(line)
        else:
            line = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
            self.__window.draw_line(line, "white")
        if self.has_top_wall:
            line = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
            self.__window.draw_line(line)
        else:
            line = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
            self.__window.draw_line(line, "white")
        if self.has_bottom_wall:
            line = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
            self.__window.draw_line(line)
        else:
            line = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
            self.__window.draw_line(line, "white")
    
    def draw_move(self, to_cell, undo=False):
        path = Line(self.__cell_center(), to_cell.__cell_center())
        fill_color = "red"
        if undo:
            fill_color = "gray"
        self.__window.draw_line(path, fill_color)