# descriptors.py
class Verbose_attribute:

    def __get__(self, obj, type=None):
        print("accessing the attribute to get the value")
        print(repr(obj))
        return 42
    
    def __set__(self, obj, value):
        print("accessing the attribute to set the value")
        raise AttributeError("Cannot change the value")

class Foo():
    attribute1 = Verbose_attribute()

my_foo_object = Foo()
x = my_foo_object.attribute1  # when using dot(.) on an object, __get__() method gets called
print(x)

'''
Descriptors in Python are objects that define how attribute access is handled. They allow you to customize the behavior of attribute access, assignment, and deletion for an object. Descriptors are typically used to implement properties, methods, class attributes, and other attribute-related functionality.

A descriptor must implement one or more of the following methods:

__get__(self, instance, owner): Called when the attribute is accessed.
__set__(self, instance, value): Called when the attribute is assigned a value.
__delete__(self, instance): Called when the attribute is deleted.
'''


class Descriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]

class MyClass:
    descriptor = Descriptor("descriptor")

    def __init__(self, data):
        self.data = data

obj = MyClass(42)

print(obj.data)  # Output: 42
print(obj.descriptor)  # Output: None

obj.descriptor = "Hello"
print(obj.descriptor)  # Output: Hello

del obj.descriptor
print(obj.descriptor)  # Output: None


'''In this example:

We define a Descriptor class that implements the descriptor protocol by defining __get__(), __set__(), and __delete__() methods.
The Descriptor class takes the name of the attribute as an argument during initialization.
In the __get__() method, we return the value of the attribute stored in the instance's __dict__.
In the __set__() method, we set the value of the attribute in the instance's __dict__.
In the __delete__() method, we delete the attribute from the instance's __dict__.
We use the Descriptor class to create a descriptor named descriptor in the MyClass class.
We create an instance of MyClass and demonstrate accessing, setting, and deleting both regular attribute (data) and descriptor attribute (descriptor).

In Python, when a descriptor's __get__() method is called, the owner parameter refers to the class that owns the descriptor. This parameter represents the class where the descriptor is defined, also known as the owner class.

Here's a breakdown of the parameters in the __get__() method:

self: The instance of the descriptor itself.
instance: The instance of the object on which the attribute access is being performed. This parameter is None if the attribute access is performed on the class itself, rather than an instance.
owner: The class that owns the descriptor. This parameter is the class where the descriptor is defined.
The owner parameter is useful when implementing descriptors that need access to the owning class or its attributes during attribute access. It allows descriptors to customize their behavior based on the class where they are defined.

'''