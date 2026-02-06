def song_source(songs):
    for song in songs:
        yield song

def decode(songs):
    for song in songs:
        yield f"Decoded({song})"

def play(songs):
    for song in songs:
        yield f"Playing {song}"


songs = ["Song1", "Song2", "Song3"]

player = play(decode(song_source(songs)))

for output in player:
    print(output)
