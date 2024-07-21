import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def are_circle(self, radius):
        return round(math.pi * (radius ** 2), 2)

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def check_triangle(self, a, b, c):
        if a ** 2 == b ** 2 + c ** 2 or b ** 2 == a ** 2 + c ** 2 or c ** 2 == a ** 2 + b ** 2:
            return True
        return False
    def area_triangle(self, a, b, c):
        p = (a + b + c) / 2
        return round(math.sqrt(p * ((p - a) * (p - b) * (p - c))), 2)

