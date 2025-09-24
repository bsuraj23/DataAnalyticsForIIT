# Local Variables
g=123  # Global variable
class Test:
    def show(self):


        # print(global[g])  # Accessing global variable
        print(g)
        
        print(globals()['g'])  # Accessing global variable
        x = 10  # Local variable
        print(x)

obj = Test()
obj.show()
print(globals()['g'])  # Accessing global variable



