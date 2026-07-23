# Write a Python function get_song_duration that takes a song name and returns its duration from a predefined dictionary. Use a try-except block to handle the case where the song is not found and print 'Song not found on Spotify!'.


def get_Song_duration(dictonary):
       
       user = input("Enter song name")
       
    
       try:
           final = dictonary[user]
           return final
       except:
             print("Song not found on Spotify!")

dicti = {
    "beliver":23,
    "life of":25,
    "standup":21
}
print(get_Song_duration(dicti))