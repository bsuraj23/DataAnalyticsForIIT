#code for inheritance concept
class Sample:
    def func1(self):
        print("This is function 1 from Parent class")   
class Chair(Sample):   #inheriting Parent class
    def func2(self):
        print("This is function 2 from Child class")    
obj = Chair()
obj.func1() #calling parent class function  
obj.func2() #calling child class function
obj1 = Sample()
obj1.func1() #calling parent class function
obj1.func2() #this will give error as parent class object cannot access child class function
#obj1.func2() #this will give error as parent class object cannot access child class function   
