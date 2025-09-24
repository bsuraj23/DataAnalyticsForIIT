#Passing Members of One Class to Another Class
class A:
    def __init__(self, value):
        self.value = value

class B:
    def __init__(self, obj):
        # Ensure obj is an instance of A
        if not isinstance(obj, A):
            raise TypeError("obj must be an instance of class A")
        self.obj = obj
        obj.value += 10

aobj = A(10)
b = B(aobj)
print(b.obj.value)

def add(a,b):
    print("Inside add method")
    return a+b

add(11,22)
print(add())  # None




