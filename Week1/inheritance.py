#inheritance

#Single Inheritance
#Multilevel Inheritance
#Multiple Inheritance
#Hierarchical Inheritance
#Hybrid Inheritance


# class Animal:
#     def speak(self):
#         print("Animal Bhokega")
        
# class Dog(Animal):
#     def speak(self):
#         super().speak()
#         print("Mujhe Kutta bolta hai tu ?")
        
# d1 = Dog()
# d1.speak()
#  # Inherited method from Animal class


# class Aninal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print(self.name)
#         print(self.age)
        
    
#     def speak(self):
#         print("Animal speaks")
        
# class Dog(Aninal):
#     def __init__(self, name, age, breed):
#         super().__init__(name, age)  # Call the constructor of the parent class
#         self.breed = breed
#         print(self.breed)
        
#     def speak(self):
#         super().speak()  # Call the speak method of the parent class
#         print("Dog barks")
        
# d1 = Dog("Buddy", 3, "Golden Retriever")
# d1.speak()  # Call the speak method of the Dog class



# #multiple inheritance
# class Animal:
#     def __init__ (self,name,age):
#         self.name = name
#         self.age = age
#         print(self.name)
#         print(self.age)
    
#     def speak(self):
#         print("Animal speaks")
        
# class Dog(Animal):
#     def __init__ (self, name, age, breed):
#         super().__init__(name,age)
        
#         self.breed = breed
#         print(self.breed)
        
#     def speak(self):
#         super().speak()
#         print("Dog barks")
                
# class Cat(Dog):
#     def __init__ (self, name, age, breed, color):
#         super().__init__(name,age,breed)
#         self.color = color
#         print(self.color)
                        
#     def speak(self):
#         super().speak()
#         print("Cat meows")
                            
# d1 = Dog("Buddy", 3, "Golden Retriever")
# d1.speak()  

# d2 = Cat("Whiskers", 2, "Siamese", "Brown")
# d2.speak()  
                            
                            
#multiple inheritance

# class Animal:
#     def __init__(self):
#         print("dog")
    
#     def speak(self):
#         print("Animal speaks")

# class Dog:
#     def __init__(self):
#         print("Cat")
        
#     def speak(self):
        
#         print("Dog barks")
        
# class Main(Animal, Dog):
#     def __init__(self):
#         Animal.__init__(self)
#         Dog.__init__(self)
        
#     def speak(self):
#         Animal.speak(self)
#         Dog.speak(self)
        
# match = Main()
# match.speak()  # Call the speak method of the Main class, which calls both 


#heirarchical inheritance

# class Animal:
#     def __init__(self, name):
#         self.name = name
    
#     def speak(self):
#         print(f"{self.name} makes a sound")
        
# class Dog(Animal):
#     def speak(self):
#         print(f"{self.name} barks")
        
# class Cat(Animal):
#     def speak(self):
#         print(f"{self.name} meows")

# class Bird(Animal):
#     def speak(self):
#         print(f"{self.name} chirps")    

# d= Dog("Buddy")
# d.speak()  # Output: Buddy barks
# c = Cat("Whiskers")
# c.speak()  # Output: Whiskers meows
# b = Bird("Tweety")
# b.speak()  # Output: Tweety chirps






#hybrid inheritance
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks")
class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows")
class Bird(Animal):