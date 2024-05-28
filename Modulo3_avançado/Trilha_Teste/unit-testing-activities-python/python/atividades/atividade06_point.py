import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other):
        if not isinstance(other, Point):
            raise ValueError("Argument must be a Point")
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)