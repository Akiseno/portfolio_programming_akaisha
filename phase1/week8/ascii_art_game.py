import random
def roll_dice(number_of_dice):
    return random.randint(1, number_of_dice)
def draw_ascii_dice(number):
    if number == 1:
        print("+---------+")
        print("|         |")
        print("|    o    |")
        print("|         |")
        print("+---------+")
    elif number == 2:
        print("+---------+")
        print("| o       |")
        print("|         |")
        print("|       o |")
        print("+---------+")
    elif number == 3:
        print("+---------+")
        print("| o       |")
        print("|    o    |")
        print("|       o |")
        print("+---------+")
    elif number == 4:
        print("+---------+")
        print("| o     o |")
        print("|         |")
        print("| o     o |")
        print("+---------+")
    elif number == 5:
        print("+---------+")
        print("| o     o |")
        print("|    o    |")
        print("| o     o |")
        print("+---------+")
    elif number == 6:
        print("+---------+")
        print("| o     o |")
        print("| o     o |")
        print("| o     o |")
        print("+---------+")


def get_dice_lines(number):
    """Convert a die value to its ASCII representation"""
    if number == 1:
        return ["+---------+", "|         |", "|    o    |", "|         |", "+---------+"]
    elif number == 2:
        return ["+---------+", "| o       |", "|         |", "|       o |", "+---------+"]
    elif number == 3:
        return ["+---------+", "| o       |", "|    o    |", "|       o |", "+---------+"]
    elif number == 4:
        return ["+---------+", "| o     o |", "|         |", "| o     o |", "+---------+"]
    elif number == 5:
        return ["+---------+", "| o     o |", "|    o    |", "| o     o |", "+---------+"]
    elif number == 6:
        return ["+---------+", "| o     o |", "| o     o |", "| o     o |", "+---------+"]

def draw_multiple_dice(dice_values):
    """Display multiple dice side by side"""
    all_dice_lines = [get_dice_lines(dice) for dice in dice_values]
    
    # Print each line across all dice
    for line_num in range(5):
        line = "  ".join(dice_lines[line_num] for dice_lines in all_dice_lines)
        print(line)

while True:
    try:
        num_dice = int(input("\nHow many dice would you like to roll? "))
        if num_dice < 1:
            print("Please enter a number greater than 0.")
            continue
    except ValueError:
        print("Please enter a valid number.")
        continue
    
    # Roll all the dice
    dice_values = [roll_dice(6) for _ in range(num_dice)]
    total = sum(dice_values)
    
    # Display all dice
    draw_multiple_dice(dice_values)
    
    # Show the calculation
    dice_string = " + ".join(map(str, dice_values))
    print(f"\nTotal: {dice_string} = {total}")
    
    roll_again = input("\nRoll again? (y/n): ")
    if roll_again.lower() != 'y':
        break

print("Thanks for playing!")