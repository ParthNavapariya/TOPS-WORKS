# Write a function read_next_line(filename) that opens a file, moves the file pointer to the 20th byte using seek(), and prints the next line from that position.<br><br><em><strong>Hint:</strong> Use seek(20) before calling readline().</em>


def read_next_line():
    with open("lyrics.txt","r") as filename:
        filename.seek(20)
        print(filename.readline())

read_next_line()


