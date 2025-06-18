#Airthmetic (+,-,*,/,%)
#Assignment (=,+=,-=,*=,/=,%=)
#Comparison (==,!=,>,<,>=,<=)
#Logical (and, or, not)
#Bitwise (&, |, ^, ~, <<, >>)
#Identity (is, is not)
#Membership (in, not in)
#Identity Operators
# a = [1, 2, 3]
# b = a
# c = a[:]    # a and b refer to the same list object
# print(a is b)      # True, both refer to the same object    






# a = 10
# b = 5
# print(a + b)  # Output: 15


# print(a - b)  # Output: 5


# print(a * b)  # Output: 50


# print(a / b)  # Output: 2.0


# print(a % b)  # Output: 0

# name = input("Enter your name: ")
# print("Hello, ", name )
# print("Would you like to do some calculations? (yes/no): ")
# response = input()
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# response = input("Enter an operator (+, -, *, /): ")
# print(response)




# Membership operator example with movie ticket vacant Booking system
my_list = [10, 18, 21, 44, 23, 45, 67, 89, 90]

print(12 in my_list)  
print(10 in my_list)  
print(43 not in my_list)  
print(44 not in my_list)  # Output: True


#identity operator example
presciption_booking= {"id ": 1, "name" : "Krishna"}
scan_face = presciption_booking
other_scan = {"id ": 1, "name" : "Aryan"}

print("is they registered for it",presciption_booking is scan_face)
print("is they registered for it",other_scan is presciption_booking)
# Output: True, both refer to the same object



#hotel BIll
dishe1_price = int(input("Enter the price of dish 1: "))
dishe2_price = int(input("Enter the price of dish 2: "))
print("The total price of the dishes is: ", dishe1_price + dishe2_price)
print("Discount on the total price is: ", (dishe1_price + dishe2_price) * 0.10)
print("You want to cancel dish2", dishe1_price-dishe2_price)
print("You want to cancel dish1", dishe2_price-dishe1_price)
print("Total Price After GST is: ", (dishe1_price + dishe2_price) / 20)
print("Total Price", (dishe1_price + dishe2_price) * 0.10 + (dishe1_price + dishe2_price) % 10)


#ELigibility for check
input_num = int(input("Enter a number to check if you elegible: "))
print("Age list is greater that 18: ", input_num >= 18)
print("Age list is less that 18: ", input_num < 18)
print("Age list is equal to 18: ", input_num == 18)
print("Age list is not equal to 18: ", input_num != 18)
print("Age list is greater than or equal to 18: ", input_num >= 18)
print("Age list is less than or equal to 18: ", input_num <= 18)

#Rule of Princidence



# 1. Parentheses ()
# 2. Exponentiation **
# 3. Unary plus and minus +, -
# 4. Multiplication, division, floor division, and modulus *, /, //, %
# 5. Addition and subtraction +, -
# 6. Bitwise shifts <<, >>  
# 7. Bitwise AND &
# 8. Bitwise XOR ^
# 9. Bitwise OR |
# 10. Comparison operators <, <=, >, >=, ==, !=
# 11. Identity operators is, is not 
# 12. Membership operators in, not in
# 13. Logical NOT not
# 14. Logical AND and
# 15. Logical OR or
# 16. Assignment operators =, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, <<=, >>=
# 17. Conditional expressions (ternary operator) x if condition else y
# 18. Comma operator , (used in tuple creation, function arguments, etc.)
# 19. Lambda expressions lambda arguments: expression
# 20. Yield expressions yield expression (used in generator functions)
# 21. Await expressions await expression (used in asynchronous programming)
# 22. Function calls (not an operator, but a common operation) function_name(arguments)


#example of precedence
a = 10
b = 5
c = 2
result = a + b * c  # Multiplication has higher precedence than addition
print(result)  # Output: 20, because b * c is evaluated first (5 * 2 = 10), then added to a (10 + 10 = 20)
#example of precedence with parenthesis
result_with_parentheses = (a + b) * c  # Parentheses change the order
print(result_with_parentheses)  # Output: 30, because (a + b) is evaluated first (10 + 5 = 15), then multiplied by c (15 * 2 = 30)
#example of precedence with exponentiation
result_exponentiation = a ** b  # Exponentiation has higher precedence than addition
print(result_exponentiation)  # Output: 100000, because 10 raised to the power of 5 is 100000
#example of precedence with bitwise operators
result_bitwise = a & b  # Bitwise AND has lower precedence than addition
print(result_bitwise)  # Output: 0, because 10 (1010 in binary) AND 5 (0101 in binary) results in 0 (0000 in binary)
#example of precedence with logical operators
result_logical = a > b and b < c  # Logical AND has lower precedence than comparison operators
print(result_logical)  # Output: False, because a > b is True and b < c is False, so the overall expression is False
#example of precedence with identity    
result_identity = a is not b  # Identity operator has lower precedence than comparison operators   
print(result_identity)  # Output: True, because a (10) is not the same object as b (5)      


#hotel bill example with precedence
dish1_price = int(input("Enter the price of dish 1: "))
dish2_price = int(input("Enter the price of dish 2: "))
total_price = dish1_price + dish2_price
discount = total_price * 0.10
gst = total_price * 0.05  # Assuming GST is 5%
final_price = total_price - discount + gst
print("Total Price Before Discount: ", total_price)
print("Discount on Total Price: ", discount)
print("Total Price After Discount: ", total_price - discount)
print("Total Price After GST: ", total_price + gst)
print("Final Price After Discount and GST: ", final_price)



#example of exponential ** compound interest of future investment
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in %): "))
time = float(input("Enter the time in years: "))
compound_interest = principal * (1 + rate / 100) ** time
print("The compound interest after", time, "years is:", compound_interest)


# example pf multiplication and division of spliting package
packs = 24
boxes = 3
weight_per_box = 2.5

total_weight = packs / boxes * weight_per_box
print(total_weight) 


# example of comparision changing using Exam Result
marks = int(input("Enter your marks: "))
print(0 <= marks < 40)  # Output: True if marks are between 0 and 39
print(40 <= marks < 60)  # Output: True if marks are between 40 and 59
print(60 <= marks < 80)  # Output: True if marks are between 60 and 79
print(80 <= marks < 100)  # Output: True if marks are between 80 and 99

Expression Evaluation

#comparision and logical operators example with account access
age = 21
correct_pin = True

can_access_account = age > 18 and correct_pin
print("Can access account:", can_access_account)  # Output: True if age is
    
   
# exponential and bitwise operators example with power of 2
unit = 3
rate = 8

bill = rate * unit ** 2  # Exponential operator for calculating bill
print("Electricity bill:", bill)  # Output: 72, because 8 *
 
 
#Access control with nested logical operators
username = "user123"
password = "pass123"
is_authenticated = (username == "user123" and password == "pass123") or (username == "admin" and password == "adminpass")
print("Is user authenticated?", is_authenticated)  # Output: True if credentials match either set


#Mobile recharge bonus check Bitwise, logical and comparision operators

recharge_amount = 1000

bonus = recharge_amount & 1 == 0 and recharge_amount >= 100
print("Is bonus applicable?", bonus)  # Output: True if both conditions are met

# Authentication check with identity, logical and comparision operators
logged_in = True
role = "admin"
session_id = "xyz123"

allow_admin = logged_in and role == "admin" and session_id is not None
print("Admin Access:", allow_admin)  # Output: True
