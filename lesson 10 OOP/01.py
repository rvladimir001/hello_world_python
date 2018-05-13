#Создать класс Circle, конструктор которого принимает радиус.
#Класс должен иметь два метода, вычисляющие площадь и длину окружности.
#Пример вызова класса:
#NewCircle = Circle(8)
#print(NewCircle.area())
#print(NewCircle.perimeter())

import math
class Circle():
    def __init__(self):
        self.radius = 0
    def get_radius(self, r):
        self.radius = r
        print(self.radius)
    def area(self):
        s = (math.pi*self.radius)**2
        print("Площадь окружности: {}".format(s))
    def perimeter(self):
        p = 2*math.pi*self.radius
        print("Длина окружности: {}".format(p))
new_circle = Circle()
new_circle.get_radius(3)
new_circle.area()   
new_circle.perimeter()
