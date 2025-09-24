# Various Places to declare Static Variables
class Student:
    school = "ABC School"  # Inside class
    def __init__(self):
        Student.school = "init School"  # Inside constructor
    def set_school(self):
      Student.school = "setting School"  # Inside method
       

obj = Student()
print(obj.school)
obj.set_school()
print(obj.school)

