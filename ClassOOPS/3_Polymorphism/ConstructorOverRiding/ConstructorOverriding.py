class Parent:
    a=90
    def __init__(self,a,b):
        print("Parent constructor with 2 arguments")
        c=89+9
        print(c)
    def fun(self, a, b):
        print("i am fun function with 2 arguments")

class Child(Parent):
    def __init__(self):
        # super().__init__(12,3)  #calling parent class constructor from child class
        print("Child constructor with no arguments")
        d=90+9
        print(d)
    

# obj = Child()

objP = Parent(12,3)
objP.fun(12,3)

objC = Child()

#TODO :  show how to call parent constructor from child class
#TODO :  show how to access parent class variable from child class  
# objC.add(45,5)
# print(objC.a)   
