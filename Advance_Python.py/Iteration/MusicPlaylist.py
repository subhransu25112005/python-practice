class MusicPlaylist:
    def __init__(self, songs):
        self.songs = songs
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.songs):
            raise StopIteration
        song = self.songs[self.index]
        self.index += 1
        return song


# ---- MAIN PROGRAM ----
playlist = [
    "Shape of You - Ed Sheeran",
    "Believer - Imagine Dragons",
    "Perfect - Ed Sheeran",
    "Kesariya - Arijit Singh",
    "On My Way - Alan Walker"
]

player = MusicPlaylist(playlist)

print("\n🎧 Welcome to Python Music Player 🎧")

for song in player:
    print(f"\n▶ Now Playing: {song}")
    choice = input("Press N for next song or Q to quit: ").lower()

    if choice == 'q':
        print("⏹ Music stopped by user")
        break

print("\n🎵 Playlist finished. Thanks for listening!")
