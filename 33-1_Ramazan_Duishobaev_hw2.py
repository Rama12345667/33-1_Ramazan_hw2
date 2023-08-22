import math

class Figure:
    unit = "cm"
    def calculate_area(self):
        pass
    def info(self):
        pass

class Circle(Figure):
    def __init__(self,radius):
        self.__radius = radius
    def calculate_area(self):
        return math.pi * self.__radius ** 2
    def info(self):
        return f"Circle radius: {self.__radius}{self.unit}, area: {self.calculate_area()}{self.unit}"

class RightTriangle(Figure):
    def __init__(self, side_a, side_b):
        self.__side_a = side_a
        self.__side_b = side_b
    def calculate_area(self):
        return 0.5 * self.__side_a * self.__side_b

    def info(self):
        return f"RightTriangle side a: {self.__side_a}{self.unit}, side b: {self.__side_b}{self.unit}, area: {self.calculate_area()}{self.unit}"

figures = [
    Circle(2),
    Circle(3),
    RightTriangle(5, 8),
    RightTriangle(3, 6),
    RightTriangle(4, 7)
]
for f in figures:
    print(f.info())