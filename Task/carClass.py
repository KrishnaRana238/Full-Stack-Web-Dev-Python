# Problem 2 : Car Class with DEfault Values

#Problem
# Create a Car class tha has attrivutes:   Company_name model, and year.
# The constuctor should allow default values
# if none are provided. Create a few car object using different set of arguments


class Car:
    def __init__(self, Company_name, model, year):
        self.Company_name = Company_name
        self.model = model
        self.year = year
    def display(self):
        return f"Company Name: {self.Company_name}, Model: {self.model}, Year: {self.year}"
        
cardetails = Car("Toyota", "Corolla", 2020)
print(cardetails.display())