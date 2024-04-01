class Test:
    def __init__(self):
        self.name = "sahil"
        self.age = 32

    def foo(self):
        print("in foo method")

    # if a class or object contains __call__ method, then that object is callable
    # this object was not callable but by adding __call__ method, made this a callable object
    # now we can call object and this __call__ function will get executed
    def __call__(self):
        print("Making it callable")


t1 = Test()

def myfunc():
    print("separate func")


print(t1.name)
print(getattr(t1, 'name')) # euqivalent to t1.name
print(vars(t1)) # will give a dictionary which contains all the variables and value of objects in key value pair form.
print(t1.__dict__) # will give a dictionary which contains all the variables and value of objects in key value pair form.

print(t1.__dict__)

print(hasattr(t1, 'name')) # True, checks if an object has the 'provided' variable or not, returns boolean
print(hasattr(t1, 'age'))  # True, checks if an object has the 'provided' variable or not, returns boolean
print(hasattr(t1,'mobile')) # False, checks if an object has the 'provided' variable or not, returns boolean
print(hasattr(t1, "__dict__"))
print(callable(t1))
print(dir(t1))
t1()
print(dir(myfunc))
print(callable(myfunc))

print(t1.__class__())
print(t1.__class__)


# By default, objects are not callable but functions are