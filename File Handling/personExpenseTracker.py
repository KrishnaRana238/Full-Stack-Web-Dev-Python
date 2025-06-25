# # Build a python based Personal Expense Tracker with file Storage 
# #with Includes features 
# # Add new expenses(data, category, description, amount)
# # View all expenses

# #Search/filter expenses by category or date
# # Store data in a CSV file for persistence

# # Project Structure:
# # - personExpenseTracker.py Main Script
# # - expenses.csv    File Where expenses are stored



# import csv
# import os

# os.chdir("File Handling")
# print(os.getcwd())


# # data = input("Enter the date (YYYY-MM-DD): ")
# # category = input("Enter the category: ")
# # description = input("Enter the description: ")
# # amount = input("Enter the amount: ")

# # file_obj = open("expenses.csv", "a")
# # file_obj.write(f"{data},{category},{description},{amount}\n")
# # file_obj.close()

# # file_obj = open("expenses.csv", "r")
# # content = file_obj.read()
# # print("Current Expenses:")
# # print(content)





# # file = open("expenses.csv", "w")
# # file.writelines("Date,Category,Description,Amount\n")
# # file.writelines("2025-6-20,Food,Food in hostel,200\n")
# # file.close()






# file_obj = open("expenses.csv", "r")
# lines = file_obj.readlines()
# file_obj.close()

# print("📋 Current Expenses:")
# for line in lines:
#     print(line.strip())


# search_category = input("\nSearch by 'category' or 'date': ").strip().lower()
# keyword = input("Enter value to search: ").strip().lower()

# print(f"\n🔍 Expenses matching {search_category} = '{keyword}':")
# found = False


# for line in lines[1:]:
#     parts = line.strip().split(',')
#     if len(parts) < 4:
#         continue

#     date, cat, desc, amt = parts

#     if (search_category == "category" and cat.lower() == keyword) or \
#        (search_category == "date" and date == keyword):
#         print(f"Date: {date}, Category: {cat}, Description: {desc}, Amount: ₹{amt}")
#         found = True

# if not found:
#     print("No matching expenses found.")
    
    
# def add_expense():   



import os
from datetime import datetime

FILENAME = "expenses.csv"
def initialize_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w") as file:
            file.write("Date,Category,Description,Amount\n")
            

def add_expense():
    date = input("Enter the date (YYYY-MM-DD) or leave blank for today: ").strip()
    if not date:
        date = datetime.today().strftime("%Y-%m-%d")
        
    category = input("Enter the category: ").strip()
    description = input("Enter the description: ").strip()
    amount = input("Enter the amount: ").strip()
    
    try:
        float(amount)  # Validate amount is a number
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
        return
    
    line = f"{date},{category},{description},{amount}\n"
    with open(FILENAME, "a") as file:
        file.write(line)
    print("✅ Expense added successfully.")

    
def view_expenses():
    try:
        with open(FILENAME, "r") as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 4:
                    print("{:<12} {:<15} {:<30} rs{:>7}".format(*parts))
    except FileNotFoundError:
        print("No expenses found. Please add some expenses first.")


def search_expenses():
    if not os.path.exists(FILENAME):
        print("No expenses found. Please add some expenses first.")
        return

    choice = input("Search by (1) Date or (2) Category:")
    keyword = input("Enter the value to search: ").strip().lower()
    
    found = False
    
    with open(FILENAME, "r") as file:
        next(file)  # Skip header
        for line in file:
            parts = line.strip().split(',')
            if len(parts) < 4:
                continue
            
            date, category, description, amount = parts
            
            if (choice == "1" and date == keyword) or (choice == "2" and category.lower() == keyword):
                print("{:<12} {:<15} {:<30} rs{:>7}".format(date, category, description, amount))
                found = True
    
    if not found:
        print(f"No expenses found for {keyword} in {('date' if choice == '1' else 'category')} search.")


def main():
    initialize_file()
    
    while True:
        print("\n📊 Personal Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search Expenses")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            search_expenses()
        elif choice == "4":
            print("Exiting the tracker. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
if __name__ == "__main__":
    main()
    
    