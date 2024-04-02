# dog.py

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

d1 = Dog('sahil',32)
d2 = Dog('Himanshu', 25)

print(d1.name)
print(d1.species)
d1.species = "New Species"
print(d1.species)
print(d2.name)
print(d2.species)
d2.species = "d2 speies"
Dog.species = "Second Species"
print(d1.species)
print(d2.species)
print(Dog.species)
