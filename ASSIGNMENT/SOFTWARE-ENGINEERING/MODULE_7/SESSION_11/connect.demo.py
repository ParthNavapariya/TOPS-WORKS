# Install the pymysql package in your Python environment and write a script connect_demo.py that connects to a local MySQL server using your credentials and prints 'Connection successful' if the connection is established.
import playlist

conn = playlist.connect(
    host = "localhost",
    user = "root",
    password="rootroot",
    database="SCHOOL_DB"

)
if conn :
    print("Connection successful")

