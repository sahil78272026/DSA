class Dog:
    species = "Canis familiaris"

    # We cannot define more than one __init__() method in a class, as python does not support method overloading.
    # if we do so, the last one will be retained.
    # In this case, second __init__() method will be considered.

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    
    def self_check(self):
        print(self.address)
    
class Cat(Dog):
    def cat_func(self):
        print(self.name)
        print(self.age)
        print(self.address)
        self.self_check()
        # print(dir(self))

# d1 = Dog('sahil',32)
# d2 = Dog('Himanshu', 25)
cat = Cat("dinesh", 35, "Delhi")
print(cat.age)
cat.cat_func()
cat.self_check()
print(type(cat))
# print(d1.name)
# print(d1.species)
# d1.species = "New Species"
# print(d1.species)
# print(d2.name)
# print(d2.species)
# d2.species = "d2 speies"
# Dog.species = "Second Species"
# print(d1.species)
# print(d2.species)
# print(Dog.species)


class Animal:
    class_att = 10
    def name(self):
        self.obj_att = 20
        print("name function")

    def __call__(self):
        print("call method")

a = Animal()
m = a.__getattribute__('name')
m()

print(a.__dict__)
print(Animal.__dict__)