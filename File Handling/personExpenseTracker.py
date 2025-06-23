# Build a python based Personal Expense Tracker with file Storage 
#with Includes features 
# Add new expenses(data, category, description, amount)
# View all expenses

#Search/filter expenses by category or date
# Store data in a CSV file for persistence

# Project Structure:
# - personExpenseTracker.py Main Script
# - expenses.csv    File Where expenses are stored



import csv
import os

os.chdir("File Handling")
print(os.getcwd())


# data = input("Enter the date (YYYY-MM-DD): ")
# category = input("Enter the category: ")
# description = input("Enter the description: ")
# amount = input("Enter the amount: ")

# file_obj = open("expenses.csv", "a")
# file_obj.write(f"{data},{category},{description},{amount}\n")
# file_obj.close()

# file_obj = open("expenses.csv", "r")
# content = file_obj.read()
# print("Current Expenses:")
# print(content)





# file = open("expenses.csv", "w")
# file.writelines("Date,Category,Description,Amount\n")
# file.writelines("2025-6-20,Food,Food in hostel,200\n")
# file.close()






file_obj = open("expenses.csv", "r")
lines = file_obj.readlines()
file_obj.close()

print("📋 Current Expenses:")
for line in lines:
    print(line.strip())


search_category = input("\nSearch by 'category' or 'date': ").strip().lower()
keyword = input("Enter value to search: ").strip().lower()

print(f"\n🔍 Expenses matching {search_category} = '{keyword}':")
found = False


for line in lines[1:]:
    parts = line.strip().split(',')
    if len(parts) < 4:
        continue

    date, cat, desc, amt = parts

    if (search_category == "category" and cat.lower() == keyword) or \
       (search_category == "date" and date == keyword):
        print(f"Date: {date}, Category: {cat}, Description: {desc}, Amount: ₹{amt}")
        found = True

if not found:
    print("No matching expenses found.")
    
    
def add_expense():   