# you have to design the simple shop cart that takes  the list of total item price and return the total price including 10% sales tax




# def calculate_total_price(item_price):
#     if item_price < 0:
#         return "Price cannot be negative."
#     sales_tax = 0.10 * item_price
#     total_price = item_price + sales_tax
#     return total_price

# def totalinput():
#     total_items = int(input("Enter the number of items: "))
#     if total_items <= 0:
#         return "Number of items must be greater than zero."
    
#     total_cart_price = 0.0
#     for i in range(total_items):
#         item_name = input(f"Enter the name of item {i + 1}: ")
#         item_price = float(input(f"Enter the price for {item_name}: "))
        
#         result = calculate_total_price(item_price)
       
#         total_cart_price += result  
    
#     return f"The total price for all items including 10% sales tax is: ${total_cart_price:.2f}"


# print(totalinput())




total_item = int(input("Enter total number of items: "))
def Itemlist():
    total = 0
    for i in range(total_item):
        item = int(input(f"Enter the name of item {i + 1}: "))
        total += item
    sales_tax = 0.10 * total
    total_price = total + sales_tax
    return total_price
print("The total price of all items is: ", Itemlist())