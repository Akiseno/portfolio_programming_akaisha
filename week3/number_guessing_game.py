print("Welcome to the number guessing game!")
print("I am thinking of a number between 1 and 20")

#secret number
secret_number = 10

#guess number
guess = int(input("Enter your first guess: "))

#check if the guess is correct
if guess == secret_number:
    print("Congratulations! You guessed the number!")
elif guess < secret_number:
    print("Too low you fool! You guessed", guess,"Try again!")
    guess = int(input("Enter your second guess: "))
    if guess == secret_number:
        print("Congratulations! You guessed the number!")
    else:
        print("Too low you fool! You guessed", guess,)    
    
elif guess > secret_number:
    print("Too high you fool! You guessed", guess,"Try again!")
    guess = int(input("Enter your second guess: "))
    if guess == secret_number:
        print("Congratulations! You guessed the number!")
    else:
        print("Too high you fool! You guessed", guess,)
else:
    print("Sorry, the number is not correct. Try again!")