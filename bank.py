import json
import os


class BankAccount:

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be greater than zero.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    def check_balance(self):
        print(f"\nCurrent Balance: ₹{self.balance:.2f}")

    def save_account(self):
        data = {
            "name": self.name,
            "balance": self.balance
        }
        with open("account.json", "w") as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def load_account():
        # If we already have saved account data, load it
        if os.path.exists("account.json"):
            with open("account.json", "r") as file:
                data = json.load(file)
            return BankAccount(data["name"], data["balance"])
        else:
            # Otherwise, this must be a new user — let's set them up
            name = input("Enter Account Holder Name: ")
            return BankAccount(name)


account = BankAccount.load_account()

while True:
    print("\n====== MINI BANKING SYSTEM ======")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)

    elif choice == "3":
        account.check_balance()

    elif choice == "4":
        account.save_account()
        print("Account data saved successfully.")
        print("Thank you for using our banking system!")
        break

    else:
        print("Invalid choice. Please try again.")