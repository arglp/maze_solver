from tkinter import Tk, BOTH, Canvas

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=2
        )

class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self.visited = False

    def draw(self, x1, y1, x2, y2, fill_color="black"):
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        line1 = Line(Point(x1, y1), Point(x1, y2))
        line2 = Line(Point(x1, y1), Point(x2, y1))
        line3 = Line(Point(x2, y1), Point(x2, y2))
        line4 = Line(Point(x1, y2), Point(x2, y2))
        if self.has_left_wall:
            color = "black"
        else:
            color = "white"
        self._win.draw_line(line1, color)
        if self.has_top_wall:
            color = "black"
        else:
            color = "white"
        self._win.draw_line(line2, color)
        if self.has_right_wall:
            color = "black"
        else:
            color = "white"
        self._win.draw_line(line3, color)
        if self.has_bottom_wall:
            color = "black"
        else:
            color = "white"
        self._win.draw_line(line4, color)

    def draw_move(self, to_cell, undo=False):
        half_length = abs(self._x2 - self._x1) // 2
        x_center = half_length + self._x1
        y_center = half_length + self._y1

        half_length2 = abs(to_cell._x2 - to_cell._x1) // 2
        x_center2 = half_length2 + to_cell._x1
        y_center2 = half_length2 + to_cell._y1

        fill_color = "red"
        if undo:
            fill_color = "gray"

        line = Line(Point(x_center, y_center), Point(x_center2, y_center2))
        self._win.draw_line(line, fill_color)