class Animal:
    def __init__(self):
        print("Animal Constructor")

class Dog(Animal):
    def __init__(self):
        
        print("Dog Constructor")

    def add(self, a, b):    
        print("i am add function with 2 arguments",a+b)

d = Dog()
d.add(12,3)
obj2 = Dog()
obj2.add(45,5)

ani = Animal()
