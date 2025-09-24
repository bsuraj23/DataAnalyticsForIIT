# Self Variable

#TODO complete this example with more explanations
#and multiple objects


class Student:
    i=90
    def show(self,j):
        print("self refers to:", self)
     
print(Student.i)
s = Student()

#TODO explaination of self variable
#and add exmaples with multiple objects
print("object s refers to:", s)
s.show()

s.show()

s2 = Student()
s2.show()
s2.j = 200
s2.show()   
