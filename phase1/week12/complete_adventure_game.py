import random
import os


class CompleteAdventure:
    def __init__(self):
        self.player_name = ""
        self.inventory_list = []
        self.health = 100
        self.score = 0
        self.visited_locations = []
        self.story_flags = {
            "met_wizard": False,
            "found_treasure": False,
            "defeated_dragon": False,
            "solved_riddle": False,
            "helped_village": False,
        }

    def get_player_info(self):
        self.player_name = input("What's your name, traveler?: ")
        while self.player_name == "":
            self.player_name = input("What's your name, traveler?: ")
        print(f"Welcome to the adventure game, {self.player_name.capitalize()}!")
        print("=" * 60)
        print("You are a normal villager living in Mamo Village, a peaceful settlement")
        print(
            "nestled in the valley between the Whispering Mountains and the Enchanted Forest."
        )
        print("Life has been quiet and simple here for generations.")
        print("=" * 60)
        print("The fate of Mamo Village rests in your hands...")
        print("=" * 60)

    def show_status(self):
        print("Noble Knight", self.player_name.capitalize())
        print("Health", self.health)
        print("Score", self.score)
        print("Inventory", self.inventory_list)
        print("Visited Locations", self.visited_locations)

    def add_item(self, item):
        self.inventory_list.append(item)
        print(f"Added {item} to Inventory")

    def remove_item(self, item):
        self.inventory_list.remove(item)
        print(f"Removed {item} from Inventory")

    def add_location(self, location):
        self.visited_locations.append(location)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(
                self.player_name.capitalize(),
                "has failed the mission and died GAME OVER",
            )
            return "death"
        else:
            print(f"You take {damage} damage, you have {self.health} health left")
            return "alive"

    def village_scene(self):
        print("=" * 60)
        print("You step out into the village of Mamo Village.")
        print("The cobblestone streets are bustling with villagers, but there's")
        print("an air of fear and worry hanging over everyone.")
        print("As you walk through the market square, an elderly woman approaches you,")
        print("her face etched with deep concern and desperation.")
        print("=" * 60)
        print("\nThe elderly woman, her hands trembling, grabs your arm gently.")
        print("'Please, young traveler! You must help us!' she pleads, her voice")
        print("filled with urgency. 'The ancient dragon Malachar has awakened from")
        print("its thousand-year slumber. It's been seen circling the mountains,'")
        print("she continues, tears welling in her eyes.")
        print("'My grandchildren are hiding in fear. The village needs a hero to")
        print("face this terrible beast before it destroys everything we hold dear.'")
        print("'Will you help us? Will you face the dragon and save Mamo Village?'")
        print("\nWhat do you do?")
        print("1. Accept the Quest")
        print("2. Ask for more Info")
        print("3. Decline and leave")
        print("=" * 60)
        choice = input("Enter your choice (1, 2, or 3): ")
        os.system('clear')

        if choice == "1":
            print("\n" + "=" * 60)
            print("The woman thanks you and hands you a healing potion and a map.")
            print("=" * 60)
            self.add_item("healing potion")
            self.add_item("map")
            self.score += 25
            self.story_flags["helped_village"] = True
            print(f"\nYou gained 25 points! Your score is now {self.score}.")
            return "accept quest"

        elif choice == "2":
            print("\n" + "=" * 60)
            print("'The dragon has been stealing our livestock!' the woman says.")
            print("'It lives in a cave high in the forbidden mountains.'")
            print("'Legends say it guards a great treasure.'")
            print("'Will you help us now?' the elderly woman asks.")
            print("1. Accept the Quest")
            print("2. Still decline")
            choice2 = input("What's your decision? 1 or 2: ")
            os.system('clear')
            if choice2 == "1":
                print(
                    "The woman thanks you and hands you a healing potion, a map and a magic sword."
                )
                self.add_item("healing potion")
                self.add_item("map")
                self.add_item("magic sword")
                self.score += 30
                self.story_flags["helped_village"] = True
                print(f"\nYou gained 30 points! Your score is now {self.score}.")
                return "accept quest"
            else:
                print("You leave the village and the villagers look disappointed")
                return "decline quest"

        else:
            print("You leave the village and the villagers look dissapointed")
            return "decline quest"

    def mountain_path(self):
        print("The forbidden mountains")
        self.add_location("Forbidden mountain")
        print(f"{self.player_name.capitalize()}, you begin your ascent to the mountains")
        print("The path is filled with dangers, you come to a fork in the road")
        print("1. Take left path (safer but longer)")
        print("2. Take right path (dangerous but shorter)")
        print("3. Climb the cliff (risky but direct)")
        choice3 = input("Which path do you choose? 1, 2 or 3: ")
        os.system('clear')
        # left path
        if choice3 == "1":
            print(
                "You took the safer path. You encounter a friendly mountain guide who helps you. He gives you advice about the dragon."
            )
            print("He gives you the mountain guide's advice.")
            self.add_item("mountain guide's advice")
            self.score += 15
            print(f"\nYou gained 15 points! Your score is now {self.score}.")
            return "safe path"
        # right path
        elif choice3 == "2":
            print("You took the dangerous path. You encounter a pack of wild wolves.")
            print("1. Fight the Wolves")
            print("2. Try sneaking past")
            print("3. Use healing potion to distract them")
            choice4 = input("What do you do? 1, 2 or 3: ")
            os.system('clear')

            if choice4 == "1":
                if "magic sword" in self.inventory_list:
                    print("You defeated the wolves!")
                    self.score += 30
                    print(f"\nYou gained 30 points! Your score is now {self.score}.")

                else:
                    print("You fight bravely, but take damage.")
                    player_state = self.take_damage(20)
                    if player_state == "death":
                        print("GAME OVER. You were eaten by the wolves.")
                        return "death"
                    else:
                        self.score += 20
                        print(
                            f"\nYou gained 20 points! Your score is now {self.score}."
                        )

            elif choice4 == "2":
                print("You successfully sneak past the wolves.")
                self.score += 25
                print(f"\nYou gained 25 points! Your score is now {self.score}.")

            else:
                if "healing potion" in self.inventory_list:
                    print("You use your healing potion to distract the wolves.")
                    self.remove_item("healing potion")
                    self.score += 35

                else:
                    print("You don't have a healing potion. The wolves attack you.")
                    player_state = self.take_damage(25)
                    if player_state == "death":
                        print("GAME OVER. You were eaten by the wolves.")
                        return "death"
                    else:
                        self.score += 15
                        print(
                            f"\nYou gained 15 points! Your score is now {self.score}."
                        )
            return "dangerous path"

        # cliff path
        else:
            print("You attempt to climb the cliff. It's very dangerous.")
            if random.random() < 0.6:
                print("You successfully climb the cliff")
                self.score += 40
                print(f"\nYou gained 40 points! Your score is now {self.score}.")
                return "cliff success"

            else:
                print("You fall from the cliff")
                player_state = self.take_damage(30)
                if player_state == "death":
                    print("GAME OVER, you fell off the cliff")
                    return "death"
                else:
                    self.score += 10
                    print(f"\nYou gained 10 points! Your score is now {self.score}.")
                return "cliff failure"

    def dragon_cave(self):
        print("The dragon's cave")
        self.add_location("dragon's cave")
        print("The cave is dark and you hear the dragons breathing from within")
        print("1. Enter the cave boldly")
        print("2. Sneak in quietly")
        print("3. Call out the dragon")
        choice5 = input("What do you want to do? 1, 2 or 3: ")
        os.system('clear')
        if choice5 == "1":
            print(
                "You march into the cave boldly, the dragon is surprised by your courage"
            )
            print("'Who dares enter my domain?' the dragon roars.")
            return self.dragon_encounter("bold")
        elif choice5 == "2":
            print(
                "You sneak quietly into the cave. You manage to get close to the dragon without being noticed."
            )
            print("You see it sleeping near a pile of treasure.")
            return self.dragon_encounter("sneaky")

        else:
            print("You call out to the dragon, 'Hello mighty dragon, I come in peace.'")
            print("The dragon looks at you with curiosity.")
            return self.dragon_encounter("diplomatic")

    def dragon_encounter(self, approach):
        if approach == "bold":
            print("The dragon looks at you with fierce interest.")
        elif approach == "sneaky":
            print("The dragon looks at you with curious interest.")
        else:
            print("The dragon looks at you with diplomatic interest.")
        print("'Why have you come here, mortal?' it asks.")
        print("1. Ask for treasure")
        print("2. Offer to help dragon")
        print("3. Challenge dragon to battle")
        print("4. Tell dragon about village problem")
        choice6 = input("How do you respond? 1, 2, 3 or 4: ")
        os.system('clear')
        if choice6 == "1":
            print("'The treasure is mine!' the dragon roars. It attacks you.")
            return self.dragon_battle()

        elif choice6 == "2":
            print("'Help me? How so?' the dragon asks.")
            print("You explain that you can help protect its treasure.")
            print(
                "The dragon is impressed by your offer. The dragon says, 'Very well, take some treasure as payment.'"
            )
            self.add_item("dragon's treasure")
            self.story_flags["found_treasure"] = True
            self.score += 100
            return "treasure ending"
        elif choice6 == "3":
            print("'You dare challenge me?' it roars.")
            print("It attacks you.")
            return self.dragon_battle()

        else:
            print(
                "You tell the dragon about the village suffering. 'I didn't know my hunting was causing such problems,' it says."
            )
            print(
                "'I will hunt in other areas from now on. As thanks for telling me, take this treasure.'"
            )
            self.add_item("dragon's gift")
            self.story_flags["found_treasure"] = True
            self.story_flags["defeated_dragon"] = True
            self.score += 150
            return "peaceful ending"

    def dragon_battle(self):
        print("Dragon battle!")
        print("The dragon attacks with fire breath.")
        if "magic sword" in self.inventory_list:
            print("You fight back with your magic sword. The battle is fierce.")
            if random.random() < 0.7:
                print("You defeated the dragon!")
                self.story_flags["defeated_dragon"] = True
                self.add_item("dragon's hoard")
                self.score += 200
                return "victory ending"
            else:
                print("The dragon is too powerful.")
                player_state = self.take_damage(50)
                if player_state == "death":
                    print("GAME OVER. The dragon has defeated you.")
                    return "death"
                else:
                    print("You barely escape with your life.")
                    return "defeat ending"
        else:
            print("You don't have a weapon. The dragon easily defeats you.")
            player_state = self.take_damage(60)
            if player_state == "death":
                print("GAME OVER, the dragon has defeated you")
                return "death"
            else:
                print("You barely escape with your life.")
                return "defeat ending"

    def determine_ending(self):
        print("Adventure complete")
        self.show_status()
        print(f"Your adventure has come to an end, {self.player_name.capitalize()}.")
        if self.story_flags["defeated_dragon"] and self.story_flags["found_treasure"]:
            print("You are a legendary hero! You defeated the dragon and found the treasure.")
            print("The village will sing songs of your victory. You are remembered as the greatest hero of Mamo Village.")
        elif self.story_flags["defeated_dragon"]:
            print("You are a dragon slayer. You defeated the dragon but didn't find the treasure.")
            print("You return to the village as a hero")

        elif self.story_flags["found_treasure"]:
            print("You are a treasure hunter.")
            print("You found the treasure and made peace with the dragon. You return to the village as a wealthy traveler.")
        elif self.story_flags["helped_village"]:
            print("You are a friend of the village. You helped them in their time of need. You may not have found the treasure, but you have their gratitude.")
        elif self.score >=100:
            print("You are a skilled adventurer. You had a successful adventure with many accomplishments.")
        else:
            print("You are a novice explorer. Your adventure was challenging, but you learned many lessons.")
        print(f"Your final score is {self.score}.")





player = CompleteAdventure()
player.get_player_info()
village_choice= player.village_scene()
if village_choice == "decline quest":
    print("You return home without adventure.")
else:
    mountain_choice = player.mountain_path()
    if mountain_choice == "death":
        print("You have died.")
    else:
        dragon_choice = player.dragon_cave()
        if dragon_choice == "death":
            print("You have died.")
           
player.determine_ending()

