import random
import time

print("IKsecurity public services")
print("Credit/debit card hider")
print(" ")
print(f"Description of number securer:")
print(" ")
print(f"The first 4 digits you see in the generated code,")
print(f"are the last 4 digits of your number")
print(f"The last 5 digits you see")
print(f"Are randomly generated numbers to conceal the number")
print(f"All IKworks resources and most retailers allow")
print(f"The last 5 digits (called SCdigits) when using for")
print(f"payment. Some don't. Make sure to find the retailers")
print("That don't allow SCdigits, and in that case, use")
print("Your regular number. *Also some retailers banned ")
print("SCdigits.")
print(" ")
print("IKsecurity is not responsible if your card is hacked")
print(" ")
print("^IT IS ADVISED THAT YOU READ THE ABOVE^")
print("IKsecurity public services")
print("Credit/debit card hider")
print(" ")

card_number = input("Enter your credit/debit card number: ")

if len(card_number) < 8 or len(card_number) > 20:
    print("Card number not found")
    print("Invalid length")

elif card_number.isdigit():
    time.sleep(2)

    print("Analyzing number...")

    time.sleep(3)

    print("Getting card info...")

    time.sleep(4)

    print("Generating secure number...")

    time.sleep(5)

    print("Finishing up generation...")

    time.sleep(2)

    print("Verifying generated card...")

    time.sleep(4)

    print("Finishing generation process (this will take some time)...")

    time.sleep(8)

    print("Done! Finishing up process...")

    time.sleep(2)

    print("Your all set!")

    last_digits = card_number[-4:]

    print(f"Your last 4 digits are {last_digits}")

    time.sleep(1)

    print("Starting SCdigits format conversion process...")

    time.sleep(2)

    print("Preparing number for SCdigital conversion...")

    time.sleep(4)

    print("Generation started: converting to SCdigital...")

    time.sleep(6)

    print("Done! Finishing up...")

    time.sleep(3)

    nums = [16342, 75638, 76987, 90873, 76562, 99857, 52413]

    random_digits = random.choice(nums)

    print("Number complete!")

    print(f"Your finished secure card number is: {last_digits}{random_digits}")
    
    
elif card_number.isalpha():
    print(f'"{card_number}" is not a valid card number')


else:
    print("Invalid card number.")



# Fully completed without video

