class AdventureGame:
    def __init__(self):
        self.name = ""
        self.result = ""
        self.inventory = []
        self.health = 100
        self.score = 0 
        self.current_location = "forest"


    def get_player_info(self):
        self.name = input("Enter your name: ")
        self.age = input("Enter your age: ")
        self.favorite_color = input("Enter your favorite color: ")
        print(f"""Welcome to the adventure game, {self.name}! You are {self.age} years old and your favorite color is {self.favorite_color}.
        You hear stories about a magical forest where anything can happen.
        Today you decided to explore this mysterious place. Your journey begins now...""")

    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"You have added {item} to your inventory.")

    def show_status(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Favorite Color: {self.favorite_color}")
        print(f"Inventory: {self.inventory}")
        print(f"Health: {self.health}")
        print(f"Score: {self.score}")
        print(f"Current Location: {self.current_location}")

    

    def forest_entrance(self):
        print("You are in a forest. You see a path to the left and a path to the right.")
        print("Which path do you choose?")
        print("1. Path of Light")
        print("2. Path of Darkness")
        print("3. Path of Adventure")
        path = input("Enter your choice: ")
        if path.lower() == "1":
            result = self.light_path()
            self.result = result
            return result
        elif path.lower() == "2":
            result = self.darkness_path()
            self.result = result
            return result
        elif path.lower() == "3":
            result = self.adventure_path()
            self.result = result
            return result
        else:
            print("Invalid choice. Please enter left or right.")
            self.result = "end"
            return "end"

    def light_path(self):
        print("The Path of Light")
        print(f"{self.name}, you approach the glowing light.")
        print("You follow the glowing mushroom.")
        print(f"It leads you to a clearing with a magical fountain, the fountain has 3 sparkling gems.")
        print("1. Ruby.")
        print("2. Sapphire.")
        print("3. Emerald.")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("You are granted a Ruby.")
            self.add_to_inventory("ruby")
            self.score += 50
            print(f"You feel courageous and ready to face the challenges ahead.")
            return "courage"
        elif choice == "2":
            print("You are granted a Sapphire.")
            self.add_to_inventory("sapphire")
            self.score += 50
            print(f"You feel wise and knowledgeable.")
            return "wisdom"
        elif choice == "3":
            print("You are granted an Emerald.")
            self.add_to_inventory("emerald")
            self.score += 50
            print(f"You feel friendly and ready to make friends.")
            return "friendship"
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            return "end"

    def darkness_path(self):
        print("The Path of Darkness")
        print(f"{self.name}, You venture into the dark shadows.")
        print("You hear a mysterious voice saying: Who dare enters my domain?.")
        print("1. Answer confidently.")
        print("2. Answer quietly.")
        print("3. Dont answer.")
        choice = input("Enter your choice: ")
        if choice.lower() == "1":
            print("The voice responds: I admire your Courage. A shadowy figure emerges and gives you a shadow cloak")
            self.add_to_inventory("shadow cloak")
            self.score += 75
            return "shadow_cloak"

        elif choice.lower() == "2":
            print("The voice responds: I appreciate your respect. You recieve a whispering stone")
            self.add_to_inventory("whispering stone")
            self.score += 60
            return "whispering_stone"
        elif choice.lower() == "3":
            print("The voice responds: Silence is also an answer. Recieve a silent charm")
            self.add_to_inventory("silent charm")
            self.score += 40
            return "silent_charm"
        else:
            print("Invalid choice.")
            return "end"

    def adventure_path(self):
        print("Adventure Path")
        print("You are on a path of adventure.")
        print("You encounter a Sphinx")
        print("The Sphinx asks you a riddle.")
        print("What has keys but no locks, space but no room, you can enter but not go inside?")
        print("1. A piano")
        print("2. A keyboard")
        print("3. A map")
        
        path = input("Enter your choice: ")
        if path.lower() == "1":
            print("You answer the riddle incorrectly, you get a music box as a consolation prize.")
            self.add_to_inventory("music box")
            self.score += 30
            return "music_box"
        elif path.lower() == "2":
            print("You answer the riddle correctly, the Sphinx gives you a riddle master crown as a reward.")
            self.add_to_inventory("riddle master crown")
            self.score += 100
            return "riddle_master_crown"
        elif path.lower() == "3":
            print("You answer the riddle incorrectly, the Sphinx gives u a compass.")
            self.add_to_inventory("compass")
            self.score += 20
            return "compass"
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            return "end"


    def display_ending(self):
        print(f"Adventure complete, {self.name}!")
        print(f"Your final score is {self.score}")
        print(f"Your inventory is {self.inventory}")
        print(f"Your health is {self.health}")
        if self.score >= 100:
            print(f"Congratulations {self.name}! You have won the game!")
            print("You are now a legendary adventurer.")
            print(f"Your name will be remembered as {self.name.title()} the Legendary Adventurer.")
        elif self.score >= 75:
            print(f"Congratulations {self.name}! You have won the game!")
            print("You are now a expert adventurer.")
            print(f"Your name will be remembered as {self.name.title()} the Expert Adventurer.")
        elif self.score >= 50:
            print(f"Congratulations {self.name}! You have won the game!")
            print("You are now a skilled adventurer.")
            print(f"Your name will be remembered as {self.name.title()} the Skilled Adventurer.")
        else:
            print(f"Congratulations {self.name}! You have won the game!")
            print("You are now a novice adventurer.")
            print(f"Your name will be remembered as {self.name.title()} the Novice Adventurer.")
        
        


game = AdventureGame()
game.get_player_info()
game.forest_entrance()
game.display_ending()