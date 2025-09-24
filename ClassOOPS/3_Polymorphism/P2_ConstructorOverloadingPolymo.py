#code for constructor  overloading polymorphism concept

class MathOperations:
    def __init__(self, *args):
        if len(args) == 0:
            self.a = 0
            self.b = 0
            self.c = 0
            print("No arguments constructor called")
        elif len(args) == 1:
            self.a = args[0]
            self.b = 0
            self.c = 0
            print("One argument constructor called")
        elif len(args) == 2:
            self.a = args[0]
            self.b = args[1]
            self.c = 0
            print("Two arguments constructor called")
        elif len(args) == 3:
            self.a = args[0]
            self.b = args[1]
            self.c = args[2]
            print("Three arguments constructor called")
        else:
            self.a = args[0] if len(args) > 0 else 0
            self.b = args[1] if len(args) > 1 else 0
            self.c = args[2] if len(args) > 2 else 0
            print("Variable Length arguments constructor called")


  
# Creating objects with different number of arguments
math_ops1 = MathOperations(5, 10)        # Two arguments
math_ops2 = MathOperations(5, 10, 15)    # Three arguments  
math_ops3 = MathOperations(5)            # One argument
math_ops4 = MathOperations()              # No arguments
#variable length arguments
math_ops5 = MathOperations(5, 10, 15, 20) #Four arguments
math_ops6 = MathOperations(5, 10, 15, 20, 25) #Five arguments
math_ops7 = MathOperations(5, 10, 15, 20, 25, 30) #Six arguments
math_ops8 = MathOperations(5, 10, 15, 20, 25, 30, 35) #Seven arguments 



print(math_ops1.add())  # two arguments
print(math_ops2.add())  # three arguments
print(math_ops3.add())  # one argument

print(math_ops4.add())  # no arguments
