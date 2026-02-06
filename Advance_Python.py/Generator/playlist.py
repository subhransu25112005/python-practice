def playlist(songs):
    for song in songs:
        yield song


songs = [
    "Shape of You",
    "Believer",
    "Perfect"
]

player = playlist(songs)

for song in player:
    choice = input(f"▶ Playing {song}. Next? (y/q): ")
    if choice == 'q':
        break
