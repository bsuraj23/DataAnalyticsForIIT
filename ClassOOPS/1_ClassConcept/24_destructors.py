# Destructors
class Test:
    def __init__(self):
        print("Constructor called")

    def __del__(self):
        print("Destructor called")
    
t = Test()
del t

# Destructor will also be called automatically when the object goes out of scope or program ends