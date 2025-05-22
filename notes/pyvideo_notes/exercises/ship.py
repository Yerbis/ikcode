print("IKcommerce shipping")

import time

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    
    print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')}, {kwargs.get('state')} {kwargs.get('zip')}")


fr = input("Enter your first name: ")
ls = input("Enter your last name: ")

st = input("Enter the street address you are shipping to: ")
ci = input("Enter the city you are shipping to: ")
si = input("Enter the state you are shipping to: ")
zi = input("Enter your ZIP code: ")

time.sleep(1)
print("Analyzing details...")
time.sleep(3)

print("To continue, login your IKcommerce/IKworks account")

username = input("Enter your accounts username: ")

password = input(f"Enter the password for {username}: ")

time.sleep(1)
print("Checking account details...")
time.sleep(2)
print("Checking if this account has any orders...")
time.sleep(3)
print("Done! Your account is good to go")

print("Review shipping details:")

print(shipping_label(fr, ls, 
                     street=st,
                     city=ci,
                     state=si,
                     zip=zi))

print(f"Account details: \n Username: {username}")

confirm = input("Confirm shipment? (y/n): ").lower()
time.sleep(1)
print("Analyzing...")
time.sleep(3)

if confirm == "y":
    print("Shipment placed! Have a good day")
elif confirm == "n":
    print("Shipment canceled by shipper.")
else:
    while not confirm == "y" or confirm == "n":
        print("Invalid answer")
        confirm = input("Please enter (y/n) to confirm shipment: ")