def broken_guessing_game():
    secret_number = 10
    guess = int(input("Enter your guess: "))
    if guess == secret_number:
        print("Correct guess")
    else:
        print("Wrong guess")
broken_guessing_game()