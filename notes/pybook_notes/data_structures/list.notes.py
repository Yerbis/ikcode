# How a list is structured
# Each object in a list is separated by "," 
# and each object can be anything (integer, string, variable, etc)

a = 'a'
list = ["hi", 232, a, "IKcode", 66, "Da biggest frog" ]
#         ^    ^   ^     ^      ^         ^
#         0    1   2     3      4         5 

# The numbers you see assigned to the values above are the -index values-
# Notice that there are -6- values in the list, but it shows 5 as the highest
# This is because lists are numbered from 0 upward
# Lists are also -mutable-, which means you can remove, add, or edit any value in the list

# Here's how you can -add- a value:

list.append(46)
list.append(56)

print(list)

# Here's how you can -remove- something from a list:

list.remove(66)

print(list)

# Another way to take things off a list is .pop()

list.pop()

# or

list.pop(5)
#        ^
#      Index

print(list)

# A way to merge lists is .extend

list.extend(4, 5)
#           ^  ^
#          These aren't indexs, but the values you want to add to the end of the said list

# If you want to add a value at index 0 or 1 or whatever index, use .insert

list.insert(0, 'FIRST!')
#           ^     ^
#          Index  Value


# How to slice lists (START, STOP, STEP)

list[0:6:2]
# Every 2nd value up to (but not including) index 6

list[3:]
# Skip the first 3 values, then gives everything else

list[:6]
# All values up to (not including) index 6

list[::2]
# Every second value

list[-6:]
# Last 6 values 

# Slicing is great because it is -non-destructive-, which means it doesn't alter the original list.
# This is how you can make an empty list (Which you can use later on in a function)

empty_list = []

# How to merge lists

list1 = [1, 2, 3]
list2 = [4, 5, 6]

merged = list1 + list2


# What if you want to check if there are certain letters in a word? well we can use 'for'

vowels = ['a', 'e', 'i', 'o', 'u']

# Now type the word you want to check here or use input()

word = 'BiggestBird'

for letter in word:
    if letter in vowels:
        print(letter)




