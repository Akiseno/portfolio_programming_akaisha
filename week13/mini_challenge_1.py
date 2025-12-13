import random
def number_guessing_game():
    secret = random.randint(1,10)
    while True:
        guess = int(input("Whats your guess? "))
        if guess == secret:
            print("You guessed the number")
            break
        else:
            print("Sorry you didnt guess right")






number_guessing_game()

