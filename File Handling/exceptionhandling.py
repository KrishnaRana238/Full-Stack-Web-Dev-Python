# expception handling 
# try, except, else, finally


# Raise Expection
# Custom Exception  
# User-defined Exception

# There are two types of exceptions in Python:
# 1. Built-in exceptions: These are predefined exceptions in Python, such as ValueError, TypeError, etc., File Not Found, ZeroDivisionError, key error etc.
# 2. User-defined exceptions: These are exceptions that you can create yourself by inheriting from the Exception class.


# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     result = a / b
    
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")
# except ValueError:
#     print("Error: Invalid input. Please enter a valid number.")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")
# else:
#     print("The Result is:", result)
# finally:
#     print("Clean UP")

# Riase Custom Exception
# def set_age(age):
#     if age < 0:
#         raise ValueError("Age cannot be negative.")
#     else:
#         print(f"Age is : {age}.")
# try:
#     set_age(-5)
# except ValueError as e:
#     print(f"Validation Error: {e}")

# class validate_age(Exception):
#     def __init__(self, age, message):
#         self.age = age
#         self.message = message
#         super().__init__(self,message)
    
    
    
# import logging
# logging.basicConfig(filename="app.log", level = logging.ERROR, format='%(asctime)s-%(levelname)s-%(message)s')

# def divide(a,b):
#     try:
#         result = a/b
#         logging.info(f"Division successful: {result}")
#         return result
#     except ZeroDivisionError:
#         logging.exception("Number cannot be divided by zero.")
#     except TypeError as e:
#         logging.exception(f"Invalid input type: {e}",exc_info=True)
# divide(10,2)
# divide(10,0)
# divide(10,"a")   




class validate_age(Exception):
    def __init__(self, age, message="Invalid age provided."):
        self.age = age
        self.message = message
        super().__init__(self,message)
def set_age(age):
    if age < 0:
        raise validate_age(age)
    else:
        print(f"Age is : {age}.")
try:
    set_age(-5)
except validate_age as e:
    print(f"Validation Error: {e}")