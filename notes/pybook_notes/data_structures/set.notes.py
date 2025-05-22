# How a set is structured

people = {'Jim', 'fun', 'John', 'Macks', 'John', '2022 Ford F-150 4x4 Off-road'}
#        ^                ^                  ^                                  ^
# Curly brace           These two are duplicates.                           Curly Brace
#                        One WONT print out


# A set's main use is that is it an  unordered set of unique objects
# And they do NOT allow duplicates
# Think of a set as a collection of unordered unique items-no duplicates (From Pybook)
# Sets are easy to spot because they have curly braces '{}' and each value is separated with ","

# Now let's print it and see what happens (ikcode/notes/pybook_notes/data_structures)

print(people)
print('=====================================================================================')
# What if we want to combine a set with another? well this is how:


cars = ('Mercedes C class', 'Honda civic 2013', 'Diesel BMW', '2022 Ford F-150 4x4 Off-road')
#                                                                          ^
#                                                                     Duplicate        
merge = people.union(set(cars))
#                ^
#           we use .union(set()) mostly. 

print(merge)

# after it's printed, you will see that that the set becomes larger.
# Notice that at the end theres a 'Duplicate'. We already have that value in the people's set
# When it is merged, only one will be printed


# Here is a set mini project, it just shows you different set methods 

vowels = set('aeiou') # Another way of making a set
word = 'hello'

u = vowels.union(set(word)) # This merges the word variable and the vowels set

u_list = sorted(list(u)) # This turns 'u' into a sorted list

d = vowels.difference(set(word)) # This checks for differences between the vowels set and word

i = vowels.intersection(set(word)) # The intersection confirms if certain values are in word




