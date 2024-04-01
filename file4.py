class Test:
    def __init__(self):
        self.name = "sahil"
        self.age = 32


t1 = Test()
print(t1.name)

print(getattr(t1, 'name')) # euqivalent to t1.name
print(vars(t1)) # will give a dictionary which contains all the variables and value of objects in key value pair form.