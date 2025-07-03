import mysql.connector
from datetime import datetime

# Step 1: Connect to MySQL and create database
con_temp = mysql.connector.connect(
    host="localhost",
    user="root",
    password="login4321",
    port=3306
)
cursor_temp = con_temp.cursor()
cursor_temp.execute("CREATE DATABASE IF NOT EXISTS order_management")
con_temp.close()

# Step 2: Connect to the database
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="login4321",
    database="order_management",
    port=3306
)
cursor = con.cursor()

# Step 3: Create tables if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    product_name VARCHAR(100),
    quantity INT,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
)
""")

# ✅ Add customer manually
def add_customer():
    name = input("Customer Name: ")
    email = input("Email: ")
    try:
        cursor.execute("INSERT INTO customers (name, email) VALUES (%s, %s)", (name, email))
        con.commit()
        print("✅ Customer added.\n")
    except mysql.connector.IntegrityError:
        print("❌ Email already exists.\n")

# ✅ Add order manually with safe input
def add_order():
    cursor.execute("SELECT id, name FROM customers")
    customers = cursor.fetchall()

    if not customers:
        print("⚠️ No customers found. Add a customer first.\n")
        return

    print("\n🧾 Customers List:")
    for c in customers:
        print(f"{c[0]}: {c[1]}")

    try:
        customer_id = int(input("Enter Customer ID: "))
    except ValueError:
        print("❌ Invalid ID. Please enter a number.\n")
        return

    cursor.execute("SELECT id FROM customers WHERE id = %s", (customer_id,))
    if not cursor.fetchone():
        print("❌ Customer ID not found.\n")
        return

    product_name = input("Product Name: ")
    try:
        quantity = int(input("Quantity: "))
    except ValueError:
        print("❌ Quantity must be a number.\n")
        return

    order_date = datetime.today().date()

    cursor.execute("""
        INSERT INTO orders (customer_id, product_name, quantity, order_date)
        VALUES (%s, %s, %s, %s)
    """, (customer_id, product_name, quantity, order_date))
    con.commit()
    print("✅ Order placed.\n")

# ✅ Show all orders with customer info
def show_all_orders_with_customers():
    print("\n📦 Orders with Customer Details:\n")
    cursor.execute("""
        SELECT orders.id, customers.name, customers.email, orders.product_name, orders.quantity, orders.order_date
        FROM orders
        JOIN customers ON orders.customer_id = customers.id
    """)
    rows = cursor.fetchall()
    if not rows:
        print("⚠️ No orders found.\n")
        return
    for row in rows:
        print(f"Order ID: {row[0]} | Customer: {row[1]} | Email: {row[2]} | Product: {row[3]} | Qty: {row[4]} | Date: {row[5]}")
    print()

# ✅ Show customers without orders
def show_customers_without_orders():
    print("🧍 Customers with No Orders:\n")
    cursor.execute("""
        SELECT name, email FROM customers
        WHERE id NOT IN (SELECT DISTINCT customer_id FROM orders)
    """)
    rows = cursor.fetchall()
    if not rows:
        print("🎉 All customers have placed orders.\n")
    else:
        for row in rows:
            print(f"Name: {row[0]} | Email: {row[1]}")
    print()

# ✅ Total orders per customer
def total_orders_per_customer():
    print("📊 Total Orders Per Customer:\n")
    cursor.execute("""
        SELECT customers.name, COUNT(orders.id) AS total_orders
        FROM customers
        LEFT JOIN orders ON customers.id = orders.customer_id
        GROUP BY customers.id
    """)
    rows = cursor.fetchall()
    for row in rows:
        print(f"Customer: {row[0]} | Total Orders: {row[1]}")
    print()

# ✅ Menu loop
def main():
    while True:
        print("\n===== Customer Orders Menu =====")
        print("1. Add Customer")
        print("2. Add Order")
        print("3. Show All Orders with Customer Info")
        print("4. Show Customers Without Orders")
        print("5. Show Total Orders Per Customer")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_customer()
        elif choice == "2":
            add_order()
        elif choice == "3":
            show_all_orders_with_customers()
        elif choice == "4":
            show_customers_without_orders()
        elif choice == "5":
            total_orders_per_customer()
        elif choice == "6":
            print("👋 Exiting program.")
            break
        else:
            print("❌ Invalid input. Please choose 1-6.")

# ✅ Run the main program
if __name__ == "__main__":
    main()
    con.close()
