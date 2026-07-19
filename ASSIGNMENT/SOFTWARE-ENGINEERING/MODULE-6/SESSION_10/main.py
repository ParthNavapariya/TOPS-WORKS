# In a separate file main.py, import the add_song function from playlist.py and use it to add three songs ('Kesariya', 'Shape of You', 'Believer') to an empty playlist, then print the final playlist.

import playlist

my_playlist = []

final = playlist.add_song("Kesariya",my_playlist)
print(final)

print(playlist.add_song("Shape of You",my_playlist))

print(playlist.add_song("Believer",my_playlist))

print(my_playlist)

print(playlist.remove_Song("Shape of You",my_playlist))

print(playlist.display_playlist(my_playlist))