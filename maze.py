from shapes import Cell
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()
    
    def _create_cells(self):
        for i in range(self._num_cols):
            col = []
            for j in range(self._num_rows):
                new_cell = Cell(self._win)
                col.append(new_cell)
            self._cells.append(col)
        for k in range(len(self._cells)):
            for l in range(len(self._cells[k])):
                self._draw_cell(k, l)
    
    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + self._cell_size_x * j
        x2 = x1 + self._cell_size_x
        y1 = self._y1 + self._cell_size_y * i
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()
    
    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

        
            
    
                

