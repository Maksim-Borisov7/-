import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area_circle(self, radius): #Вычисление площади круга
        return round(math.pi * (radius ** 2), 2)

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def check_triangle(self, a, b, c): #Проверка на прямоугольный треугольник
        if a ** 2 == b ** 2 + c ** 2 or b ** 2 == a ** 2 + c ** 2 or c ** 2 == a ** 2 + b ** 2:
            return True
        return False
    def area_triangle(self, a, b, c): #Вычисление площади треугольника
        p = (a + b + c) / 2
        return round(math.sqrt(p * ((p - a) * (p - b) * (p - c))), 2)

def test_area_circle(): #Юнит тест на правильность вычисления площади круга
    circle = Circle(radius=5)
    assert circle.area_circle() == 78.54

def test_is_right_triangle(): #Юнит тест на прямоугольный треугольник
    triangle = Triangle(a=3, b=4, c=5)
    assert triangle.check_triangle()
    triangle = Triangle(a=5, b=3, c=4)
    assert triangle.check_triangle()
    triangle = Triangle(a=4, b=5, c=3)
    assert triangle.check_triangle()
    triangle = Triangle(a=3, b=4, c=6)
    assert not triangle.check_triangle()

def test_area_triangle(): #Юнит тест на правильность вычисления площади треугольника
    triangle = Triangle(a=3, b=4, c=5)
    assert triangle.area_triangle() == 6.0
    triangle = Triangle(a=5, b=12, c=13)
    assert triangle.area_triangle() == 30.0
    triangle = Triangle(a=7, b=24, c=25)
    assert triangle.area_triangle() == 84.0

if __name__ == 'main':
    test_area_circle()
    test_is_right_triangle()
    test_area_triangle()

