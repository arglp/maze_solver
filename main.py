from window import Window
from shapes import Line, Point, Cell
from maze import Maze

def main():
    num_rows = 10
    num_cols = 10
    margin = 30
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    maze._solve()
    
    win.wait_for_close()

if __name__ == "__main__":
    main()