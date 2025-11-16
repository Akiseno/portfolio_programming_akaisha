#adventure game
print("Welcome to the adventure game!")
def get_player_name():
    name = input("Enter your name: ")
    return name

def display_welcome_message(name):
    print(f"Welcome to the adventure game, {name}!")
    print("You are a brave knight on a quest to save the kingdom from a dragon.")
    print("You will need to choose your path wisely.")

def forest_scene():
    print("You are in a forest. You see a path to the left and a path to the right.")
    print("Which path do you choose? (left/right)")
    path = input("Enter your choice: ")
    if path.lower() == "left":
        return "light"
    elif path.lower() == "right":
        return "cave"

    else:
        print("Invalid choice. Please enter left or right.")
        return "end"

def light_scene(name):
    print("Glowing Light")
    print(f"{name}, you approach the glowing light.")
    print("Its a magical crystal floating in the air")
    print(f"The crystal speaks: Hello, {name}, I grant you one wish.")
    print("1. I wish for treasure.")
    print("2. I wish for knowledge.")
    print("3. I wish for a secret.")
    choice = input("Enter your choice: ")
    if choice == "1":
        print("You are granted the treasure.")
        return "treasure"
    elif choice == "2":
        print("You are granted knowledge.")
        return "knowledge"
    elif choice == "3":
        print("You are granted a secret.")
        return "poopie"
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
        return "end"

def cave_scene(name):
    print("Dark Cave")
    print(f"{name}, you enter the dark cave.")
    print("You can barely see, but you hear something moving.")
    print("1. Light a torch.")
    print("2. Feel around in the dark.")
    print("3. Call out Hello?")
    choice = input("Enter your choice: ")
    if choice.lower() == "1":
        print("You light a torch and see a sleeping dragon, you quietly sneak past and find hidden treasure.")
        print(f"Congratulations {name}, you have found the treasure!")
        return "treasure"
    elif choice.lower() == "2":
        print("You feel around in the dark and find a hidden passage, the passage leads to an ancient library.")
        print("You discover books of forgotten knowledge")
        return "knowledge"
    elif choice.lower() == "3":
        print("You call out Hello? and you hear a friendly voice respond.")
        print("Its a wise old owl who becomes your mentor and teaches you the ways of the forest.")
        print("You make a new friend and continue your quest.")
        return "friendship"
    else:
        print("Invalid choice. Please enter left or right.")
        return "end"


def display_ending(name, result):
    print(f"Adventure complete, {name}!")
    if result == "treasure":
        print(f"Congratulations {name}! You have found the treasure!")
        print("You are now extremely rich and have a new castle and a new kingdom.")
        print(f"Your name will be remembered as {name.title()} the Treasure Hunter.")
    elif result == "knowledge":
        print(f"Congratulations {name}! You have found the knowledge!")
        print("You gain wisdom and became a scholar.")
        print(f"Your name will be remembered as {name.title()} the Wise Scholar.")
    elif result == "friendship":
        print(f"Congratulations {name}! You have made a new friend!")
        print("You have became a leader.")
        print(f"Your name will be remembered as {name.title()} the Friend.")
    elif result == "poopie":
        print(f"Oh no {name}! You have landed in the poopie!")
        print("You smell like a piece of shet and now everybody is laughing at you.")
        print(f"Your name will be remembered as {name.title()} the Laughing Stock.")
    else:
        print(f"Your adventure ended in FAILURE, try again {name.title()}")

def play_game():
    name = get_player_name()
    display_welcome_message(name)
    result = forest_scene()
    if result == "light":
        result = light_scene(name)
    elif result == "cave":
        result = cave_scene(name)
    display_ending(name, result)

play_game()