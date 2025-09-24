#code for constructor over riding  polymorphism concept

#not possible as python does not support constructor overloading last defined constructor will be considered
#thus we can not achieve constructor overloading in python like other languages  Java or C++


class Animal:
    
  
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species
        print("Animal constructor  3 para called")  


 
   

    def ad(self, a, b, c, d):
        print("i am add function with 4 arguments",a+b+c+d)

obj = Animal("Buddy", 5, "Dog")
# obj.ad(12,3)
obj.ad(1,1,1,1) # this will give error as last
# defined function will be considered


   