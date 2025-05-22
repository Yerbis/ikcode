import time
import random

print("SCkey generator")

print("About SCkey")
print(" ")
print("SCkey is used for a bunch of IKcode formatting")
print("and modifying D grade code. Without it, IKcode's")
print("Interpreter cannot continue with the code.")
print("SCkey is only available to individuals with valid")
print("ID's and ages.")
print("Please generate an SCkey if you need it AT THE MOMENT")
print("SCkeys can only be used once, if you generate one")
print("With your current ID, you will not be able to create")
print("Another one without contacting IKsecurity.")
print(" ")
print("IKsecurity contact info:")
print("ikcode.help@gmail.com or 971-238-2971")

print(" ")

print("SCkey Generator (^ READ THE ABOVE ^)")

name = input("Enter your full name: ")

while name.isdigit():
    print(f"{name} is not a name.")
    name = input("Enter your full name: ")

age = int(input("Enter your age (18+): "))

if age < 18:
    print("Invalid age. Resetting.")

contact_info = input("Enter your email or phone num: ")

ids = []


id = input("Enter any form of ID (bank num, driver id, school id): ")
ids.append(id)

while id in ids:
    print("ERROR")
    print("This ID has been used")
    print("Not available. Contact IKsecurity")
    print("To reuse ID (at ikcode.help@gmail.com)")
    id = input("Enter your ID: ")

while id == "":
    print("ERROR")
    print("Nothing entered. Try again")
    id = input("Enter your ID: ")



ids.append(id)

print("Checking info...")

time.sleep(3)



print("Info valid. Procceding to SCkey generation...")

time.sleep(2)

print("What platform are you using (IKcode / Python)(Recommended: IKcode)")
print("If you are using default keys, type 'none' (not recommended)")
platform = input("Enter platform: ").lower()

while platform not in ["ikcode", "python", "none"]:
    print("Invalid platform. try again")
    platform = input("Enter platform (IKcode or Python or None): ")

time.sleep(1)

print("Gathering platform info...")

time.sleep(3)

confirm = input("Would you like to continue? (Y / N): ").lower()

while confirm == "n":
    print("Generation aborted. Feel free to confirm again anytime")
    confirm = input("Confirm generation? (Y/N): ").lower()

while confirm not in ["y", "n"]:
    print("Unknown answer. Please type Y or N")
    confirm = input("Confirm generation?: ")

print(f"Confirmed. preparing SCkey generation for {platform}")

ikcode_keys = ["Cq36682Zb545666", "Fk80852Yo552924", "Uh59041Kj153289"
               , "At73661Vi434535", "Yp70356Ov322359",
               "Sq05281Hb056013"]

python_keys = ["G5x0R2-213472", "P5p0N4-213198", "W2b3V3-442736"
               , "E0z0N1-355497", "R7s2F1-379072", "F0b9F9-563434"]

default_keys = ["Rz115A-79549w", "Nh684K-98878z", "Ys595X-72384w",
                "Ei184T-99945a", "Ia352L-07462e", "Ol113C-17652k"]


if platform == "ikcode":
    key = random.choice(ikcode_keys)
elif platform == "python":
    key = random.choice(python_keys)
elif platform == "none":
    key = random.choice(default_keys)
else:
    print("Error with platform key generation")
    print("Switching to default keys")
    key = random.choice(default_keys)

time.sleep(6)

print("Gathering info...")

time.sleep(5.5)

print("Generating key (This will take some time)...")

time.sleep(9)

print("Generation successful. Finishing up details...")

time.sleep(4)

print("Clearing cache/data...")

time.sleep(3)

print("Gathering finishing info...")

time.sleep(3)

print("Securing any leak-able data...")

time.sleep(4)

print("Generation done! Preparing key for print...")

time.sleep(3)

print("Adding SCtag...")

time.sleep(5)

sctags = ["-G7014w", "-S5986q", "-J9870o"]

sctag = random.choice(sctags)

print("Finishing up...")

time.sleep(3)

print("Done!")

time.sleep(1)
print(" ")
print(f"Your SCkey for {platform} is: {key}{sctag}")
print("The tag is the last four digits separated by a '-'")
print("It's not needed for most transactions, bu some do require it")

print(" ")

print("Thanks for using SCkey! Use it with caution!")


