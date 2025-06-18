# # User details
# account_balance = 15000
# withdrawal_amount = int(input("Enter amount to withdraw: "))
# daily_withdrawal_total = 2000
# daily_limit = 14000
# minimum_balance = 2000
# penalty_fee = 100

# # Smart ATM logic
# if withdrawal_amount <= 0:
#     print(" Invalid amount. Please enter a positive value.")

# elif withdrawal_amount % 100 != 0:
#     print(" Amount must be in multiples of ₹100 or ₹500.")
# elif account_balance - withdrawal_amount < minimum_balance:
#     print(f" Warning: This will reduce your balance below ₹{minimum_balance}.")
#     confirm = input("Do you want to continue with a ₹100 penalty? (yes/no): ").lower()
    
#     if confirm == "yes":
#         total_deduction = withdrawal_amount + penalty_fee
#         if total_deduction <= account_balance:
#             account_balance -= total_deduction
#             print(f" Withdrawal successful with penalty. New balance: ₹{account_balance}")
#         else:
#             print(" You don’t have enough balance to cover penalty.")
#     else:
#         print("ℹ Transaction cancelled by user.")

# elif daily_withdrawal_total + withdrawal_amount > daily_limit:
#     print(" Daily withdrawal limit exceeded. Try a smaller amount.")

# elif withdrawal_amount > account_balance:
#     print(" Insufficient balance.")



# else:
#     account_balance -= withdrawal_amount
#     print(f" Withdrawal successful. New balance: ₹{account_balance}")





# Account details
account_balance = 15000
withdrawal_amount = 0
daily_withdrawal_total = 2000
daily_limit = 14000
minimum_balance = 2000
penalty_fee = 100
correct_pin = "1234"
card_valid = True

print("🏧 Welcome to Smart ATM")

# Step 1: Check if card is valid
if card_valid == False:
    print("❌ ATM card is not valid. Please contact your bank.")

else:
    # Step 2: PIN Verification
    pin = input("🔐 Enter your 4-digit ATM PIN: ")
    if pin != correct_pin:
        print("❌ Incorrect PIN. Access denied.")
    else:
        # Step 3: Ask for withdrawal amount
        try:
            withdrawal_amount = int(input("💵 Enter amount to withdraw: "))
        except:
            print("❌ Invalid amount. Please enter a number.")
            withdrawal_amount = 0

        # Step 4: Process conditions

        if withdrawal_amount <= 0:
            print("❌ Invalid amount. Must be greater than zero.")

        elif withdrawal_amount % 100 != 0:
            print("❌ Amount must be in multiples of ₹100 or ₹500.")

        elif account_balance < withdrawal_amount:
            print("❌ Insufficient balance in your account.")

        elif daily_withdrawal_total + withdrawal_amount > daily_limit:
            print("❌ Daily withdrawal limit exceeded.")

        elif account_balance - withdrawal_amount < minimum_balance:
            print(f"⚠️ Warning: This will reduce your balance below ₹{minimum_balance}.")
            confirm = input("Do you want to continue with ₹100 penalty? (yes/no): ").lower()

            if confirm == "yes":
                total_deduction = withdrawal_amount + penalty_fee

                if total_deduction <= account_balance:
                    account_balance -= total_deduction
                    daily_withdrawal_total += withdrawal_amount
                    print(f"✅ Withdrawal successful with ₹{penalty_fee} penalty.")
                    print(f"💰 New balance: ₹{account_balance}")
                else:
                    print("❌ You don’t have enough balance to cover the penalty.")
            else:
                print("ℹ️ Transaction cancelled by user.")

        else:
            account_balance -= withdrawal_amount
            daily_withdrawal_total += withdrawal_amount
            print("✅ Withdrawal successful.")
            print(f"💰 New balance: ₹{account_balance}")

