# How a Dictionary is structured

frog = { 'Name': 'Big Frog', 'Strength': 1200, 'Occupation': 'Frog'}
#          ^         ^           ^         ^        ^          ^
#         Key       Value       Key       Value    Key       Value

# A dictionary is an unordered set of -key/value pairs-
# Each key is assigned to a value, like a dictionary
# Formatting:

# Like said before, Dictionaries contains pairs of key/values
# Each pair is separated by a ","
# The Key can be a String("name"), An integer(1: "1"), or A Tuple((1, 2): "Tuple")
# Use a ":" to connect the key with the value 
# look at dict to see how a basic dictionary is structured
# Unlike lists, Dictionaries use "{}" instead of "[]"

# Dictionaries can also be structured like this:

stack = {'Name': 'Not a frog',
         'Strength': 3, 
         'Occupation': 'Being Dumb'}

print(stack)

# This doesn't change anything in the code, but just the visuals.
# Be careful with the indentation though


# Calling a Dictionary
# Let's say you want to see the value of 'name' in the frog dictionary

print(frog['Name'])
#      ^       ^
#  Dict name  Key

# Dict name is the name of the dictionary, and the key is the key of the value you want to see
# Make sure to structure it like this: (dict['key'])
#                                           ^     ^
#                                  Make sure to include the square brackets "[]"

# | IT DOES NOT MATTER how the dictionary is ordered, just if the interpreter can access the
# | dictionary's values (no matter how big it gets)

# If you want to -ADD- a value to a dictionary, theres a way to do that:

# Let's add IQ to each dictionary (frog, stack)

frog['IQ'] = 120
stack['IQ'] = 2
# ^     ^     ^
# Dict  key   value for key

# (from now on, Dict is short for dictionary)

# Now if we print it we will see the new values added

print(frog)
print(stack)


# Heres a mini project using Dicts to search a word for vowels

vowels = ['a', 'e', 'i', 'o', 'u'] # Create a list for the vowels

word = 'BiggestFrogAhh' # The word that will be searched (You can make it an input by doing [input()]

found = {} # create the empty Dict to store the data

found['a'] = 0 # The following block makes keys and assigns them to values (0)
found['e'] = 0
found['i'] = 0
found['o'] = 0
found['u'] = 0

for letter in word: # searching for the -letter- in -word-, and if it is, add one to the Dict
    if letter in vowels:
        found[letter] += 1 # The '+=' is just used for updating a value 

for k, v in sorted(found.items()): # 'k' for key and 'v' for value, this is used to print better
    print(k, 'was found', v, 'time(s).') 

# 

