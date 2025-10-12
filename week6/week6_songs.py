import random
favorite_songs = ["song1", "song2", "song3", "song4", "song5"]
print(random.choice(favorite_songs))

favorite_songs.append("song6")
print(favorite_songs)

favorite_songs.pop(2)
print(favorite_songs)

favorite_songs.remove("song5")
print(favorite_songs)
