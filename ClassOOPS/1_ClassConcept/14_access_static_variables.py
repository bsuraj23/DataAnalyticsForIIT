# How to access Static Variables
class Student:
    city = "Hyderabad"
print(Student.city)

#TODO:
# Try to access static variable using object reference.
# Student obj = Student()   
# print(obj.city)  # Accessing static variable via instance
# obj.city = "New City"  # This creates an instance variable for obj
# print(obj.city)  # Accessing instance variable
# print(Student.city)  # Static variable remains unchanged