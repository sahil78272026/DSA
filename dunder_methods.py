# getting signature of each dunder mnethod belongs to an object

import inspect

# Example class
class MyClass:
    def __init__(self, x):
        self.x = x
    
    def __str__(self):
        return f"MyClass instance with x={self.x}"
    
    def __eq__(self, other):
        return self.x == other.x

# Example object
obj = MyClass(42)

def add(num, name='Sahil', **kwargs):
    var1 = 10
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Test the function with keyword arguments
add(5)  # Output: 5, Sahil
add(10, name='John', age=25)  # Output: 10, John, age: 25

def sub(var):
    print(var)

# print("attributes and methods of a function ", dir(add))
print("add.__dict__ : ", add.__dict__)
print("add.__dir__(): ",add.__dir__())
print("add.__closure__: ",add.__closure__)
print("type(add) : ",type(add))
print("add.__code__: ", add.__code__)
print("add.__doc__ : ", add.__doc__)
print("add.__hash__() : ", add.__hash__())
print("add.__module__: ", add.__module__)
print("add.__name__ : ", add.__name__)
print("add.__reduce__ : ", add.__reduce__) # cannot pickle 'function' object
print("add.__subclasshook__():" , add.__subclasshook__())
print("add.__init__() : " , add.__init__())
print("add.__get__(sub) : " , add.__get__(sub))
print("add.__kwdefaults__ : " , add.__kwdefaults__) # add.__kwdefaults__() , 'NoneType' object is not callable
print("obj.__sizeof__() : ", obj.__sizeof__())

# List of dunder methods you want to inspect
dunder_methods = [
    '__init__',
    '__str__',
    '__eq__',
    # Add more dunder methods here if needed
]
new_dunder_methods = dir(obj)
# print("attributes and methods of MyClass object :",new_dunder_methods)

# Inspect the signature of each dunder method
for method_name in new_dunder_methods:
    try:
        method = getattr(MyClass, method_name)
    except:
        pass
    try:
        signature = inspect.signature(method)
    except:
        signature = None
    # print(f"Signature of {method_name}: {signature}")