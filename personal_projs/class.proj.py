import time

print("IKnature frog creator via Froog caterings")

class Animal:


    def __init__(self, is_alive, name):
        self.is_alive = is_alive
        self.name = name
    
class Frog(Animal):

    def __init__(self, jump_distance, color, type):
        super().__init__(self.is_alive, self.name)
        self.jump_distance = jump_distance
        self.color = color
        self.type = type
    

name = input("Enter name of frog: ")
jdist = input("Enter how long the frog can jump (in): ")
color = input("What color is the frog: ")
type = input("What speices of frog is the frog:" )


time.sleep(0.3)
print("Creating frog...")
time.sleep(3)

print("Done!")
print(" ")
print("Results: ")

frog = Frog(True, name, jdist, color, type)

print(f"Frog name: {name}")
print(f"Jump distance(in): {jdist}")
print(f"Frog color: {color}")
print(f"Frog type: {type}")

print(" ")
print("Backend: ")
print(frog)