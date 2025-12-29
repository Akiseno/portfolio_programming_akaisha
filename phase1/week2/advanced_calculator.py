print("advanced calculator")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Choose an Operation")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

operation = input("Enter the operation: ")

if operation == "1":
    print("The sum of the two numbers is", num1 + num2)
elif operation == "2":
    print("The difference of the two numbers is", num1 - num2)
elif operation == "3":
    print("The product of the two numbers is", num1 * num2)
elif operation == "4":
    if num2 == 0:
        print("Error: Division by zero")
    else:
        print("The quotient of the two numbers is", num1 /num2)
