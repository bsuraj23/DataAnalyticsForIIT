# What is Object?
# An object is an instance of a class.

class Person:
    pass




    

obj1 = Person()  #creatrion of Object 

class Student:
    pass
student1 = Student()

class Automobile:
    a=90
    tires="tires"   #//2 bytes
    def func():   #// 7 Bytes
        a=90  #// 1byte
        print("")

BMW = Automobile()  # 10 bytes
print(BMW.tires)
BMW.func()
Thar = Automobile()  #10 bytes
print(Thar.a)
print(Thar.tires)

Hummer = Automobile()  #10 bytes
Audi = Automobile()  #10 bytes


