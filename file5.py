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

# List of dunder methods you want to inspect
dunder_methods = [
    '__init__',
    '__str__',
    '__eq__',
    # Add more dunder methods here if needed
]
new_dunder_methods = dir(obj)
print(new_dunder_methods)

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
    print(f"Signature of {method_name}: {signature}")