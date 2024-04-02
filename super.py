class Parent:
  def __init__(self, txt):
    self.message = txt

  def printmessage(self, msg):
    print(msg)
    print("calling Parent class method")

  def show(self):
    print(self.message)

class Child(Parent):
  def __init__(self, txt):
    super(Child, self).printmessage("hello") # Child is Subclass and self is the object of current class, same as super().printmessage("hello")

  

x = Child("Hello, and welcome!")
