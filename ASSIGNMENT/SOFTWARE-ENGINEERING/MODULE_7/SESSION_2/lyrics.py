# Create a Python script that opens a file called lyrics.txt and prints the file pointer's current position using tell() before and after reading the first 10 characters.


with open("lyrics.txt","r") as f:
    print(f.tell())
    print(f.read(10))
    print(f.tell())