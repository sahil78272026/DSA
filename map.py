def add(a):
    return a+5

l1 = [1,2,3,4]
l2 = map(add,l1)  # applies function to each value and returns a map object
print(type(l2)) #map
print(list(l2))