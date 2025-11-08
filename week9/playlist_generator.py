import random
def generate_playlist():
    songs = [["song1", "artist1", "album1", 180], ["song2", "artist2", "album2", 190], ["song3", "artist3", "album3", 200], ["song4", "artist4", "album4", 210], ["song5", "artist5", "album5", 220], ["song6", "artist6", "album6", 230], ["song7", "artist7", "album7", 240], ["song8", "artist8", "album8", 250], ["song9", "artist9", "album9", 260], ["song10", "artist10", "album10", 270]]
    return songs

def display_songs(songs):
    print("available songs:")
    for song in songs:
        print(song[0], "by", song[1], "from", song[2], "is", song[3], "seconds long")

def create_randome_playlist(all_songs, num_songs=5):
    playlist = random.sample(all_songs, num_songs)
    return playlist

def display_playlist(playlist):
    print("playlist:")
    for song in playlist:
        print(song[0], "by", song[1], "from", song[2], "is", song[3], "seconds long")

songs = generate_playlist()
display_songs(songs)
playlist = create_randome_playlist(songs, 3)
display_playlist(playlist)