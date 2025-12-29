import random
def roll_dice():
    return random.randint(1, 6)

def flip_coin():
    return random.choice(["heads", "tails"])

def get_random_number(min, max):
    return random.randint(min, max)

dice = roll_dice()
coin = flip_coin()
number = get_random_number(1, 10)

print("The dice is", dice)
print("The coin is", coin)
print("The number is", number)
