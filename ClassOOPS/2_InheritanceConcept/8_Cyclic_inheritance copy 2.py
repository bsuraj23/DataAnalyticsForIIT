#code for cyclic inheritance concept
class A(B): pass
class B(A): pass

#code for cyclic inheritance concept with functions
class A(B):
    def funcA(self):
        print("Function A")
class B(A):
    def funcB(self):
        print("Function B")

#obj = A()  #this will give error as cyclic inheritance is not allowed
#obj1 = B() #this will give error as cyclic inheritance is not allowed ..
#print(A.mro()) #this will give error as cyclic inheritance is not allowed
#print(B.mro()) #this will give error as cyclic inheritance is not allowed

