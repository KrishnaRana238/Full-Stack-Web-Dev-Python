

# Problem 3: Student information System
#problem:
# Create a class student with the following attriubutes: name, roll_number and grade
# Use a constructor to initialize these values
# Create two student objects with display after their information

class Student:
    def __init__(self, name, roll_number, grade):
        self.name = name
        self.roll_number = roll_number
        self.grade = grade

    def display(self):
        print(f"Company Name: {self.name}, Model: {self.roll_number}, Year: {self.grade}")
    
student1 = Student("John Doe", "101", "A")
student1.display()
    
     
    