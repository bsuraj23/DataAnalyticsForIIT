# Constructor Concept


#comment this class is demo for constructor concept
#static variableclass NewClass:
    """ this is demo class for constructor concept"""
    
    a2=67
    def __init__(self):
        print("i am getting executed class NewClass constructor")
        self.a
        self.b
    
    
    def add(self):
        print("inside add method")
        return 45+45

obj1 = NewClass()
print(obj1.add())
print("document for this class is ",obj1.__doc__)

obj2 = NewClass()

class Student:
    static_var = 90  #static 
    __var = 78   #private variable
    _var2 = 67  #protected variable
    var4= 89  #public variable
    def __init__(self, name):
        self.name = name
        print("i am getting executed class Student constructor")
        self.b=78

    
    def add(self):
        return 9+6

vijay = Student("Vijay")
print(Student.static_var)
Student.static_var =67
print(vijay.static_var)
print(vijay.b)  #78
Alice = Student("Alice")
print(Alice.static_var)  #67
Alice.b=34   
print(Alice.b)  # 34
print(Alice.add())

print(vijay.b)  #78

Ajayobj = Student("Ajay")


print(Ajayobj.a)
print(Ajayobj.add())



class Person:
    name = "name"
    age = 14
    def sleep(self):
        print("sleeping executed ")

    

personObj1 = Person()
personObj1.name ="ajay"
personObj1.age = 24
print(personObj1.age)
# print(personObj1.sleep())

personObj2 = Person()
personObj2.name = "aman"
personObj2.age = 34
print(personObj2.age)
# print(personObj2.sleep())

# print(personObj2.age)
print(personObj2.sleep())


