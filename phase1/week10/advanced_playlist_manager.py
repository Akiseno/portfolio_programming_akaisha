import random
class Playlist:
    def __init__(self):
        self.history = []
        self.playlist = []
        self.current_index = 0
        self.is_shuffled = False
        self.original_order = []

    def add_song(self,title,artist,duration):
        self.playlist.append([title,artist,duration])

    def remove_song(self,title):
        for song in self.playlist:
            if song[0] == title:
                self.playlist.remove(song)
                return True
        return False

    def display_playlist(self):
        if len(self.playlist) == 0:
            return "Playlist is empty"
        result = []
        for i, song in enumerate(self.playlist, 1):
            title, artist, duration = song
            result.append(f"{i}. {title} - {artist} ({duration} min)")
        return "\n".join(result)

    def shuffle_playlist(self):
        if not self.is_shuffled:
            self.is_shuffled = True
            self.original_order = self.playlist.copy()
            random.shuffle(self.playlist)

    def unshuffle_playlist(self):
        self.playlist = self.original_order.copy()
        self.is_shuffled = False

    def play_next_song(self):
        if len(self.playlist) == 0:
            return None
        song = self.playlist.pop(0)
        self.history.append(song)
        return song

    def show_history(self):
        return self.history

    def get_stats(self):
        total_songs = len(self.playlist)
        total_duration = 0
        for song in self.playlist:
            total_duration += song[2]  # duration is at index 2
        history_count = len(self.history)
        return {
            "total_songs": total_songs,
            "total_duration": total_duration,
            "songs_played": history_count,
            "is_shuffled": self.is_shuffled
        }
    
    def display_stats(self):
        stats = self.get_stats()
        result = []
        result.append("=" * 30)
        result.append("Playlist Statistics")
        result.append("=" * 30)
        result.append(f"Total songs: {stats['total_songs']}")
        result.append(f"Total duration: {stats['total_duration']} min")
        result.append(f"Songs played: {stats['songs_played']}")
        result.append(f"Shuffle status: {'Shuffled' if stats['is_shuffled'] else 'Original order'}")
        result.append("=" * 30)
        return "\n".join(result)


def demo_playlist_manager():
    playlist = Playlist()
    playlist.add_song("song1", "artist1", 3)
    playlist.add_song("song2", "artist2", 4)
    playlist.add_song("song3", "artist3", 5)
    print(playlist.display_playlist())
    print(playlist.display_stats())
    playlist.shuffle_playlist()
    print(playlist.display_playlist())
    print("--------------------------------")
    playlist.unshuffle_playlist()
    print(playlist.display_playlist())


demo_playlist_manager()
