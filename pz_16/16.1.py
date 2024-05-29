# Создайте класс «Круг», который имеет атрибут радиуса и методы для вычисления
# площади, длины окружности и диаметра
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

    def diameter(self):
        return 2 * self.radius

radius = 6

circle = Circle(radius)

print("Площадь круга:", circle.area())
print("Длина окружности:", circle.circumference())
print("Диаметр круга:", circle.diameter())