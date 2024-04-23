'''
The Liskov Substitution Principle (LSP) is the third principle in the SOLID design principles. It states that objects of a superclass should be replaceable with objects of its subclasses without affecting the correctness of the program. In other words, a subclass should behave in such a way that it can be substituted for its superclass without altering the desired behavior of the program.
'''

class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Car is moving")

class Bicycle(Vehicle):
    def move(self):
        print("Bicycle is moving")


def travel(vehicle):
    vehicle.move()


car = Car()
bicycle = Bicycle()

travel(car)  # Output: Car is moving
travel(bicycle)  # Output: Bicycle is moving

class Airplane(Vehicle):
    def move(self):
        print("Airplane is flying")

airplane = Airplane()

travel(airplane)  # Output: Airplane is flying

travel(Vehicle())

