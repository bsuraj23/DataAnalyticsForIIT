# How to Delete Static Variables of a Class
class Student:
    school = "ABC School"
del Student.school
# print(Student.school)  # This will raise an AttributeError because the static variable has been deleted
