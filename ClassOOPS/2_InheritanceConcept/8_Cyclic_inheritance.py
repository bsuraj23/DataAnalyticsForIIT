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


#TODO :  show error of cyclic inheritance
#obj = A()  
#obj.funcA()
#obj.funcB()    
#obj1 = B()  
#obj1.funcA()
#obj1.funcB()
# --- IGNORE ---
# --- IGNORE ---
#obj = A()
#obj.funcA()
#obj.funcB()
#obj1 = B()
#obj1.funcA()
#obj1.funcB()
# --- IGNORE ---
# --- IGNORE ---

