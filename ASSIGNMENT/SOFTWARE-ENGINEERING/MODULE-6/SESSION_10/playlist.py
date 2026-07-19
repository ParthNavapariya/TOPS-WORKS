# Create a new Python file called playlist.py and define a function add_song(song_name, playlist) that adds a song to the playlist list and returns the updated list.

def add_song(song_name,playlist):
        playlist.append(song_name)
        return playlist
final_playlist = []
print(add_song("beliver",final_playlist))


def remove_Song(song_name,playlist):
        if song_name in playlist:
         playlist.remove(song_name)

        return playlist

def display_playlist(playlist):
      count = 0
      for i in playlist:
            print(count,i)
            count+=1
      
