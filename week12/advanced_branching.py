class AdventureState:
    def __init__(self):
        self.inventory = []
        self.has_key = False
        self.has_torch = False
        self.has_sword = False
        self.health = 100
        self.score = 0
        self.visited_locations = []
    def show_status(self):
        print(f"Inventory: {self.inventory}")
        print(f"Has Key: {self.has_key}")
        print(f"Has Torch: {self.has_torch}")
        print(f"Has Sword: {self.has_sword}")
        print(f"Health: {self.health}")
        print(f"Score: {self.score}")
        print(f"Visited Locations: {self.visited_locations}")

def adventure_castle():
    game_state = AdventureState()
    game_state.visited_locations.append("castle")
    print("The castle has 2 entrances")
    print("1. The main gate(guarded)")
    print("2. The secret passage(hidden)")
    path = input("Enter your choice: ")
    if path.lower() == "1":
        print("--------------------------------")
        print("You approach the main gate. Two armored guards stand watch, their eyes scanning the area.")
        print("As you get closer, one guard steps forward and raises his hand.")
        print("'Halt! Identify youself, traveler.'")
        print("Show me your Identification.")
        print("1. Show fake ID")
        print("2. Attempt to sneak past")
        print("3. Ask about castle")
        choice = input("Enter your choice: ")
        if choice.lower() == "1":
            print("--------------------------------")
            print("You nervously pull out a fake ID you prepared earlier.")
            print("The guard examines it carefully, squinting at the details.")
            print("After a tense moment, he nods and says, 'Everything seems in order.'")
            print("The guards think your a guard aswell dues to your fake ID so they give you a key to the castle rooms.")
            print("The guards step aside and allow you to pass through the main gate.")
            print("You breathe a sigh of relief as you enter the main hall.")
            game_state.score += 20
            game_state.visited_locations.append("main hall")
            game_state.has_key = True
            return game_state
        elif choice.lower() == "2":
            print("--------------------------------")
            print("You try to quickly dart past the guards while they're distracted.")
            print("Unfortunately, one guard spots your movement and shouts, 'Stop!'")
            print("The guards catch you and you're forced to explain yourself.")
            print("They're suspicious but eventually let you through after a stern warning.")
            print("You enter the main hall, but your health has taken a hit from the scuffle.")
            game_state.score += 10
            game_state.health -= 15
            game_state.visited_locations.append("main hall")
            return game_state
        elif choice.lower() == "3":
            print("--------------------------------")
            print("You decide to be honest and ask the guards about the castle.")
            print("'I'm a curious traveler. What can you tell me about this place?'")
            print("The guards are impressed by your directness and respect your honesty.")
            print("They share some information about the castle and even give you a small map.")
            print("They welcome you inside with a friendly nod.")
            print("You enter the main hall feeling confident and well-informed.")
            game_state.score += 25
            game_state.inventory.append("castle map")
            game_state.visited_locations.append("main hall")
            return game_state
        else:
            print("Invalid choice. The guards become impatient.")
            print("You're turned away from the gate.")
            game_state.health -= 20
            return game_state
    elif path.lower() == "2":
        print("--------------------------------")
        print("You search around the castle walls, looking for the secret passage.")
        print("After some investigation, you find a hidden door covered in ivy.")
        print("You push it open and enter a dark, narrow passage.")
        print("The air is musty and you can hear the sound of dripping water.")
        print("It's pitch black inside. You can barely see your hand in front of your face.")
        print("1. Search for a torch")
        print("2. Make your way through in the darkness")
        choice = input("Enter your choice: ")
        if choice.lower() == "1":
            print("--------------------------------")
            print("You feel along the walls, searching for anything that might help you see.")
            print("Your fingers brush against something wooden and cylindrical.")
            print("You've found an old torch! You also discover a flint and steel nearby.")
            print("After a few attempts, you manage to light the torch.")
            print("The flickering flame illuminates the passage, revealing old traps and obstacles.")
            print("You carefully navigate through the secret passage, avoiding danger.")
            print("You emerge into a hidden chamber deep within the castle, safe and prepared.")
            print("No one has seen you enter - you have the element of surprise!")
            game_state.score += 30
            game_state.has_torch = True
            game_state.inventory.append("torch")
            game_state.visited_locations.append("hidden chamber")
            return game_state
        elif choice.lower() == "2":
            print("--------------------------------")
            print("You decide to brave the darkness and feel your way forward.")
            print("You stumble several times, scraping your knees and hands on rough stone.")
            print("Suddenly, you hear a click beneath your foot - you've triggered a trap!")
            print("You quickly jump back, but not before a dart grazes your arm.")
            print("Despite the setback, you continue forward, more carefully now.")
            print("You eventually emerge into a hidden chamber, battered but determined.")
            print("No one has seen you enter - you have the element of surprise!")
            game_state.score += 20
            game_state.health -= 25
            game_state.visited_locations.append("hidden chamber")
            return game_state
        else:
            print("Invalid choice. You hesitate too long in the darkness.")
            print("You decide to turn back and leave the passage.")
            game_state.health -= 10
            return game_state
    else:
        print("Invalid choice. Please enter 1 or 2.")
        game_state.health -=30
        return game_state

game_state = adventure_castle()
game_state.show_status()
if "main hall" in game_state.visited_locations:
    print("\n" + "="*50)
    print("You stand in the main hall, taking in the magnificent architecture.")
    print("The main hall is vast, with beautiful gardens and fountains.")
    print("You see 3 doors")
    print("1. treasure room(locked)")
    print("2. library")
    print("3. Armory")
    door = input("Which door do you choose: ")
    if door == "1":
        if game_state.has_key:
            print("You use the key to open the treasure room")
            print("You find a chest full of gold")
            game_state.score +=100
            game_state.visited_locations.append("treasure room")    

        else: 
            print("The door is locked and you need a key.")
            print("You go back to the main hall.")
    elif door == "2":
         print("You enter the library and find ancient books")
         print("You learn new skills.")
         game_state.score +=50
         game_state.visited_locations.append("library")
         game_state.inventory.append ("ancient books")
    elif door == "3":
        print ("You enter the Armory and you find a magical sword.")
        game_state.has_sword = True
        game_state.score +=70
        game_state.visited_locations.append("Armory")
        game_state.inventory.append("sword")
    else:
        print("--------------------------------")
        print("You stand confused in the main hall, staring at the doors.")
        print("You're not sure which door to choose, and you hesitate for too long.")
        print("A guard notices your indecision and approaches you.")
        print("'You seem lost, traveler. Perhaps you should make up your mind.'")
        print("The guard escorts you back to reconsider your options.")
        print("You lose some time, but you're still in the main hall.")
        print("--------------------------------")
        game_state.health -= 5
        game_state.score -= 10

game_state.show_status()


       

    