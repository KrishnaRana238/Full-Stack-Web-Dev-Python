import mysql.connector
import getpass
import datetime

# Step 1: Ensure database exists
con_temp = mysql.connector.connect(
    host="localhost",
    user="root",
    password="login4321",
    port=3306
)
cursor_temp = con_temp.cursor()
cursor_temp.execute("CREATE DATABASE IF NOT EXISTS user1")
con_temp.close()

# Step 2: Connect to the 'user1' database
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="login4321",
    database="user1",
    port=3306
)
cursor = con.cursor()

# Step 3: Create the 'users' table (including password column)
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    gender ENUM('Male', 'Female', 'Other') NOT NULL,
    dob DATE NOT NULL,
    phone VARCHAR(15) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")
print("✅ Table 'users' in database 'user1' is ready!\n")

# Register user
def register_user():
    print("\n--- Register User ---")
    username = input("Username: ")
    email = input("Email: ")
    gender = input("Gender (Male/Female/Other): ")
    dob_input = input("Date of Birth (YYYY-MM-DD): ")
    phone = input("Phone Number: ")
    password = getpass.getpass("Password: ")

    try:
        dob = datetime.datetime.strptime(dob_input, "%Y-%m-%d").date()
    except ValueError:
        print("❌ Invalid date format. Please use YYYY-MM-DD.\n")
        return

    if gender not in ["Male", "Female", "Other"]:
        print("❌ Invalid gender. Must be Male, Female, or Other.\n")
        return

    try:
        cursor.execute("""
            INSERT INTO users (username, email, gender, dob, phone, password)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (username, email, gender, dob, phone, password))
        con.commit()
        print("✅ Account created successfully!\n")
    except mysql.connector.IntegrityError as err:
        print(f"❌ Error: {err.msg}\n")

# Login user
def login_user():
    print("\n--- User Login ---")
    username = input("Username: ")
    password = getpass.getpass("Password: ")

    cursor.execute("""
        SELECT * FROM users WHERE username = %s AND password = %s
    """, (username, password))
    user = cursor.fetchone()

    if user:
        print(f"✅ Welcome back, {user[1]}!\n")
    else:
        print("❌ Invalid username or password.\n")

# Show all users with passwords
def show_users():
    cursor.execute("SELECT id, username, email, gender, dob, phone, password, created_at FROM users")
    users = cursor.fetchall()

    if not users:
        print("📭 No users found.\n")
        return

    print("\n--- All Registered Users ---")
    for u in users:
        print(f"""
ID: {u[0]}
Username: {u[1]}
Email: {u[2]}
Gender: {u[3]}
DOB: {u[4]}
Phone: {u[5]}
Password: {u[6]}
Created At: {u[7]}
------------------------------""")

# Main menu
while True:
    print("======== MENU ========")
    print("1. Create Account")
    print("2. Login")
    print("3. Show All Users")
    print("4. Exit")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        register_user()
    elif choice == '2':
        login_user()
    elif choice == '3':
        show_users()
    elif choice == '4':
        print("👋 Exiting... Goodbye!")
        break
    else:
        print("❌ Invalid choice. Please enter 1, 2, 3, or 4.\n")

# Close connection
con.close()
