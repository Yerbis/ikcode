# How a function is stuctured

def multiply(a, b): # This first line has something new: 'def'. 
    result = a * b
    return result # Here's another new thing: return. this returns the said value to the function


# 'def' is what you need for every function 
# Detailed view of the start of a function:

#    def         test(a, b):
#     ^               ^
#  start with def   name your function then put "()" and inside them put the values needed
# You can put whatever value you want

# Now call the function



# printing it wont work. We need to CALL the function. Here's how:

aa = 100 # Make 2 new values for each of the values in the function (in this case: a, b)
bb = 10

new_function = multiply(aa, bb) # See how we replaced the origonal values with the new ones

# now print it

print(new_function)

# You see how the new values go into the function
# And print out the result, thats how -return- works. If we didn't put return, nothing would
# come out. 