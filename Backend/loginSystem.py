import mysql.connector 
import bcrypt

# ✅ Use correct MySQL password
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="login4321",
    database="loginapp"
)

mycursor = con.cursor()
print("✅ Connected to MySQL")

# ✅ Run this only once to create the table (then comment it out)
# mycursor.execute("""
# CREATE TABLE IF NOT EXISTS users (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     username VARCHAR(100) UNIQUE NOT NULL,
#     password VARCHAR(255) NOT NULL
# )
# """)
# print("✅ Table 'users' created")

def sign_up(username, password):
    hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    try:
        mycursor.execute("INSERT INTO users(username, password) VALUES (%s, %s)", (username, hashed_pw))
        con.commit()
        print("✅ User registered successfully")
    except mysql.connector.IntegrityError:
        print("❌ User already registered! Try a different one.")

def login(username, password):
    mycursor.execute("SELECT password FROM users WHERE username = %s", (username,))
    result = mycursor.fetchone()
    if result:
        stored_hash = result[0].encode('utf-8')
        if bcrypt.checkpw(password.encode('utf-8'), stored_hash):
            print("✅ Login successful")
        else:
            print("❌ Incorrect password")
    else:
        print("❌ Username not found")

def main():
    while True:
        print("\n------- Login System -------")
        print("1. Sign Up")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            u = input("Username: ")
            p = input("Password: ")
            sign_up(u, p)
        elif choice == "2":
            u = input("Username: ")
            p = input("Password: ")
            login(u, p)
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice, try again!")

if __name__ == "__main__":
    main()
