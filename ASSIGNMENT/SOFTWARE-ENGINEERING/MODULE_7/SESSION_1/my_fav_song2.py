# Write a Python script that opens the my_fav_songs.txt file in read ('r') mode and prints each song name to the console with its line number (like a playlist).

with open("my_fav_song.txt","r") as f:
    count = 0
    for line in f:
        count+=1
        print(count,line)