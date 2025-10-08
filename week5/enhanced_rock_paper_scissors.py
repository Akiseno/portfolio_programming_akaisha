import random
def get_computer_choice():
    computer_choice = random.choice(["rock", "paper", "scissors"])
    return computer_choice


def get_user_choice():
    user_choice = input("Choose rock, paper or scissors: ")
    while user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Choose rock, paper or scissors")
        user_choice = input("Choose rock, paper or scissors: ")
    return user_choice

def determine_winner(computer_choice, user_choice):
    if computer_choice == user_choice:
        return "It's a tie!"
    elif computer_choice == "rock" and user_choice == "scissors":
        return "You lose!"
    elif computer_choice == "paper" and user_choice == "rock":
        return "You lose!"
    elif computer_choice == "scissors" and user_choice == "paper":
        return "You lose!"
    else:
        return "You win!"

def show_score(computer_score, user_score, ties):
    print("The computer has", computer_score, "points")
    print("You have", user_score, "points")
    print("There have been", ties, "ties")

def play_game():
    computer_score = 0
    user_score = 0
    ties = 0
    rounds = 0
    while rounds < 5:
        print(f"Round {rounds + 1}")

        computer_choice = get_computer_choice() 
        user_choice = get_user_choice()
        print("The computer chose", computer_choice)
        print("You chose", user_choice)
        result = determine_winner(computer_choice, user_choice)
        print(result)
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1
        else:
            ties += 1
        rounds += 1

        show_score(computer_score, user_score, ties)
    print("Final score:")
    if user_score > computer_score:
        print("You win!")
    elif user_score < computer_score:
        print("You lose!")
    else:
        print("It's a tie!")

play_game()
   