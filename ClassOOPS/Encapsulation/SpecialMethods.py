class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person Name: {self.name}"

p = Person("John")
print(p)


#same like string in Java to over ride the per define string and have our own 