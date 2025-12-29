from mimetypes import guess_extension
import random
print("Welcome to the number guessing game!")
print("I am thinking of a number between 1 and 20")

#secret number
secret_number = random.randint(1, 20)
guesses = 0
max_guesses = 5

#guess number
while guesses < max_guesses:

    guess = int(input("Enter your first guess: "))
    guesses += 1

    #check if the guess is correct
    if guess == secret_number:
        print("Congratulations! You guessed the number!")
        print("You guessed the number in", guesses, "guesses")
        break
    elif guess < secret_number:
        print("Too low you fool! You guessed", guess,"Try again!")
    else:
        print("Too high you fool! You guessed", guess,"Try again!")
    remaining_guesses = max_guesses - guesses
    if remaining_guesses > 0:
        print("You have", remaining_guesses, "guesses left")
   
if guess != secret_number:
   print("Game over! The secret number was", secret_number)
else:
    print("Congratulations! You guessed the number!")
    print("You guessed the number in", guesses, "guesses")