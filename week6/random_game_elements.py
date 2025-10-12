import random
weapons = ["sword", "bow", "axe", "spear", "mace"]
armors = ["helmet", "chestplate", "leggings", "boots"]
enemies = ["orc", "troll", "dragon", "giant", "wraith"]

#random character generator

def generate_character():
    weapon = random.choice(weapons)
    armor = random.choice(armors)
    enemy = random.choice(enemies)
    character = {
        "weapon": weapon,
        "armor": armor,
        "enemy": enemy
    }
    return character

print(generate_character())