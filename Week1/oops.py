# what is opps? how it is diffrent from pop and functional programming?
# Object-Oriented Programming (OOP) is a programming paradigm that uses "objects" to represent data and methods to manipulate that data. OOP is based on several key concepts, including encapsulation, inheritance, polymorphism, and abstraction. where pop is a method used in data structures like lists and dictionaries to remove and return an element, and functional programming is a paradigm that treats computation as the evaluation of mathematical functions and avoids changing state or mutable data.




# what are the other similar approaches present in market similar to OOPs ?
# There are several programming paradigms similar to Object-Oriented Programming (OOP) that are prevalent in the market. Some of these include:
# 1. **Functional Programming (FP)**: Emphasizes the use of functions and immutable data. It avoids changing state and mutable data, focusing on the application of functions to arguments.
# 2. **Procedural Programming**: A step-by-step approach that focuses on procedures 
# 3. **Event-Driven Programming**: Centers around the concept of events and event handlers, where the flow of the program is determined by events such as user actions or messages from other programs.
# 4. **Declarative Programming**: Focuses on what the program should accomplish without specifying how to achieve it. It includes languages like SQL and HTML.
# 5. **Aspect-Oriented Programming (AOP)**: Aims to increase modularity by allowing the separation of cross-cutting concerns, such as logging or security, from the main business logic.
# 6. **Logic Programming**: Based on formal logic, where programs are expressed in terms of relations, and computation is triggered by running queries over these relations. Prolog is a well-known logic programming language.
 



# When the OOPs eveolve in the market and why?
# Object-Oriented Programming (OOP) emerged in the 1960s and 1970s, with its roots in earlier programming concepts. The first OOP language, Simula, was developed in the 1960s by Ole-Johan Dahl and Kristen Nygaard. However, OOP gained significant popularity in the 1980s with the introduction of languages like Smalltalk and C++. The paradigm became widely adopted in the 1990s with the rise of languages such as Java, C#, and Python, which incorporated OOP principles into their design. OOP's focus on modularity, code reuse, and abstraction made it a powerful approach for managing complex software systems, leading to its continued relevance in modern software development.



# why python approach only OOPS and is there any other approach in python that it supports?
# Python is primarily an object-oriented programming (OOP) language, but it also supports other programming paradigms, including procedural and functional programming. The OOP approach in Python allows developers to create classes and objects, encapsulating data and behavior together, which promotes code reuse and modularity.
# Python's flexibility enables developers to choose the paradigm that best suits their needs, whether it's OOP for building complex systems, procedural for straightforward scripts, or functional for data processing tasks. This versatility is one of Python's strengths, making it a popular choice for a wide range of applications, from web development to data science and machine learning.



#grocery shopping list manager
#you want to create grocery shopping system using the list#
# you are going to shoping but some item you forgot
# add remove and view items in the list

#
class Dog:
    bread = "Labrador"  # Class variable shared by all instances
    
    def __init__(self, name, age):
        print("dog class")
        self.name = name  # Instance variable unique to each instance   
        self.age = age    # Instance variable unique to each instance
        
    def bark(self):
        print("Dogs are barkiing")
        
d1 = Dog("Buddy", 3)
d2 = Dog("Max", 5)
d1.bark()
d2.bark()

print(d1.name)
print(d2.name)
print(d1.age)
print(d2.age)
print(d1.bread)  # Accessing class variable
print(d2.bread)  # Accessing class variable 