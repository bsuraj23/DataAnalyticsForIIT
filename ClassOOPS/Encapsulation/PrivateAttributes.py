class Example:
    def __init__(self):
        self.__secret = 50

obj = Example()
print(obj._Example__secret)  # Accessing private attribute


# The following line would raise an AttributeError if uncommented
# print(obj.__secret)  # This will give an error as __secret is private 
# and cannot be accessed directly from outside the class
# However, it can be accessed using name mangling as shown above.
# Name mangling is a mechanism in Python that alters the name of a private attribute
# to include the class name, making it harder to access from outside the class.