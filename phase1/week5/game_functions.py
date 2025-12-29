def show_menu():
    print("game menu")
    print("1. play game")
    print("2. view rules")
    print("3. exit")

def view_rules():
    print("game rules")
    print("choose rock paper or scissors")
    print("rock beats scissors")
    print("paper beats rock")
    print("scissors beats paper")
    
def play_game():
    print("playing game")
    

show_menu()
choice = input("Enter your choice: ")
if choice == "1":
    play_game()
elif choice == "2":
    view_rules()
elif choice == "3":
    print("exiting game")
else:
    print("invalid choice")