class Temp:

    class_variable = 10

    @staticmethod
    def statmethod():
        print("static method")

    @classmethod
    def clasmethod(cls):
        print("class method", cls)
        cls.class_variable += 1
        # cls is the object of class
   
    def normalmethod(self):
        print("normal method", self)
        # self the instance of class
    

t  = Temp()
t2 = Temp()
print(t.class_variable) # 10
t.normalmethod()
t.clasmethod()  
t.statmethod()
print(t.class_variable) # 11
t.clasmethod()
print(t.class_variable) # 12
print(t2.class_variable)  # 12  # changing state of class variable through @classmethod decorator for every instance