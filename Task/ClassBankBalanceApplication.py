

class BankBalanceApplication:
    def __init__(self,balance):
        self.__balance = balance
        
    def deposition(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Credited Amount: {amount}", f"Updated Balance: {self.__balance} ")
        else:
            print("Invalid amount. Please enter a positive value.")
            
    def withdrawal(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Debited Amount: {amount}", f"Remaing Balance: {self.__balance} ")
        else:
            print("Invalid amount. Please enter a positive value or check your balance.")    
            
    def display(self):
        print(f"Current Balance: {self.__balance}")
        
Amount = BankBalanceApplication(200000)
Amount.display()
Amount.withdrawal(50000)
Amount.deposition(100000)
Amount.display()