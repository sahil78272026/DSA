# Function based decorator1

def decorator_function(original_function):
    def wrapper_function():
        original_function()

    return wrapper_function

def display():
    print("display function ran")

decorated_display = decorator_function(display) # passing display function, functions are first class object in python
decorated_display()
# decorated_display()


# decorator2
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(args, kwargs)
        original_function(*args, **kwargs)
        return 10

    return wrapper_function


# @decorator_function
def display(name, age):
    print(f"display function ran, {name}, {age}")

decorated_display = decorator_function(display)
return_value = decorated_display('Sahil', 31)
print(return_value)

# display('Sahil', 31)

# *******************************

# class Decorator
class Decorator_class:
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print(f'call method executed this before {self.original_function.__name__}')
        return self.original_function(*args, **kwargs)

# @Decorator_class
def display():
    print("display function ran")

@Decorator_class
def display_info(name, age):
    print(f'display_info function with {name}, {age}')

display = Decorator_class(display)
display()  # object called as function call, invoking __call__ method in Decorator_class, mentioning __call__ method in class, makes the object callable

display_info('sahil',31)



print('*********************************')

def decorator_func(original_func):
    def wrapper_func(*args):
        print("wrapper func")
        original_func(*args)

    return wrapper_func


def existing_func(nums):
    print('existing function')


new_func = decorator_func(existing_func)
new_func(20)

print('*********************************')




def dec_func(func):
    def dec_wrap_func(*args):
        print('dec_wrap_func')
        func(*args)
        return 50

    return dec_wrap_func

@dec_func
def my_func(num):
    print(f'my func {num}')

# my_var = dec_func(my_func)
# var = my_var()
# print(var)

my_func(10)


