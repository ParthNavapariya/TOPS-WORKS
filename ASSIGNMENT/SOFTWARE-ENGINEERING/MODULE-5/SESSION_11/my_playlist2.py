# Add a new song and its duration to your my_playlist dictionary, then update the duration of one existing song.

my_playlist = {
    "miles davis so what":4.12,
    "miles, davis so what":4.5,
    "weezer, 'buddy holly":3.4
}

my_playlist["Santana, ‘Oye Como Va’"] = 4.1
print(my_playlist)

my_playlist.update({"weezer, 'buddy holly":4.0})
print(my_playlist)