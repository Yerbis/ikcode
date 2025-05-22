print("IKbanks")

import random
import time

def show_balance(balance):
    time.sleep(0.7)
    print(f"Your balance is: ${balance: .2f}")
    time.sleep(3)

def deposit(balance):
    amount = float(input("Enter how much you would like to deposit: "))

    if amount < 0:
        print("Not a valid amount")
        return 0
    else:
        time.sleep(0.7)
        print("Payment added to balance")
        time.sleep(3)
        return amount
        


def withdraw(balance):
    amount = float(input("Enter how much you would like to withdraw: "))

    if amount > balance:
        print("Not a valid amount")
        return 0
    elif amount < 0:
        print("Not a valid amount")
    else:
        time.sleep(0.7)
        print("Payment withdrawn")
        time.sleep(3)
        return amount
    
username = ""
password = ""
name = ""

usernames = []
passwords = []
names = []

def account():
    username = input("Enter your username: ")
    usernames.append(username)
    password = input("Create or enter your password: ")
    passwords.append(password)
    name = input("Enter your full name: ")
    names.append(name)
    return username, password, name


def bank_num():
    print("To continue, you must have an account")
    username = input("Enter your username: ")
    if username in usernames:
        print("Username found!")
    else:
        print("Username not found, creating...")
    password = input("Enter your password: ")
    if password in passwords:
        print("Password found!")
    else:
        print("Password not found. Creating...")

    a = random.randint(1, 9)
    b = random.randint(1, 9)
    c = random.randint(1, 9)
    d = random.randint(1, 9)
    e = random.randint(1, 9)
    end = random.randint(100, 999)

    time.sleep(1)
    print("Checking details...")
    time.sleep(3)
    print("Creating number...")
    time.sleep(4)
    print("Number created")
    print(" ")
    print(" - Your number is: - ")
    print(" ")
    print(f" == {a}{b}{c}{d}-{end} == ")
    time.sleep(3)


def main():

    balance = 0
    is_running = True

    while is_running:
        print("Type '1' to see your balance")
        print("Type '2' to deposit")
        print("Type '3' to withdraw")
        print("Type '4' to create an account")
        print("Type '5' to set up a bank account number")
        print("Type 'exit' to exit the account")

        u = input("Enter an action from above: ").lower()

        if u == "1" or u == 1:
            show_balance(balance)
        elif u == "2" or u == 2:
            balance += deposit(balance)
        elif u == "3" or u == 3:
            balance -= withdraw(balance)
        elif u == '4' or u == 4:
            account()
        elif u == '5' or u == 5:
            bank_num()
        elif u == 'exit':
            is_running = False
        else:
            print("Not a valid action")

    print("Exited")

if __name__ == "__main__":
    main()