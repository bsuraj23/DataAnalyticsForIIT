# Instance Variable vs Static Variable
class Student:
    school = "MET"
    def __init__(self, name):
        self.name = name

s1 = Student("Alice")
s2 = Student("Bob")                 
# print(s1.name)        # Instance variable
# s1.name = "Charlie"  # Modifying instance variable for s1
# print(s2.name)        # Instance variable  
# print(Student.school) # Static variable
# print(s1.school)     # Accessing static variable via instance   

Student.school = "class using  School"  # This creates an instance variable for s1     

print(s1.name)
print(s1.school)     # Accessing static variable via instance
print(s2.name)
print(s2.school)     # Accessing static variable via instance   

# s2.school = "s2  School"

# print(s2.school)     # Accessing static variable via instance