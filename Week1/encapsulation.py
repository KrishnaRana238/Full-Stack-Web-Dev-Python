#encapsulation 


#__privatevariable
#protectedcvariable

#normal class into encupsulated class

class Employee:
    cname = "Data Zip"
   
    
    
    
    
    def __init__(self, name,age,salary):
        self.name = name # public 
        self._age = age. #protected
        self.__salary = salary #private
    
    def display(self):
        print(self.__salary)


e2 = Employee("John Doe", 30, 60000)
e2.display() 
# print(e2.__salary)


class update(Employee):
    def display_data(self):
        print(self._age)

e3 = update("Jane Doe", 28, 70000)
e3.display_data()  # Accessing protected variable from subclass
    