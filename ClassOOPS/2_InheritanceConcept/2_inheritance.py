import os
os.system('cls')

#code for inheritance concept is a
class A:
    def func1(self):
        print("This is function 1 from class A")    
class B(A):   #inheriting class A
    def func2(self):
        print("This is function 2 from class B")    
class C(B):   #inheriting class B
    def func3(self):
        print("This is function 3 from class C")
objc = C()
objc.func1() #calling class A function   
objc.func2() #calling class B function
objc.func3() #calling class C function
objb = B()
objb.func1() #calling class A function
objb.func2() #calling class B function  
#objb.func3() #this will give error as class B object cannot access class C function

#Has a relationship
class D:
    def func4(self):
        print("This is function 4 from class D")    
class E:
    def func5(self):
        print("This is function 5 from class E")    
class F:

    def __init__(self):
        self.d = D()  #F has a relationship with D
        self.e = E()  #F has a relationship with E
    def func6(self):
        print("This is function 6 from class F")
        self.d.func4() #accessing class D function
        self.e.func5() #accessing class E function

objFF = F()
objFF.func6() #calling class F function
objFF.d.func4() #accessing class D function using class F object
objFF.e.func5() #accessing class E function using class F object


class A:
    def func1(self):
        print("This is function 1 from class A")

class B():   #inheriting class A
    def func2(self):
        print("This is function 2 from class B")
        obj = A()
        obj.func1() #accessing class A function


#TODO how can one class stop question inheriting another class
#TODO how can one class stop question inheriting another class
#TODO add code for generator and decorator in master repo ..github and also in local system