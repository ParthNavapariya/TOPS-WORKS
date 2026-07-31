# Create a random_playlist.py script that uses the random module to shuffle a list of 5 of your favorite songs (just song names as strings) and prints the shuffled playlist each time you run it.


import random
from song import song_list
random.shuffle(song_list)

for i in song_list:
    print(i)
