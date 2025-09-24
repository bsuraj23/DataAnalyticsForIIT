class Animal:
    def add(self,a):
        print("add with no parameter Constructor")
    def add(self,a,b):
        print("add with two parameter",a,b)
class Dog(Animal):
    pass  # No own constructor

d = Dog()

ani = Animal()
# ani.add(23)
ani.add(23,45)