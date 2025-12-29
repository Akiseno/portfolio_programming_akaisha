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

computer_choice = get_computer_choice() 
user_choice = get_user_choice()
print(determine_winner(computer_choice, user_choice))
print("The computer chose", computer_choice)
print("You chose", user_choice)