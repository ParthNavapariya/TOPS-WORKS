# Given a file called playlist.txt containing song names (one per line), write code to jump to the start of the third song using seek() and readline(), then print only that song's name.<br><br><em><strong>Constraint:</strong> Do not read the whole file into memory at once.</em>

with open("playlist.txt","r") as f:
    f.seek(0)
    f.readline()
    f.readline()
    third_song = f.readline() 
    print(third_song.strip())
