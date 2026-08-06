# Write a Python script using pymysql to fetch and display all playlists from the music_stream database where song_count is greater than 10, showing the playlist name and song_count only.


import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="rootroot",
    database="music_stream"
)
if conn:
    print("connection succesfully")

myCursor = conn.cursor()

sql = "SELECT name,song_count FROM playlist WHERE song_count > 10"
myCursor.execute(sql)

mylst = myCursor.fetchall()

print(mylst)

conn.commit()
conn.close()