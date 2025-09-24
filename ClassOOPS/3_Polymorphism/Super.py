class Parent:
    def __init__(self,a):
        print("Parent constructor")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child constructor")

obj = Child()
