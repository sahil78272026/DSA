'''def outer_func(param):

    def inner_func():
        print(param)
        return 1
    
    return inner_func


hi_func = outer_func('Hi')
bye_func = outer_func('Bye')

print(hi_func())
bye_func()
'''

# # Function decorator

# def decorator_function(original_function):
#     def wrapper_function():
#         original_function()

#     return wrapper_function

# def display():
#     print("display function ran")

# decorated_display = decorator_function(display) # passing display function, functions are first class object in python
# decorated_display()
# # decorated_display()


# decorator
# def decorator_function(original_function):
#     def wrapper_function(*args, **kwargs):
#         print(args, kwargs)
#         original_function(*args, **kwargs)
#         return 10

#     return wrapper_function

# # @decorator_function
# def display(name, age):
#     print(f"display function ran, {name}, {age}")

# decorated_display = decorator_function(display)
# return_value = decorated_display('Sahil', 31)
# print(return_value)

# # display('Sahil', 31)

#*******************************

# class Decorator
class decorator_class:
    def __init__(self, original_function):
        self.original_function = original_function
    
    def __call__(self, *args, **kwargs):
        print(f'call method executed this before {self.original_function.__name__}')
        return self.original_function(*args, **kwargs)
    
@decorator_class
def display():
    print("display function ran")

@decorator_class
def display_info(name, age):
    print(f'display_info function with {name}, {age}')


display()
display_info('sahil',31)

