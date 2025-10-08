def add_numbers(num1, num2):
    print(num1, "+", num2, "=", num1 + num2)
    return num1 + num2

def subtract_numbers(num1, num2):
    print(num1, "-", num2, "=", num1 - num2)
    return num1 - num2

def multiply_numbers(num1, num2):
    print(num1, "*", num2, "=", num1 * num2)
    return num1 * num2

def divide_numbers(num1, num2):
    print(num1, "/", num2, "=", num1 / num2)
    return num1 / num2

sum = add_numbers(1, 2)
difference = subtract_numbers(1, 2)
product = multiply_numbers(1, 2)
quotient = divide_numbers(1, 2)

print("sum:", sum, ",", "difference:", difference, ",", "product:", product, ",", "quotient:", quotient)
