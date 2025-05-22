print("IKcalculator ")

operator = input("Enter an operator(+, -, *, /): ")

x = float(input("Enter a number: "))

y = float(input("Enter another number: "))

if operator == "+":
    total = x + y
    print(f"{x} + {y} = {total}")
elif operator == "-":
    total = x - y
    print(f"{x} - {y} = {total}")
elif operator == "*":
    total = x * y
    print(f"{x} x {y} = {total}")
elif operator == "/":
    total = x / y
    print(f"{x} / {y} = {total}")
    print("rounded:")
    print(round(total))
elif operator == "/" and x == 0.00 or y == 0.00:
    raise Exception("Cannot divide by zero")
else:
    print(f'Function couldnt complete. "{operator}"')
    print("is not a valid operator.")

# completed without video
    