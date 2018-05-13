#Создать класс Rectangle, конструктор которого принимает длину и ширину.
#Класс должен иметь два метода, вычисляющие площадь и периметр прямоугольника.

class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def calculation_perimeter(self):
        perimeter = self.width*2+self.height*2
        print("Периметр прямоугольника: {}".format(perimeter))
    def calculation_area(self):
        area = self.width*self.height
        print("Площадь прямоугольника: {}".format(area))

new_rectangle = Rectangle(4, 3)
new_rectangle.calculation_perimeter()
new_rectangle.calculation_area()
