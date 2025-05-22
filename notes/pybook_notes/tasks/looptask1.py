# Example 1
#Takes a list of numbers iterates once for each number in the list
for i in [1, 2, 3]:
    print(i)

print("==================================")

#Example 2
#Iterates over a string with each character(ch) in the string being processed during each iteration.
for ch in "Dingus":
    print(ch)

print("===================================")

#Example 3
#range accepts a single number that dictates how many times the for loop runs.
for i in range(5):
    print("Ding")


print("=================================")

#Outcome:

#from dates.py:

from datetime import datetime

odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]

for i in range(5):
    minute = datetime.today().minute
    
    if minute == odds:
        print("Seems odd")
    else:
        print("No odds right now")
    print(minute)
