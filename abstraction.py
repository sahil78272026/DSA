'''
Abstract Base Classes (ABCs) are a way of defining interfaces or abstract behaviors that concrete subclasses must implement. 
They allow you to define common interfaces without specifying the implementation details, promoting abstraction and ensuring consistency across subclasses.
Here's how you can use ABCs in Python:
1. Defining an Abstract Base Class:
You can define an ABC using the abc module in Python. 
An ABC is a class that inherits from abc.ABC or includes the @abc.abstractmethod decorator on one or more of its methods. 
These abstract methods define the interface that concrete subclasses must implement.
2. Creating Concrete Subclasses:
Concrete subclasses must inherit from the abstract base class and provide implementations for all abstract methods defined in the base class. 
If a subclass fails to implement any abstract method, it will raise a TypeError at runtime.
3. Using Polymorphism:
With ABCs, you can treat instances of different concrete subclasses interchangeably, allowing you to work with them at a higher level of abstraction. 
This promotes polymorphism, where objects of different classes can be used interchangeably if they adhere to a common interface.
In this example, Shape is an abstract base class that defines two abstract methods: area() and perimeter(). 
Concrete subclasses Rectangle and Circle inherit from Shape and provide implementations for these methods. 
By defining a common interface using ABCs, we can treat instances of Rectangle and Circle interchangeably in the print_shape_info() function, promoting abstraction and polymorphism.

'''

import math

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # error , if this method is not defined.TypeError: Can't instantiate abstract class Rectangle with abstract methods area
    # def area(self):
    #     return self.width * self.height
        
    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


def print_shape_info(shape):
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())

rectangle = Rectangle(5, 3)
circle = Circle(4)

print_shape_info(rectangle)
print_shape_info(circle)

'''
If you define a method in an abstract base class (ABC) without the @abstractmethod decorator, it will be treated as a regular method, and subclasses will not be required to implement it. In other words, the method will not be considered abstract, and subclasses can choose whether or not to override it.
'''