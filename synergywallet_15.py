"""INST 326 - FINAL PROJECT
 Team 15 - Robin Godinho, Nikita Naz Kamal
 Synergy Wallet - Mobile Banking App"""

import pandas as pd
import openpyxl
import os

"""
    Parent class: User - witholds personal information of the account holder. Has a function that shows user details
    Args: name, acc_num
    Returns:
"""
class User:
    def __init__(self, name, acc_num):
        self.name = name
        self.acc_num = acc_num
        print(f"\nThank you for choosing Synergy Wallet {self.name}, your account number is {self.acc_num}.\n")

    def show_detials(self):
        print("View BANK STATEMENT")
        print("------------------------------------------")
        print("Account holder: ", self.name)
        print("Account number: ", self.acc_num)

"""
    Child class: Bank - inherits user details from the User class
    Args: name,acc_num, balance, amount
    Returns: balance
"""
class Bank(User):
    def __init__(self, name, acc_num):
        super().__init__(name, acc_num)
        self.balance = 0

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + amount
        print(f"Your current account balance is ${self.balance}\n")

    def transfer(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print(f"Insufficient Funds | Balance available: ${self.balance}.\n\n")
        else:
            self.balance = self.balance - self.amount
            print(f"Your transfer was successful. Your account balance is ${self.balance}\n\np")

    def statement(self):
        self.show_detials()
        print(f"Your bank statement has been updated. Your current balance is ${self.balance}")


if os.path.exists("output.xlsx"):
  os.remove("output.xlsx")

#Get the user's infromation
print("Welcome to Synergy Wallet! Where mobile banking is made easy")
naMe = input("\nPlease enter your name ")
acc_Num = input("\nPlease enter your account number ")

user1 = Bank(naMe, acc_Num)

if __name__ == "__main__":
    while True:
        # Prompt choices
        print("1. Deposit Money")
        print("2. Transfer Money")
        print("3. View Statement")
        print("4. Quit")

        choice = int(input("Enter 1, 2, or 3: "))
        if choice not in [1, 2, 3, 4]:
            print("You entered the wrong option")
            continue

        if choice == 1:
            amount = int(input("How much do you want to deposit? "))
            user1.deposit(amount)
        elif choice == 2:
            amount = int(input("How much do you want to transfer? "))
            user1.transfer(amount)
        elif choice == 3:
            user1.statement()
        else:
            break
        continue
        
        #user1.deposit(int(input("How much would you like to start off with? ")))
        #user1.transfer(int(input("How much you like to transfer from your account? ")))
        #user1.statement()

    output = []

    add = {"Name": naMe, "Account Number": acc_Num, "Balance": user1.balance}
    output.append(add)

    data = pd.DataFrame(output)
    data.to_excel("output.xlsx")

