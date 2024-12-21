from window import Window
from shapes import Line, Point

def main():
    win = Window(800, 600)
    win.draw_line(Line(Point(50, 50), Point(750, 50)), "black")
    win.draw_line(Line(Point(50, 50), Point(50, 550)), "black")
    win.draw_line(Line(Point(750, 50), Point(750, 550)), "black")
    win.draw_line(Line(Point(50, 550), Point(750, 550)), "black")
    win.wait_for_close()

if __name__ == "__main__":
    main()