from mimetypes import guess_extension
import random
print("Welcome to the enhanced number guessing game!")

#game settings
play_again = "yes"
total_games = 0
total_guesses = 0



#guess number
while play_again.lower() == "yes":
    print( f"Game {total_games + 1}")
    print("I am thinking of a number between 1 and 20")


    secret_number = random.randint(1, 20)
    guesses = 0
    max_guesses = 5

    
    while guesses < max_guesses:
        guess = int(input("Enter your guess: "))
        guesses += 1

    #check if the guess is correct
        if guess == secret_number:
            print("Congratulations! You guessed the number!")
            print("You guessed the number in", guesses, "guesses")
            total_guesses += guesses
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
        total_guesses += guesses
    total_games += 1
    play_again = input("Do you want to play again? (yes/no): ")
    

    print("Thank you for playing!")
    