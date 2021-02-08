def make_album(artist_name, album_title, song_numbers=None):
    music = {"artist": artist_name, "album": album_title}

    if song_numbers:
        music = {"artist": artist_name, "album": album_title, "songs": song_numbers}
    return music

while True:
    artist = input("\nEnter artist name: ")
    if artist == "quit":
        break
    album = input("\nEnter album's name: ")
    if album == "quit":
        break
    send = make_album(artist, album)
    print(send)
