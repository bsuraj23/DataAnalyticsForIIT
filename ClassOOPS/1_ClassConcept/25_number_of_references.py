# How to find the Number of References of an Object
import sys
class Student: pass
s = Student()
a=sys.getrefcount(s)
print(a)
# print(sys.getrefcount(s))

#ADD why 2 because of print function
#one reference is created when we assign object to variable s
#another reference is created when we pass the object to sys.getrefcount()  function
# s1 = s  # Second reference  
# print(sys.getrefcount(s))
# s2 = s  # Third reference   
# print(sys.getrefcount(s))
