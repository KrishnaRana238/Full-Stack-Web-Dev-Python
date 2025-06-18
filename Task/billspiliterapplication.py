#your application is bill splitter application write the function that takes the total bill amount and numnber of people and return how much each person share bill 
total_amount = float(input("Enter the total bill amount: "))
num_people = int(input("Enter the number of people to split the bill: "))
def split_bill(total_amount, num_people):
    
    if num_people <= 0:
        return "Number of people must be greater than zero."
    share = total_amount / num_people
    return share
print("Each One of you should pay", split_bill(total_amount,num_people))  # Example usage, should return 25.0
