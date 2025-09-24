str = "Hello "
str2 = "World"
print(str + str2)
# Here + operator is overloaded to perform addition for Number class and concatenation for string class
print(str * 3)
# Here * operator is overloaded to perform multiplication for Number class and repetition for string class

class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num

n1 = Number(10)
n2 = Number(20)
print(n1 + n2)

