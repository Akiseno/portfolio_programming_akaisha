from mimetypes import guess_extension
import random
max_guesses = 5
print("Welcome to the number guessing game with difficulty!")
print("Choose a difficulty: easy, medium, hard")
print("easy: random guesses between 1 and 5")
print("medium: random guesses between 1 and 10")
print("hard: random guesses between 1 and 20")
difficulty = input("Enter the difficulty: ")


if difficulty.lower() == "easy":
    max_number = 5   
elif difficulty.lower() == "medium":
    max_number = 10
elif difficulty.lower() == "hard":
    max_number = 20
else:
    print("Invalid difficulty")
    

print("i am thinking of a number between 1 and", max_number)
secret_number = random.randint(1, max_number)
guesses = 0





while guesses < max_guesses:
    guess = int(input("Enter your guess: "))
    guesses += 1

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

if guesses >= max_guesses and guess != secret_number:
 print("Game over! The secret number was", secret_number)


print("Thank you for playing!")
