class Demo:
    @classmethod
    def show(cls):
        print("Class method called")

Demo.show()


#ADD examples when to use class method and when to use static method
class Utility:
    @staticmethod
    def add(a, b):
        return a + b    

    @classmethod
    def info(cls):
        return "Utility class for basic operations" 

print(Utility.add(5, 10))          # Static method call
print(Utility.info())              # Class method call          
print(Utility.info())              # Class method call
# Static method is used for operations that don't need class or instance data
# Class method is used for operations related to the class itself