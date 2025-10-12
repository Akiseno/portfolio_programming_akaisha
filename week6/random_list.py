import random
favorite_songs = ["song1", "song2", "song3", "song4", "song5"]
print(random.choice(favorite_songs))

random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))
print(random_numbers)