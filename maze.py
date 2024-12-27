from shapes import Cell, Line, Point
import time
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        if seed != None:
            random.seed(seed)
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
    
    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)
    
    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + self._cell_size_x * i
        x2 = x1 + self._cell_size_x
        y1 = self._y1 + self._cell_size_y * j
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()
    
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.01)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)
    
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            if i != len(self._cells) - 1:
                if self._cells[i+1][j].visited == False:
                    to_visit.append((i+1, j))
            if i != 0:
                if self._cells[i-1][j].visited == False:
                    to_visit.append((i-1,j))
            if j != len(self._cells[i]) - 1:
                if self._cells[i][j+1].visited == False:
                    to_visit.append((i, j+1))
            if j != 0:
                if self._cells[i][j-1].visited == False:
                    to_visit.append((i, j-1))
            if to_visit == []:
                self._draw_cell(i,j)
                return
            new_cell = to_visit[random.randrange(0,len(to_visit))]
            if new_cell == (i, j+1):
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j+1].has_top_wall = False
            if new_cell == (i, j-1):
                self._cells[i][j].has_top_wall = False
                self._cells[i][j-1].has_bottom_wall = False
            if new_cell == (i+1, j):
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False
            if new_cell == (i-1, j):
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False
            self._break_walls_r(new_cell[0],new_cell[1])

    def _reset_cells_visited(self):
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._cells[i][j].visited = False

    def _solve(self):
        return self._solve_r(0, 0)
    
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == len(self._cells) - 1 and j == len(self._cells[i]) - 1:
            return True
        # moving right
        if i != len(self._cells) - 1:
            if self._cells[i+1][j].visited == False and self._cells[i+1][j].has_left_wall is False:
                self._cells[i][j].draw_move(self._cells[i+1][j])
                if self._solve_r(i+1, j) is True:
                    print("moving right")
                    return True
                self._cells[i][j].draw_move(self._cells[i+1][j], True)
        # moving down
        if j != len(self._cells[i]) - 1:
            if self._cells[i][j+1].visited == False and self._cells[i][j+1].has_top_wall is False:
                self._cells[i][j].draw_move(self._cells[i][j+1])
                if self._solve_r(i, j+1) is True:
                    return True
                self._cells[i][j].draw_move(self._cells[i][j+1], True)
        # moving left
        if i != 0:
            if self._cells[i-1][j].visited == False and self._cells[i-1][j].has_right_wall is False:
                self._cells[i][j].draw_move(self._cells[i-1][j])
                if self._solve_r(i - 1, j) is True:
                    return True
                self._cells[i][j].draw_move(self._cells[i-1][j], True)
        # mowing up
        if j != len(self._cells[i]) - 1:
            if self._cells[i][j+1].visited == False and self._cells[i][j+1].has_top_wall is False:
                self._cells[i][j].draw_move(self._cells[i][j+1])
                if self._solve_r(i, j+1) is True:
                    return True
                self._cells[i][j].draw_move(self._cells[i][j+1], True)
        # moving up
        if j != 0:
            if self._cells[i][j- 1].visited == False and self._cells[i][j-1].has_bottom_wall is False:
                self._cells[i][j].draw_move(self._cells[i][j-1])
                if self._solve_r(i, j-1) is True:
                    return True
                self._cells[i][j].draw_move(self._cells[i][j-1], True)
        return False

        


    

        

            




            
           


        
            
    
                

