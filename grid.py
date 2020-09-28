from polyline import Polyline, Point
from graphics import *

class Grid:
    
    def __init__(self, x_size: int, y_size: int):
        if y_size<4 or x_size<4:
            raise ValueError("Grids must be at least 6x6 in size") 
        
        self.x_size = x_size
        self.y_size = y_size
        self.x_max = 0
        self.y_max = 0
        self.phrase = ""
        self.win = None
        self.ineligible_points = []

        self.letter_codes = {
            "A": "UURDLRD",
            "B": "UURDLRDLR",
            "C": "UURLDDR",
            "D": "URUDDLR",
            "E": "UURLDRLDR",
            "F": "UURLDRLDR",
            "G": "UURLDDRUlrD",
            "H": "UUDRUDD",
            "I": "UUDD",
            "J": "UDRUULRDD",
            "K": "E",
            "L": "UUDD",
            "M": "UURDDUURDD",
            "N": "UURDD",
            "O": "UURDDLR",
            "P": "UURDLDR",
            "Q": "RUULDRD",
            "R": "UURLDDR",
            "S": "RULURLDRD",
            "T": "UUlrrlDD",
            "U": "UUDDRUUDD",
            "V": "UUDDRUUDD",
            "W": "UUDDRUUDDRUUDD",
            "X": "E",
            "Y": "RUUDLUDRD",
            "Z": "E",
            " ": "R",
        }

    def verify_drawing(self, x_origin: int, y_origin: int) -> bool:
        for point in self.cursor.get_points():
            if point.x > self.x_size or point.y > self.y_size:
                return False
        for x in range(x_origin, self.x_max + 1):
            for y in range(y_origin, self.y_max + 1):
                for point in self.ineligible_points:
                    if point.x == x or point.y == y:
                        return False
        return True

    def get_max_x(self):
        maxX = 0
        for point in self.cursor.get_points():
            if point.x > maxX:
                maxX = point.x
        return maxX
    
    def get_max_y(self):
        maxY = 0
        for point in self.cursor.get_points():
            if point.y > maxY:
                maxY = point.y
        return maxY

    def get_max_cords(self):
        print(f"Max: [{self.get_max_x()},{self.get_max_y()}]")
        return self.get_max_x(), self.get_max_y() 
        
    def draw_letter(self, letter: str):
        if len(letter) > 1:
            raise ValueError("draw_letter only accepts one char at a time")
        for command in self.letter_codes[letter]:
            if command == "L":
                self.cursor.go_left()
            elif command == "R":
                self.cursor.go_right()
            elif command == "U":
                self.cursor.go_up()
            elif command == "D":
                self.cursor.go_down()
            if command == "l":
                self.cursor.go_halfway_left()
            if command == "r":
                self.cursor.go_halfway_right()
            if command == "u":
                self.cursor.go_halfway_up()
            if command == "d":
                self.cursor.go_halfway_down()
            if command == "E":
                raise ValueError("Cannot print K, X, Y")

    def draw_phrase(self, phrase: str, x: int, y: int):
        self.cursor = Polyline(x,y)
        self.phrase = phrase.upper()
        for letter in self.phrase[:-1]:
            self.draw_letter(letter)
            if letter is not " ":
                self.cursor.go_right()
        self.draw_letter(self.phrase[-1])

    def render(self, phrase: str):
        self.draw_phrase(phrase, 0, 0)
        self.x_max, self.y_max = self.get_max_cords()
        for x in range(self.x_size - self.x_max + 1):
            for y in range(self.y_size - self.y_max + 1):
                self.draw_phrase(phrase, x, y)
                successful_drawing = self.verify_drawing(x,y)
                if successful_drawing:
                    return
        raise ValueError("Drawing cannot fit onto the grid") 

    def add_ineligible_point(self, x: int, y: int):
        self.ineligible_points.append(Point(x,y))

    def setup_graphic(self, scale: int):
        self.win = GraphWin("Road Art", 4*scale*len(self.phrase), 7*scale)
        self.win.yUp()

    def display_graphic(self, scale: int):
        point_list = self.cursor.get_points()
        for i in range(len(point_list)-1):
            ln = Line( Point(point_list[i].x*scale, point_list[i].y*scale), Point(point_list[i+1].x*scale, point_list[i+1].y*scale))
            ln.setWidth(4)
            ln.draw(self.win)

    def display_eligible_points(self, scale: int):
        for x in range(self.x_size):
            for y in range(self.y_size):
                cir = Circle(Point(x*scale, y*scale), 2)
                cir.setOutline('green')
                cir.setFill('green')
                cir.draw(self.win)

    def display_ineligible_points(self, scale: int):
        for point in self.ineligible_points:
            cir = Circle(Point(point.x*scale, point.y*scale), 8)
            cir.setOutline('red')
            cir.setFill('red')
            cir.draw(self.win)
    
    def render_graphic(self):
        self.win.getMouse()
        self.win.close()

    

    def __str__(self):
        return str(self.cursor)



if __name__ == "__main__":
    g = Grid(40,7)

    # g.add_ineligible_point(0,0)
    g.render("Hello Github")

    g.setup_graphic(40)
    g.display_graphic(40)
    g.display_ineligible_points(40)
    g.display_eligible_points(40)
    g.render_graphic()
    

    
    
    
    
