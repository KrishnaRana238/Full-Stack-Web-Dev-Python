# polymorphis in python

# Built in functiom
# USer Defined Function 
# Operators
# oops


class Animal:
    def sound(self):
        print("Animal makes a sound")
class Dog(Animal):
    def sound(self):
        print("Dog barks")
class Cat(Animal):
    def sound(self):
        print("Cat meows")        
        
def make_sound(animal):
    animal.sound()  # This will call the appropriate sound method based on the object type

d1 = Dog()
c1 = Cat()
a1 = Animal()
d1.make_sound()  # This will call the Dog's sound method
c1.make_sound()  # This will call the Cat's sound method
a1.make_sound()  # This will call the Animal's sound method

    
    
animal = [Animal(), Dog(), Cat()]
for a in animal:
    a.sound()  # This will call the appropriate sound method based on the object type 


