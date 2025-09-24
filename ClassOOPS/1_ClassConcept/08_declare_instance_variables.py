# Where we can declare Instance Variables
#inside constructor
#inside instance method 
#outside the class using object reference variable



class Student:
    """Student class"""
    university = "IITM"  # static variable
    def __init__(self, name):
        self.name = name
    # instance method example of declaring instance variable
    def set_age(self, age):
        self.age = age
    def add(self):
        return self.age + 10



obj = Student("John")
print(obj.__doc__)  # Output: Student clas
obj.set_age(20)
#declaring instance variable outside the class using object reference variable
obj.age=22 
print(obj.name)  # Output: John
print(obj.age)   # Output: 20   


santosh = Student("Santosh")
santosh.set_age(24)

print(santosh.name)  # Output: John
print(santosh.age)   # Output: 24
santosh.add()

print(santosh.name)

obj3 = Student("Sashi")
obj3.set_age(20)


print(obj3.name)  # Output: sashi
print(obj3.age)   # Output: 20


print(obj.__dict__)  # Output: {'name': 'John'}
# print(obj2.__dict__)  # Output: {'name': 'Ajay', 'age': 30}
print(obj3.__dict__)  # Output: {'name': 'Sashi', 'age': 40}

del obj.age  # Deleting instance variable age from obj
# del obj2.age  # Deleting instance variable age from obj2
del obj3.age  # Deleting instance variable age from obj3

del obj

# print(obj.__dict__)  # Output: {'name': 'John'}
# print(obj2.__dict__)  # Output: {'name': 'Ajay', 'age': 30}
# print(obj3.__dict__)  # Output: {'name': 'Sashi', 'age': 40}