import mysql.connector
from datetime import date

# Step 1: Connect to MySQL and create database
con_temp = mysql.connector.connect(
    host="localhost",
    user="root",
    password="login4321",  # Use your MySQL root password
    port=3306
)
cursor_temp = con_temp.cursor()
cursor_temp.execute("CREATE DATABASE IF NOT EXISTS store_inventory")
con_temp.close()

# Step 2: Connect to the new database
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="login4321",
    database="store_inventory",
    port=3306
)
cursor = con.cursor()

# Step 3: Create product table
cursor.execute("""
CREATE TABLE IF NOT EXISTS product (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL,
    created_at DATE
)
""")
print("✅ Table 'product' is ready.\n")

# Function: Insert product
def insert_product():
    name = input("Product name: ")
    description = input("Description: ")
    price = float(input("Price: "))
    stock = int(input("Initial stock: "))
    today = date.today()

    cursor.execute("""
        INSERT INTO product (name, description, price, stock, created_at)
        VALUES (%s, %s, %s, %s, %s)
    """, (name, description, price, stock, today))
    con.commit()
    print("✅ Product added successfully.\n")

# Function: Update stock after sale
def update_stock():
    product_id = int(input("Enter Product ID: "))
    sold_quantity = int(input("Enter quantity sold: "))

    cursor.execute("SELECT stock FROM product WHERE id = %s", (product_id,))
    result = cursor.fetchone()

    if not result:
        print("❌ Product not found.\n")
        return

    current_stock = result[0]
    if sold_quantity > current_stock:
        print("❌ Not enough stock.\n")
        return

    new_stock = current_stock - sold_quantity
    cursor.execute("UPDATE product SET stock = %s WHERE id = %s", (new_stock, product_id))
    con.commit()
    print("✅ Stock updated successfully.\n")

# Function: View products with low stock
def view_low_stock():
    threshold = 5
    cursor.execute("SELECT id, name, stock FROM product WHERE stock < %s", (threshold,))
    rows = cursor.fetchall()

    if not rows:
        print("🎉 All products have sufficient stock.\n")
        return

    print("\n⚠️ Products with Low Stock:")
    for row in rows:
        print(f"ID: {row[0]} | Name: {row[1]} | Stock: {row[2]}")
    print()

# Function: View all products
def view_all_products():
    cursor.execute("SELECT * FROM product")
    rows = cursor.fetchall()

    if not rows:
        print("📦 No products in inventory.\n")
        return

    print("\n📋 All Products:")
    for row in rows:
        print(f"""
ID: {row[0]}
Name: {row[1]}
Description: {row[2]}
Price: ₹{row[3]}
Stock: {row[4]}
Created At: {row[5]}
-------------------------""")

# Main menu
def main():
    while True:
        print("====== Inventory Menu ======")
        print("1. Insert New Product")
        print("2. Update Stock After Sale")
        print("3. View Low Stock Products")
        print("4. View All Products")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            insert_product()
        elif choice == "2":
            update_stock()
        elif choice == "3":
            view_low_stock()
        elif choice == "4":
            view_all_products()
        elif choice == "5":
            print("👋 Exiting Inventory System.")
            break
        else:
            print("❌ Invalid option. Please try again.\n")

# Run program
if __name__ == "__main__":
    main()

# Close DB connection at the end
con.close()
