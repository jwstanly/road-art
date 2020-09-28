from typing import List

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"[{self.x},{self.y}]"

class Polyline:
    def __init__(self, startingX: int, startingY: int):
        self.points = []
        self.points.append(Point(startingX, startingY))

    def go_left(self):
        current_point = self.points[-1]
        self.points.append(Point(current_point.x - 2, current_point.y))

    def go_right(self):
        current_point = self.points[-1]
        self.points.append(Point(current_point.x + 2, current_point.y))

    def go_up(self):
        current_point = self.points[-1]
        self.points.append(Point(current_point.x, current_point.y + 2))

    def go_down(self):
        current_point = self.points[-1]
        self.points.append(Point(current_point.x, current_point.y - 2))

    def go_halfway_left(self):
        current_point = self.points[-1]
        self.points.append(Point(current_point.x - 1, current_point.y))

    def go_halfway_right(self):
        current_point = self.points[-1]
        self.points.append(Point(current_point.x + 1, current_point.y))

    def go__halfway_up(self):
        current_point = self.points[-1]
        self.points.append(Point(current_point.x, current_point.y + 1))

    def go_halfway_down(self):
        current_point = self.points[-1]
        self.points.append(Point(current_point.x, current_point.y - 1))

    def get_points(self) -> List[Point]:
        return self.points
    
    def get_latest_point(self):
        return self.points[-1]

    def __str__(self) -> str:
        result = ""
        for point in self.points:
            result += str(point) + "\n"
        return result