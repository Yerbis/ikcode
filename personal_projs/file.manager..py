print("IKcode file creator & searcher")
import time
import os

path = input("Enter the directory path: ")

print("Finding directory path...")
time.sleep(3)
print("Path found!")
print(f"Directory path: {path}")
print("===================================")
print(" ")
print("Enter '1' to create a new file: ")
print("Enter '2' to search for an existing file: ")
print("Enter '3' to update the directory path")
print("Enter '4' to delete an existing file")
print("Enter '5' to exit")

choice = input("Enter your choice: ")
if choice == "1":
    yn = input("Is the file included in the directory path? (y/n): ")
    if yn.lower( ) == "y":
        file = f"{path}"
    else:
        ufile = input("Enter the file name: ")
        ext = input("Enter the file extension (.txt, .json, .csv): ")
        print("Creating file...")
        time.sleep(2)
        file = f"{path}/{ufile}.{ext}"  
    with open(file, "w") as f:
        content = input("Enter the content of the file: ")
        f.write(content)
        print(f"File {file} created successfully.")

elif choice == "2":
    yn = input("Are you going to include the entire directory path? (y/n): ")
    if yn.lower() == "y":
        file = input('Enter the entire file path: ')
    else:
        ufile = input("Enter the file name: ")
        ext = input("Enter the file extension (.txt, .json, .csv): ")
        file = f"{path}/{ufile}.{ext}"

    print("Searching for file...")
    time.sleep(2)
    try:
        with open(file, "r") as f:
            content = f.read()
            print(f"File {file} found.")
            print("Content of the file:")
            print("===================================")
            print(content)
    except FileNotFoundError:
        print(f"File {file} not found.")
elif choice == "3":
    path = input("Enter the new directory path: ")
    print("Directory path updated successfully.")
elif choice == "4":
    yn = input("Are you going to include the entire directory path? (y/n): ")
    if yn.lower() == "y":
        file = input('Enter the entire file path: ')
    else:
        ufile = input("Enter the file name: ")
        ext = input("Enter the file extension (.txt, .json, .csv): ")
        file = f"{path}/{ufile}.{ext}"
    print("Deleting file...")
    time.sleep(2)
    try:
        os.remove(file)
        print(f"File {file} deleted successfully.")
    except FileNotFoundError:
        print(f"File {file} not found.")
elif choice == "5":
    print("Exiting...")
    time.sleep(2)
else:
    print("Invalid choice. Please try again.")
    time.sleep(2)
