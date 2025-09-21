print("Welcome to the scoring guessing game!")
print("I am thinking of a number between 1 and 20")

#secret number
secret_number = 10
score = 100

#guess number
guess1 = int(input("Enter your first guess: "))

#check if the first guess is correct
if guess1 == secret_number:
    print("Congratulations! You guessed the number!")
    print("You scored", score, "points")
elif guess1 < secret_number:
    print("Too low! You guessed", guess1, "Try again!")
    score = score - 10  # Deduct 10 points for wrong guess
    print("You scored", score, "points")
    
    # Second guess
    guess2 = int(input("Enter your second guess: "))
    if guess2 == secret_number:
        print("Congratulations! You guessed the number!")
        print("You scored", score, "points")
    elif guess2 < secret_number:
        print("Too low! You guessed", guess2, "Try again!")
        score = score - 10  # Deduct 10 points for wrong guess
        print("You scored", score, "points")
        
        # Third guess
        guess3 = int(input("Enter your third guess: "))
        if guess3 == secret_number:
            print("Congratulations! You guessed the number!")
            print("You scored", score, "points")
        elif guess3 < secret_number:
            print("Too low! You guessed", guess3, "Game over!")
            score = score - 10  # Deduct 10 points for wrong guess
            print("You scored", score, "points")
        else:
            print("Too high! You guessed", guess3, "Game over!")
            score = score - 10  # Deduct 10 points for wrong guess
            print("You scored", score, "points")
    elif guess2 > secret_number:
        print("Too high! You guessed", guess2, "Try again!")
        score = score - 10  # Deduct 10 points for wrong guess
        print("You scored", score, "points")
        
        # Third guess
        guess3 = int(input("Enter your third guess: "))
        if guess3 == secret_number:
            print("Congratulations! You guessed the number!")
            print("You scored", score, "points")
        elif guess3 < secret_number:
            print("Too low! You guessed", guess3, "Game over!")
            score = score - 10  # Deduct 10 points for wrong guess
            print("You scored", score, "points")
        else:
            print("Too high! You guessed", guess3, "Game over!")
            score = score - 10  # Deduct 10 points for wrong guess
            print("You scored", score, "points")
elif guess1 > secret_number:
    print("Too high! You guessed", guess1, "Try again!")
    score = score - 10  # Deduct 10 points for wrong guess
    print("You scored", score, "points")
    
    # Second guess
    guess2 = int(input("Enter your second guess: "))
    if guess2 == secret_number:
        print("Congratulations! You guessed the number!")
        print("You scored", score, "points")
    elif guess2 < secret_number:
        print("Too low! You guessed", guess2, "Try again!")
        score = score - 10  # Deduct 10 points for wrong guess
        print("You scored", score, "points")
        
        # Third guess
        guess3 = int(input("Enter your third guess: "))
        if guess3 == secret_number:
            print("Congratulations! You guessed the number!")
            print("You scored", score, "points")
        elif guess3 < secret_number:
            print("Too low! You guessed", guess3, "Game over!")
            score = score - 10  # Deduct 10 points for wrong guess
            print("You scored", score, "points")
        else:
            print("Too high! You guessed", guess3, "Game over!")
            score = score - 10  # Deduct 10 points for wrong guess
            print("You scored", score, "points")
    elif guess2 > secret_number:
        print("Too high! You guessed", guess2, "Try again!")
        score = score - 10  # Deduct 10 points for wrong guess
        print("You scored", score, "points")
        
        # Third guess
        guess3 = int(input("Enter your third guess: "))
        if guess3 == secret_number:
            print("Congratulations! You guessed the number!")
            print("You scored", score, "points")
        elif guess3 < secret_number:
            print("Too low! You guessed", guess3, "Game over!")
            score = score - 10  # Deduct 10 points for wrong guess
            print("You scored", score, "points")
        else:
            print("Too high! You guessed", guess3, "Game over!")
            score = score - 10  # Deduct 10 points for wrong guess
            print("You scored", score, "points")