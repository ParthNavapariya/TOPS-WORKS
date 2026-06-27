
# 5.
# Create a program that uses a while loop to print a pyramid star pattern with 4 rows, so the output looks like BookMyShow's seat rows:
# *
# ***
# *****
# *******<br><br><em><strong>Hint:</strong> Use two nested while loops: one for spaces, one for stars.</em>


i = 1
while i <= 8:
    j = 1
    while j <= i:
        print("*", end=" ")
        j+=1
    print()
    i+=2


