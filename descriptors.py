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
