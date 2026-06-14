num1 = float(input("enter first number:"))
num2 = float(input("enter second number:"))

print("\n choose an operation:")
print("+ for addition")
print("- for subtraction")
print("* for multiplication")
print("/ for division")


operation = input("enter operation:")

if operation == "+":
    result = num1 + num2
    print("Result =", result)

elif operation == "-":
    result = num1 - num2
    print("result =", result)

elif operation == "*":
    result = num1 * num2
    print("Result =", result)

elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result =", result)

    else:
        print("error: division by zero is not allowed.")
        
else:
    print("Invalid operation selected.")
    
