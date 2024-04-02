class Pizza(object):
    def __init__(self):
        self.toppings = []

    def __call__(self, topping):
        # When using '@instance_of_pizza' before a function definition
        # the function gets passed onto 'topping'.
        self.toppings.append(topping())

    def __repr__(self):
        return str(self.toppings)

pizza = Pizza()

@pizza
def cheese():
    return 'cheese'

@pizza
def sauce():
    return 'sauce'

print(pizza)
# ['cheese', 'sauce']

print(dir(pizza))
print("pizza.__class__ : ", pizza.__class__)
print("pizza.__class__() :", pizza.__class__())
print("pizza.__delattr__", pizza.__delattr__)
print("pizza.__delattr__()", pizza.__delattr__)
print("pizza.__dict__", pizza.__dict__)
print("pizza.__dict__()", pizza.__dict__())  # dict object is not callable
print(pizza.__dir__)
print(pizza.__doc__)