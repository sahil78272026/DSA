from abc import ABCMeta, abstractmethod,   abstractstaticmethod, abstractclassmethod

class IPerson(metaclass=ABCMeta):

    @abstractmethod
    def print_data():
        """implement in child class"""


class PersonSingleTon(IPerson):
    __instance = None

    @staticmethod
    def get_instance():
        if PersonSingleTon.__instance==None:
            PersonSingleTon("default name", 0)
        return PersonSingleTon.__instance
    
    def __init__(self,name, age):
        if PersonSingleTon.__instance!=None:
            raise Exception("Singleton cannot be instantiated more than once")
        else:
            self.name = name
            self.age = age
            PersonSingleTon.__instance = self

    @staticmethod
    def print_data():
        print(f"Name:{PersonSingleTon.__instance.name}, Age:{PersonSingleTon.__instance.age}")

p1 = PersonSingleTon("sahil", 32)
print(p1)
# p2 = PersonSingleTon("Himanshu", 25) # Singleton cannot be instantiated more than once
p2=p1
print(p2)
print(p1.name)
print(p2.name)

