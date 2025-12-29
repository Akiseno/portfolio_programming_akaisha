#guessing loop
secret_number = 10
guess = 0

guess = int(input("Enter your guess: "))
while guess != secret_number:
    print("Wrong guess")
    guess = int(input("Enter your guess: "))
print("Correct guess")



#guessing loop with a limit