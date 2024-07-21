import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def are_circle(self, radius):
        return round(math.pi * (radius * radius), 2)

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def check_triangle(self, a, b, c):
        if a == b + c or b == a + c or c == a + b:
            return True
        return False
    def area_triangle(self, a, b, c):
        p = (a + b + c) / 2
        return round(math.sqrt(p * ((p - a) * (p - b) * (p - c))), 2)

