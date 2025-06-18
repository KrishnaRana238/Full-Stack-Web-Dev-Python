elif account_balance - withdrawal_amount < minimum_balance:
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