import random
def get_computer_choice():
    computer_choice = random.choice(["1", "2", "3"])
    return computer_choice


def get_user_choice():
    user_choice = input("Choose 1 for rock, 2 for paper or 3 for scissors: ")
    while user_choice not in ["1", "2", "3"]:
        print("Invalid choice! Choose rock, paper or scissors")
        user_choice = input("Choose 1 for rock, 2 for paper or 3 for scissors: ")
    return user_choice

def determine_winner(computer_choice, user_choice):
    if computer_choice == user_choice:
        return "It's a tie!"
    elif computer_choice == "1" and user_choice == "3":
        return "You lose!"
    elif computer_choice == "2" and user_choice == "1":
        return "You lose!"
    elif computer_choice == "3" and user_choice == "2":
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
    play_again = "yes"
    while play_again.lower() == "yes":

        computer_choice = get_computer_choice() 
        user_choice = get_user_choice()
        result = determine_winner(computer_choice, user_choice)
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1
        else:
            ties += 1
        rounds += 1
        #show_score(computer_score, user_score, ties)
        play_again = input("Do you want to play again? (yes/no): ")

           
    
    show_statistics(computer_score, user_score, ties, rounds)



def show_statistics(computer_score, user_score, ties,rounds):
    print("Statistics:")
    print("Total rounds:", rounds)
    print("Total ties:", ties)
    print("Total wins:", user_score)
    print("Total losses:", computer_score)
    print("Win percentage:", user_score / rounds * 100)
    print("Loss percentage:", computer_score / rounds * 100)
    print("Tie percentage:", ties / rounds * 100)
    
    if user_score > computer_score:
        print("You win!")
    elif user_score < computer_score:
        print("You lose!")
    else:
        print("It's a tie!")
    

play_game()
   