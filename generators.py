def gen():
    for i in range(10):
        yield i


obj = gen()
atts = dir(obj)
print(atts)
for i in atts:
    if callable(i):
        print(f"{i} is a method")
    else:
        print(f"{i} is a variable")

print(obj.__next__())
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())