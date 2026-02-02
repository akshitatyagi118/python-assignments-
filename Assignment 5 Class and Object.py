
class BankAccount:
    
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:  
            self.balance += amount
            print(f"Amount ₹{amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Amount ₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance or invalid amount.")

    def check_balance(self): 
        print(f"Account Holder: {self.account_holder} | Current Balance: ₹{self.balance}")

# Example usage:
account = BankAccount("John Doe", 5000) 
account.check_balance() 
account.deposit(2000) 
account.withdraw(1500) 
account.check_balance()