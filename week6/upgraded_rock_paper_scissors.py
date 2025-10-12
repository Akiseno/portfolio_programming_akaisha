import random
choices = ["rock", "paper", "scissors"]
choice_descriptions = {
    "rock": "Rock is a hard object that can be used to break other objects",
    "paper": "Paper is a soft object that can be used to cover other objects",
    "scissors": "Scissors are a sharp object that can be used to cut other objects"
}

game_stats = {
    "total_games": 0,
    "total_wins": 0,
    "total_losses": 0,
    "total_ties": 0,
    "player_choices": [],
    "computer_choices": [],
    
}

def get_computer_choice():
    return random.choice(choices)

def get_user_choice():
    choice = input("Enter your choice: ")
    while choice not in choices:
        print("Invalid choice! Choose rock, paper or scissors")
        choice = input("Enter your choice: ")
    return choice
    

def determine_winner(computer_choice, user_choice):
    if computer_choice == user_choice:
        return "tie"
    elif computer_choice == "rock" and user_choice == "scissors":
        return "loss"
    elif computer_choice == "paper" and user_choice == "rock":
        return "loss"
    elif computer_choice == "scissors" and user_choice == "paper":
        return "loss"
    else:
        return "win"

def update_stats(user_choice, computer_choice, result):
    game_stats["total_games"] += 1
    if result == "win":
        game_stats["total_wins"] += 1
    elif result == "loss":
        game_stats["total_losses"] += 1
    else:
        game_stats["total_ties"] += 1

    game_stats["player_choices"].append(user_choice)
    game_stats["computer_choices"].append(computer_choice)

def display_stats():
    print("Total games:", game_stats["total_games"])
    print("Total wins:", game_stats["total_wins"])
    print("Total losses:", game_stats["total_losses"])
    print("Total ties:", game_stats["total_ties"])
    print("Player choices:", game_stats["player_choices"])
    print("Computer choices:", game_stats["computer_choices"])


def play_game():
    play_again = "yes"
    while play_again.lower() == "yes":

        computer_choice = get_computer_choice() 
        user_choice = get_user_choice()
        result = determine_winner(computer_choice, user_choice)
        update_stats(user_choice, computer_choice, result)

        #show_score(computer_score, user_score, ties)
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() == "no":
            display_stats()
            break

play_game()