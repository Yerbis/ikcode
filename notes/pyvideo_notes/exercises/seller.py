import time
from datetime import datetime

print("IKcommerce seller platform")

item = input("Enter the name of your item: ")
price = float(input("Enter the price of item: "))
quantity = int(input("How much are you selling?: "))

total_price = price * quantity

money = 0

print(f"You have put {item} on sale for ${price}.")
print(f"Total profit: ${total_price}")

# semi completed without video
print("Looking for buyers...")
time.sleep(5)
print("Someone viewed your item!")
time.sleep(3)
print(f"Someone bought your item for ${total_price - 3}!")

confirm = input("Confirm payment or refund buyer? (Confirm/Refund): ").strip().lower()
time.sleep(1)
print("Analyzing...")
time.sleep(3)

if confirm == "confirm":
    money + total_price
    print("Payment successful! Ship within 1 day(s)")
    ship = float(input("Please enter the shipping costs, if it is free, type 0 (if free, you pay $4.99, If not, buyer pays costs): "))
    if ship > 1:
        shep = 0
        total_profit = total_price + ship
    if ship <= 0:
        shep = 4.99
        total_profit = total_price - 4.99
    print(f"You charged the buyer with {ship} for shipping. Total profit: {total_profit}")
    carrier = input("Type one of the following carriers: KPS, Line mail, WSPS, Carr loads. If you don't want any, please type (none): ").strip().lower()
    if carrier == "none":
        shipping_cost_buyer = 0.00
        shipping_cost_seller = ship
    else:
        shipping_cost_buyer = ship
        shipping_cost_seller = 0.00
    print(f"You have selected {carrier}. Buyer pays: ${shipping_cost_buyer}. You pay: ${shipping_cost_seller}")
    overall_profit = total_profit + shipping_cost_buyer + shipping_cost_seller
    if ship <= 0:
        print(f"Reciept: {item} x{quantity} for ${total_price}, shipping: $4.99. ${total_price - 4.99}. Overall total: ${total_profit}")
    elif ship > 1:
        print(f"Reciept: {item} x{quantity} for ${total_price}, shipping: ${ship}. ${total_price} +{ship}. Overall profit: ${total_profit}")
    payment_info = int(input("Enter your card or bank number (SCdigits permitted (allowed)): "))
    print("Analyzing...")
    time.sleep(2)
    print(f"The next payout for {total_profit}  to {payment_info} will be in 4 day(s).")
    print("Now to get the payout, create an account!")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    age = int(input("Selling/buying is only valid for people ages 18+, enter your age: "))
    if age < 18:
        print("You must be 18 to interact with IKcommerce")
    elif age < 0:
        print("You don't exist")
    else:
        print("Welcome to IKcommerce! Just provide the last details and you will be set!")
    full_name = input("Enter your full name: ")
    store_name = input("Name your IKcommerce store to continue to sell across the platform!: ")
    print(f"Thanks, {full_name} for creating an IKcommerce account. Your account, {username}, can be used across all of IKworks resources.")
    print(f" To expand {store_name}, list more items and leave feedback on buyers and other sellers.")
    store_bio = input("Enter a bio (description) of your store to have others get familiar with your products: ")
    print(f"Great! Thanks {full_name} for using IKcommerce! Here's a $10 discount code for any purchases: IKCOMMERCE-10")
    search = input("Search for anything you would like to purchase: ")
    print("Exact match not found. Here's some other products:")
    print("Goo $23 Item ID: 2343")
    print("IKcode full course book| $29.99| Item ID: 4543")
    print("Mystery Barrel| $99.99| Item ID: 6452")
    print("Stick.| $129.99| Item ID: 6736")
    print("Lime Ego 76e Go kart| $899.99| Item ID: 8736")
    i_found = int(input("Enter the item ID for the item you want to purchase: "))
    if i_found == 2343:
        pitem = "Goo"
        pprice = 23.00
        print(f"You are going to purchase {pitem} for ${pprice}.")
        print(f"Shipping with KPS. Shipping is $4.99")
        pconfirm = input("Confirm purchase? Y/N: ")
        if pconfirm == "Y":
            print(f"Purchasing {pitem} with card/bank number {payment_info}")
            print("Processing...")
            time.sleep(3)
            print("Finishing payment...")
            time.sleep(3)
            print(f"One more thing before purchasing! Please enter your address info to ship:")
            address = input()
            print("Great! Now enter your ZIP code:")
            zip_code = int(input())
            print("Thanks! Analyzing details...")
            time.sleep(4)
            discount = input("Before finalizing, enter any discount code you may have: ")
            time.sleep(2)
            print("Checking discount code...")
            time.sleep(4)
            if discount == "IKCOMMERCE-10":
                print(f"Discount exists! Payment finished. Sold for {pprice + 4.99 - 10} (-$10 off)")
            else:
                print("Discount doesn't exist/No discount entered")
                print(f"Payment finished! {pitem} sold for {pprice + 4.99} (with shipping)")
                print(f"Bought on ")
            print(f"We hope to see you again soon, {full_name}!")
        if pconfirm == "N":
            print("Purchase declined by buyer")
        else:
            print("Unknown answer. Im too lazy to re-code everything, so Goodbye")
    elif i_found == 4543:
        pitem = "IKcode full course book"
        pprice = 29.99
        print(f"You are going to purchase {pitem} for ${pprice}.")
        print(f"Shipping with Line mail. Shipping is $2.99")
        pconfirm = input("Confirm purchase? Y/N: ")
        if pconfirm == "Y":
            print(f"Purchasing {pitem} with card/bank number {payment_info}")
            print("Processing...")
            time.sleep(3)
            print("Finishing payment...")
            time.sleep(3)
            print(f"One more thing before purchasing! Please enter your address info to ship:")
            address = input()
            print("Great! Now enter your ZIP code:")
            zip_code = int(input())
            print("Thanks! Analyzing details...")
            time.sleep(4)
            print("Gathering final details...")
            time.sleep(3)
            discount = input("Before finalizing, enter any discount code you may have: ")
            time.sleep(2)
            print("Checking discount code...")
            time.sleep(4)
            if discount == "IKCOMMERCE-10":
                print(f"Discount exists! Payment finished. Sold for {pprice + 2.99 - 10} (-$10 off)")
            else:
                print("Discount doesn't exist/No discount entered")
                print(f"Payment finished! {pitem} sold for ${pprice + 2.99} (with shipping)")
            print(f"We hope to see you again soon, {full_name}!")
        if pconfirm == "N":
            print("Purchase declined by buyer")
        else:
            print("Unknown answer. Im too lazy to re-code everything, so Goodbye")
    elif i_found == 6452:
        pitem = "Mystery barrel"
        pprice = 99.99
        print(f"You are going to purchase {pitem} for ${pprice}.")
        print(f"Shipping with KPS. Shipping is $14.99")
        pconfirm = input("Confirm purchase? Y/N: ")
        if pconfirm == "Y":
            print(f"Purchasing {pitem} with card/bank number {payment_info}")
            print("Processing...")
            time.sleep(3)
            print("Finishing payment...")
            time.sleep(3)
            print(f"One more thing before purchasing! Please enter your address info to ship:")
            address = input()
            print("Great! Now enter your ZIP code:")
            zip_code = int(input())
            print("Thanks! Analyzing details...")
            time.sleep(4)
            discount = input("Before finalizing, enter any discount code you may have: ")
            time.sleep(2)
            print("Checking discount code...")
            time.sleep(4)
            if discount == "IKCOMMERCE-10":
                print(f"Discount exists! Payment finished. Sold for {pprice + 14.99 - 10} (-$10 off)")
            else:
                print("Discount doesn't exist/No discount entered")
                print(f"Payment finished! {pitem} sold for ${pprice + 14.99} (with shipping)")
            print(f"We hope to see you again soon, {full_name}!")
        if pconfirm == "N":
            print("Purchase declined by buyer")
        else:
            print("Unknown answer. Im too lazy to re-code everything, so Goodbye")
    elif i_found == 6736:
        pitem = "Stick"
        pprice = 129.99
        print(f"You are going to purchase {pitem} for ${pprice}.")
        print(f"Shipping with KPS. Shipping is free")
        pconfirm = input("Confirm purchase? Y/N: ")
        if pconfirm == "Y":
            print(f"Purchasing {pitem} with card/bank number {payment_info}")
            print("Processing...")
            time.sleep(3)
            print("Finishing payment...")
            time.sleep(3)
            print(f"One more thing before purchasing! Please enter your address info to ship:")
            address = input()
            print("Great! Now enter your ZIP code:")
            zip_code = int(input())
            print("Thanks! Analyzing details...")
            time.sleep(4)
            discount = input("Before finalizing, enter any discount code you may have: ")
            time.sleep(2)
            print("Checking discount code...")
            time.sleep(4)
            if discount == "IKCOMMERCE-10":
                print(f"Discount exists! Payment finished. Sold for {pprice - 10} (-$10 off)")
            else:
                print("Discount doesn't exist/No discount entered")
                print(f"Payment finished! {pitem} sold for {pprice} (with shipping)")
            print(f"We hope to see you again soon, {full_name}!")
            if pconfirm == "N":
                print("Purchase declined by buyer")
            else:
                print("Unknown answer. Im too lazy to re-code everything, so Goodbye")
    elif i_found == 8736:
        pitem = "Lime ego 76e Go kart"
        pprice = 899.99
        print(f"You are going to purchase {pitem} for ${pprice}.")
        print(f"Shipping with KPS. Shipping is $114.99")
        pconfirm = input("Confirm purchase? Y/N: ")
        if pconfirm == "Y":
            print(f"Purchasing {pitem} with card/bank number {payment_info}")
            print("Processing...")
            time.sleep(3)
            print("Finishing payment...")
            time.sleep(3)
            print(f"One more thing before purchasing! Please enter your address info to ship:")
            address = input()
            print("Great! Now enter your ZIP code:")
            zip_code = int(input())
            print("Thanks! Analyzing details...")
            time.sleep(4)
            discount = input("Before finalizing, enter any discount code you may have: ")
            time.sleep(2)
            print("Checking discount code...")
            time.sleep(4)
            if discount == "IKCOMMERCE-10":
                print(f"Discount exists! Payment finished. Sold for {pprice + 114.99 - 10} (-$10 off)")
            else:
                print("Discount doesn't exist/No discount entered")
                print(f"Payment finished! {pitem} sold for {pprice + 114.99} (with shipping)")
            print(f"We hope to see you again soon, {full_name}!")
        if pconfirm == "N":
            print("Purchase declined by buyer")
        else:
            print("Unknown answer. Im too lazy to re-code everything, so Goodbye")
    else:
        print(f"{i_found} is not a valid ID.")
