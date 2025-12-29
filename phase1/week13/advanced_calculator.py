class AdvancedCalculator:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result

    def divide(self, a, b):
        if b != 0:
            result = a / b
            self.history.append(f"{a} / {b} = {result}")
            return result 
        
        else:
             divide_zero = "Sorry, you cannot divide by Zero"
             return divide_zero
     

    def power(self, a, b):
        result = a ** b
        self.history.append(f"{a} ** {b} = {result}")
        return result

    def root(self, a, b):
        result = a ** (1/b)
        self.history.append(f"{a} ** {1/b} = {result}")
        return result

    def modulo(self, a, b):
        result = a%b == 0
        self.history.append(f"{a} % {b} = {result}")
        return result

    def print_history(self):
        print(self.history)

    def clear_history(self):
        self.history = []

calculator = AdvancedCalculator()
while True:
    print("Welcome to the calculator")
    print("What you like to do")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Root")
    print("7. Modulo")
    print("8. Show history")
    print("9. Clear history")
    print("10. Exit")
    choice = input("Whats your choice?  ")
    if choice == "1":
        number1 = int(input("First number: "))
        number2 = int(input("Second number: "))
        add_result = calculator.add(number1, number2)
        print(add_result)

    elif choice == "2":
        number1 = int(input("First number: "))
        number2 = int(input("Second number: "))
        subtract_result = calculator.subtract(number1, number2)
        print(subtract_result)

    elif choice == "3":
        number1 = int(input("First number: "))
        number2 = int(input("Second number: "))
        multiply_result = calculator.multiply(number1, number2)
        print(multiply_result)

    elif choice == "4":
        number1 = int(input("First number: "))
        number2 = int(input("Second number: "))
        divide_result = calculator.divide(number1, number2)
        print(divide_result)
    
    elif choice == "5":
        number1 = int(input("First number: "))
        number2 = int(input("Second number: "))
        power_result = calculator.power(number1, number2)
        print(power_result)

    elif choice == "6":
        number1 = int(input("First number: "))
        number2 = int(input("Second number: "))
        root_result = calculator.root(number1, number2)
        print(root_result)

    elif choice == "7":
        number1 = int(input("First number: "))
        number2 = int(input("Second number: "))
        modulo_result = calculator.modulo(number1, number2)
        print(modulo_result)

    elif choice == "8":
        calculator.print_history()

    elif choice == "9":
        calculator.clear_history()

    elif choice == "10":
        print("Thanks for calculating")
        break

    else:
        print("Invalid choice")

       


        

        

