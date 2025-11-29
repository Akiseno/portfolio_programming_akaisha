import os

def forest_adventure():
    os.system('clear')
    print("Welcome to the forest adventure!")
    print ("You are a new Knight in training and you are tasked with finding the treasure of the forest.")
    print("You must state your name before you can start your journey, otherwise the town wont know who to praise if you succeed.")
    name = input("Enter your name: ")
    print(f"Your journey begins now, {name}!")
    print("You are in a forest. You see 3 paths in front of you.")
    print("1. Path of Light")
    print("2. Path of Darkness")
    print("3. Hidden Path")
    path = input("Which path do you choose? (1, 2, 3): ")
    if path == "1":
        print("--------------------------------")
        print("You choose the path of light. You see a glowing light in the distance.")
        print("You follow the glowing light, everything starts to get darker and darker.")
        print("You hear a noise in the distance, you start to run.")
        print("As you are running, an unknown entity starts to chase you.")
        print("You see 2 ways and only one will lead you to safety.")
        print("1. The left path")
        print("2. The right path")
        path = input("Which path do you choose? (1, 2): ")
        if path == "1":
            print("--------------------------------")
            print("You choose the left path. You see sunlight in the distance.")
            print("You follow the sunlight, you see a clearing in the distance.")
            print("You look back and see that the entity has disappeared.")
            print("You are safe and you have found the treasure.")
            return "treasure"
        elif path == "2":
            print("--------------------------------")
            print("You choose the right path. You chose the path leading to a dead end.")
            print("You turn around and see the entity getting closer and closer.")
            print("You know you have no where to go so you accept your fate.")
            return "end"
        else:
            print("--------------------------------")
            print("You didnt choose a valid path a time traveler has found you and has made you go back to phase 1.")
            forest_adventure()
    elif path == "2":
        print("--------------------------------")
        print("You choose the path of darkness. You see a dark cave in the distance.")
        print("You enter the cave and you see a dragon.")
        print("The dragon is sleeping, you start to walk closer to the dragon.")
        print("The dragon wakes up and asks you why you are there.")
        print("You tell the dragon that you are lost and you are looking for the treasure.")
        print("The dragon tells you that the treasure is in the cave, but you need to solve a riddle to get it.")
        print("The riddle is: What needs to be broken before you can use it?")
        print("1. An egg")
        print("2. A glowstick")
        print("3. A glass")
        riddle = input("Enter your answer: ")
        if riddle == "1":
            print("--------------------------------")
            print("You answer the riddle correctly, the dragon gives you the treasure.")
            return "treasure"
        elif riddle == "2":
            print("--------------------------------")
            print("The dragon says 'You are correct, but its not the answer im looking for.'")
            return "riddle"
        elif riddle == "3":
            print("--------------------------------")
            print("You answer the riddle incorrectly, the dragon consumes you.")
            return "end"
        else:
            print("--------------------------------")
            print("You didnt choose a valid path a time traveler has found you and has made you go back to phase 1.")
            forest_adventure()
    elif path == "3":
        print("--------------------------------")
        print("You choose the hidden path. You see a hidden cave in the distance.")
        print("You enter the cave and you see a hidden door.")
        print("You enter the door and you see a hidden room.")
        print("The room is filled with ancient symbols and three mysterious objects.")
        print("Each object seems to hold a different power. Which one do you choose?")
        print("1. The glowing crystal")
        print("2. The ancient scroll")
        print("3. The golden key")
        choice = input("Which object do you choose? (1, 2, 3): ")
        if choice == "1":
            print("--------------------------------")
            print("You pick up the glowing crystal. It begins to pulse with energy.")
            print("The crystal reveals a hidden passage behind the wall.")
            print("You follow the passage and discover the treasure!")
            return "treasure"
        elif choice == "2":
            print("--------------------------------")
            print("You pick up the ancient scroll. As you read it, the room starts to shake.")
            print("The scroll contains a powerful spell that transports you away from the treasure.")
            print("You find yourself back at the start of the forest, empty-handed.")
            return "end"
        elif choice == "3":
            print("--------------------------------")
            print("You pick up the golden key. It fits perfectly into a lock on the treasure chest.")
            print("The chest opens, revealing the treasure inside!")
            return "treasure"
        else:
            print("--------------------------------")
            print("You didnt choose a valid path a time traveler has found you and has made you go back to phase 1.")
            forest_adventure()
    else:
       
        print("--------------------------------")
        print("You didnt choose a valid path a time traveler has found you and has made you go back to phase 1.")
        forest_adventure()





def play_game():
    start = forest_adventure()
    if start == "treasure":
        print("--------------------------------")
        print("You have found the treasure! You are remembered as a hero, everyone in the whole wide world knows your name!")
        return "end"
    elif start == "riddle":
        print("--------------------------------")
        print("You have unfortunateley failed the riddle! But you are now a legend in the making, everyone in the whole wide world knows your name!")
        return "end"
    elif start == "end":
        print("--------------------------------")
        print("You have died! You are a failure! Your name will be forgotten and you will be remembered as a failure!")
        return "end"

    
play_game()