elif confirm == "refund":
    print("Payment declined by seller. Refunded")
else:
    confirm = input("Unknown answer. Please type Confirm or Refund: ").strip().lower()
    if confirm == "confirm":
        print("Payment successful! Ship within 1 day(s)")
        ship = float(input("Please enter the shipping costs, if it is free, type 0 (if free, you pay $4.99, If not, buyer pays costs): "))
        if ship > 1:
            shep = 0
            total_profit = total_price + ship
        if ship <= 0:
            shep = 4.99
            total_profit = total_price - 4.99
        print(f"You charged the buyer with {ship} for shipping. Total profit: {total_profit}")
        carrier = input("Type one of the following carriers: KPS, Line mail, WSPS, Carr loads. If you don't want any, please type (none): ").strip().lower()
        if carrier == "none":
            shipping_cost_buyer = 0.00
            shipping_cost_seller = ship
        else:
            shipping_cost_buyer = ship
            shipping_cost_seller = 0.00
        print(f"You have selected {carrier}. Buyer pays: ${shipping_cost_buyer}. You pay: ${shipping_cost_seller}")
        overall_profit = total_profit + shipping_cost_buyer + shipping_cost_seller
        if ship <= 0:
            print(f"Reciept: {item} x{quantity} for ${total_price}, shipping: $4.99. ${total_price - 4.99}. Overall total: ${total_profit}")
        elif ship > 1:
            print(f"Reciept: {item} x{quantity} for ${total_price}, shipping: ${ship}. ${total_price} +{ship}. Overall profit: ${total_profit}")
        payment_info = int(input("Enter your card or bank number: "))
        print(f"The next payout for {total_profit}  to {payment_info} will be in 4 day(s).")
        print("Now to get the payout, create an account!")
        username = input("Enter your username: ")
        password = input("Enter your password")
        age = input("Selling/buying is only valid for people ages 18+, enter your age: ")
        if age < 18:
            print("You must be 18 to interact with IKcommerce")
        elif age < 0:
            print("You don't exist")
        else:
            print("Welcome to IKcommerce! Just provide the last details and you will be set!")
        full_name = input("Enter your full name: ")
        store_name = input("Name your IKcommerce store to continue to sell across the platform!: ")
        print(f"Thanks, {full_name} for creating an IKcommerce account. Your account, {username}, can be used across all of IKworks resources.")
        print(f" To expand {store_name}, list more items and leave feedback on buyers and other sellers.")
        store_bio = input("Enter a bio (description) of your store to have others get familiar with your products: ")
        print(f"Great! Thanks {full_name} for using IKcommerce! Here's a $10 discount code for any purchases: IKCOMMERCE-10")
        search = input("Search for anything you would like to purchase: ")
        print("Exact match not found. Here's some other products:")
        print("Goo $23 Item ID: 2343")
        print("IKcode full course book| $29.99| Item ID: 4543")
        print("Mystery Barrel| $99.99| Item ID: 6452")
        print("Stick.| $129.99| Item ID: 6736")
        print("Lime Ego 76e Go kart| $899.99| Item ID: 8736")
        i_found = int(input("Enter the item ID for the item you want to purchase: "))
        if i_found == 2343:
            pitem = "Goo"
            pprice = 23.00
            print(f"You are going to purchase {pitem} for ${pprice}.")
            print(f"Shipping with KPS. Shipping is $4.99")
            pconfirm = input("Confirm purchase? Y/N: ")
            if pconfirm == "Y":
                print(f"Purchasing {pitem} with card/bank number {payment_info}")
                print("Processing...")
                time.sleep(3)
                print("Finishing payment...")
                time.sleep(3)
                print(f"One more thing before purchasing! Please enter your address info to ship:")
                address = input()
                print("Great! Now enter your ZIP code:")
                zip_code = int(input())
                print("Thanks! Analyzing details...")
                time.sleep(4)
                discount = input("Before finalizing, enter any discount code you may have: ")
                if discount == "IKCOMMERCE-10":
                    print(f"Discount exists! Payment finished. Sold for {pprice + 4.99 - 10} (-$10 off)")
                else:
                    print("Discount doesn't exist/No discount entered")
                    print(f"Payment finished! {pitem} sold for {pprice + 4.99} (with shipping)")
                print(f"We hope to see you again soon, {full_name}!")
        elif i_found == 4543:
            pitem = "IKcode full course book"
            pprice = 29.99
            print(f"You are going to purchase {pitem} for ${pprice}.")
            print(f"Shipping with Line mail. Shipping is $2.99")
            pconfirm = input("Confirm purchase? Y/N: ")
            if pconfirm == "Y":
                print(f"Purchasing {pitem} with card/bank number {payment_info}")
                print("Processing...")
                time.sleep(3)
                print("Finishing payment...")
                time.sleep(3)
                print(f"One more thing before purchasing! Please enter your address info to ship:")
                address = input()
                print("Great! Now enter your ZIP code:")
                zip_code = int(input())
                print("Thanks! Analyzing details...")
                time.sleep(4)
                discount = input("Before finalizing, enter any discount code you may have: ")
                if discount == "IKCOMMERCE-10":
                    print(f"Discount exists! Payment finished. Sold for {pprice + 2.99 - 10} (-$10 off)")
                else:
                    print("Discount doesn't exist/No discount entered")
                    print(f"Payment finished! {pitem} sold for ${pprice + 2.99} (with shipping)")
                print(f"We hope to see you again soon, {full_name}!")
        elif i_found == 6452:
            pitem = "Mystery barrel"
            pprice = 99.99
            print(f"You are going to purchase {pitem} for ${pprice}.")
            print(f"Shipping with KPS. Shipping is $14.99")
            pconfirm = input("Confirm purchase? Y/N: ")
            if pconfirm == "Y":
                print(f"Purchasing {pitem} with card/bank number {payment_info}")
                print("Processing...")
                time.sleep(3)
                print("Finishing payment...")
                time.sleep(3)
                print(f"One more thing before purchasing! Please enter your address info to ship:")
                address = input()
                print("Great! Now enter your ZIP code:")
                zip_code = int(input())
                print("Thanks! Analyzing details...")
                time.sleep(4)
                discount = input("Before finalizing, enter any discount code you may have: ")
                if discount == "IKCOMMERCE-10":
                    print(f"Discount exists! Payment finished. Sold for {pprice + 14.99 - 10} (-$10 off)")
                else:
                    print("Discount doesn't exist/No discount entered")
                    print(f"Payment finished! {pitem} sold for ${pprice + 14.99} (with shipping)")
                print(f"We hope to see you again soon, {full_name}!")
        elif i_found == 6736:
            pitem = "Stick"
            pprice = 129.99
            print(f"You are going to purchase {pitem} for ${pprice}.")
            print(f"Shipping with KPS. Shipping is free")
            pconfirm = input("Confirm purchase? Y/N: ")
            if pconfirm == "Y":
                print(f"Purchasing {pitem} with card/bank number {payment_info}")
                print("Processing...")
                time.sleep(3)
                print("Finishing payment...")
                time.sleep(3)
                print(f"One more thing before purchasing! Please enter your address info to ship:")
                address = input()
                print("Great! Now enter your ZIP code:")
                zip_code = int(input())
                print("Thanks! Analyzing details...")
                time.sleep(4)
                discount = input("Before finalizing, enter any discount code you may have: ")
                if discount == "IKCOMMERCE-10":
                    print(f"Discount exists! Payment finished. Sold for {pprice - 10} (-$10 off)")
                else:
                    print("Discount doesn't exist/No discount entered")
                    print(f"Payment finished! {pitem} sold for {pprice} (with shipping)")
                print(f"We hope to see you again soon, {full_name}!")
        elif i_found == 8736:
            pitem = "Lime ego 76e Go kart"
            pprice = 899.99
            print(f"You are going to purchase {pitem} for ${pprice}.")
            print(f"Shipping with KPS. Shipping is $114.99")
            pconfirm = input("Confirm purchase? Y/N: ")
            if pconfirm == "Y":
                print(f"Purchasing {pitem} with card/bank number {payment_info}")
                print("Processing...")
                time.sleep(3)
                print("Finishing payment...")
                time.sleep(3)
                print(f"One more thing before purchasing! Please enter your address info to ship:")
                address = input()
                print("Great! Now enter your ZIP code:")
                zip_code = int(input())
                print("Thanks! Analyzing details...")
                time.sleep(4)
                discount = input("Before finalizing, enter any discount code you may have: ")
                if discount == "IKCOMMERCE-10":
                    print(f"Discount exists! Payment finished. Sold for {pprice + 114.99 - 10} (-$10 off)")
                else:
                    print("Discount doesn't exist/No discount entered")
                    print(f"Payment finished! {pitem} sold for {pprice + 114.99} (with shipping)")
                print(f"We hope to see you again soon, {full_name}!")
    elif confirm == "refund":
        print("Refunded")
    else:
        print("Unknown answer. Exiting.")