

def fizzbuzz_game(start,end):
    for i in range(start,end+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)



def fizzbuzz_checker(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number



while True:
    print("Welcome to the FizzBuzz game!")
    print("1. Play FizzBuzz game")
    print("2. Check if a number is FizzBuzz")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))
        print("--------------------------------")
        fizzbuzz_game(start,end)
        print("--------------------------------")
    elif choice == 2:
        number = int(input("Enter a number: "))
        print(fizzbuzz_checker(number))
        print("--------------------------------")

    elif choice == 3:
        print("Thank you for playing!")
        break
    else:
        print("Invalid choice")

