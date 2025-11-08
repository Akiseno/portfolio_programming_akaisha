import random
def music_library():
    songs = [["song1", "artist1", "pop", 180], ["song2", "artist2", "rock", 190], ["song3", "artist3", "jazz", 200], ["song4", "artist4", "blues", 210], ["song5", "artist5", "country", 220], ["song6", "artist6", "hip hop", 230], ["song7", "artist7", "electronic", 240], ["song8", "artist8", "classical", 250], ["song9", "artist9", "folk", 260], ["song10", "artist10", "latin", 270]]
    return songs

def display_songs(songs):
    print("available songs:")
    for song in songs:
        print(song[0], "by", song[1], "from", song[2], "is", song[3], "seconds long")

def create_randome_playlist(all_songs, num_songs=5):
    playlist = random.sample(all_songs, num_songs)
    return playlist

def create_genre_playlist(all_songs, genre):
    playlist = [song for song in all_songs if song[2] == genre]
    return playlist

def create_duration_playlist(all_songs, duration):

    playlist = [song for song in all_songs if song[3] <= duration]
    return playlist

def create_artist_playlist(all_songs, artist):
    playlist = [song for song in all_songs if song[1] == artist]
    return playlist

def display_playlist(playlist):
    print("playlist:")
    for song in playlist:
        print(song[0], "by", song[1], "from", song[2], "is", song[3], "seconds long")

def get_available_genres(songs):
    genres = set(song[2] for song in songs)
    return genres

def get_available_artists(songs):
    artists = set(song[1] for song in songs)
    return artists



songs = music_library()
print("*"*30)
display_songs(songs)
print("*"*30)
playlist = create_randome_playlist(songs, 3)
display_playlist(playlist)
print("*"*30)
playlist = create_genre_playlist(songs, "pop")
display_playlist(playlist)
print("*"*30)
playlist = create_duration_playlist(songs, 200)
display_playlist(playlist)