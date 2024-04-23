'''
The Open/Closed Principle (OCP) is the second principle in the SOLID design principles. It states that software entities (classes, modules, functions, etc.) should be open for extension but closed for modification. In other words, you should be able to extend the behavior of a module without modifying its source code.
'''


#not following open closed principle
class Shape:
    def __init__(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

r = Rectangle(10,20)
c = Circle(20)

# everytime we add new shape, we need to modify AreaCalculator class.
class AreaCalculator:
    def calculate_area(self, shape):
        if isinstance(shape, Rectangle):
            return shape.width * shape.height
        elif isinstance(shape, Circle):
            return 3.14 * shape.radius ** 2
        

rec = AreaCalculator().calculate_area(r)
print(rec)
area = AreaCalculator().calculate_area(c)
print(area)




# following open close principle
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class AreaCalculator:
    def calculate_area(self, shape):
        return shape.area()

r = Rectangle(20,40)
a = AreaCalculator().calculate_area(r)
print(a)