print("Boot.dev notes on Classes")
print("1/31/2025")


# A class must be structured like this:

class Human:
    age = 20
    health = 100
    banana = 2

# Now if we want to double health when eating a banana:

    def eat_banana(self):
        current_health = 100
        current_health *= self.banana
        return current_health

# Now call and print it:

bananed_health = Human()
print(bananed_health.eat_banana())


#Segment 1 done

# Now lets do a constructor

# A constructor assigns values to an empty class. example:

class fruits:

# Notice there is nothing in there. Now do the constructor:

    def __init__(self, apple, banana, lemon):
        self.apple = apple
        self.banana = banana
        self.lemon = lemon

# Now if we print the class it should show the new contents

new_fruits = fruits("Apple", "Banana", "Lemon") # Here you can assign the contents to anything
print(new_fruits.apple)
print(new_fruits.banana)
print(new_fruits.lemon)



    
