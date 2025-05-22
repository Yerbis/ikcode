def divide(a, b):
    result = a / b
    try:
        a * b
    except ZeroDivisionError:
        print("Not able to divide")


print("Enter a number")
aa = input()
aa = int()

print("enter another number")
bb = input()
bb = int()


result = divide(aa, bb)
print("The result is", result)

