def main():

    print("IKunnecessary code server")
    print("Follow instructions to get a free debit card number")
    print("that could have a balance of $0.1 - $999.99!")
    text1 = "Waiting for input..."
    text2 = "Validating input..."
    text3 = "Invalid input..."
    text4 = "User entered input..."

    import random

    a = random.randint(1000, 9999)
    b = random.randint(1000, 9999)
    c = random.randint(1000, 9999)
    d = random.randint(1000, 9999)
    e = random.randint(1000, 9999)

    m1 = random.randint(0, 999)
    m2 = random.randint(1, 99)
    m3 = random.randint(1000, 9999)


    text5 = f"Your card number is: {a}-{b}-{c}-{d}"
    text6 = f"Getting balance..."

    if m1 == 0:
        text7 = f"Your balance is: ${m1}.{m2}"
    else:
        text7 = f"Your balance is: ${m1}"

    file = "server_file.txt"

    import time 
    time.sleep(0.7)
    print("Starting...")
    time.sleep(3)

    print(" ")
    u = input("Enter anything to begin: ")

    if u == "":
        waiting = True
        inputed = False
    else:
        waiting = False 
        inputed = True
        
    while waiting:
        with open(file, "a") as f:
            f.write("\n" + text2, text1)
            print("A file called 'server_file.py' has been created")
            print("Locate it and leave it open")

    if inputed:
        with open(file, 'a') as f:
            f.write("\n" + text4)
            print("Input inputted")
            print("Locate and open the file 'server_file.txt' while leaving the program open")


    with open(file, 'a') as f:
        time.sleep(2.9)
        f.write("\n"+ text1)
    u = input("Enter 'continue' to get card: ").lower()

    if u == "continue":
        with open(file, 'a') as f:
            time.sleep(1.8)
            f.write("\n" + text2)
            time.sleep(3)
            f.write("\n Input valid")
            f.write("\n" + text5)
            f.write("\n" + text6)
            f.write("\n" + text7)
            f.write(f"\n Your card's PIN: {m3}")
            print("Submitted")
    
    else:
        with open(file, 'a') as f:
            f.write("\n" + text2)
            f.write("\n" + text3)

    with open(file, 'a') as f:
        f.write("\n Program ended. Access Pin: 67554")


    print("Continue to find your card by locating a new file")
    print("called ''server_file.txt''")
    print("We show the card in a different file to make sure")
    print("that your device is safe")

    print("Got 'Invalid Input...'? Well, you maybe didn't enter")
    print("the correct word or your device isn't safe")


main()