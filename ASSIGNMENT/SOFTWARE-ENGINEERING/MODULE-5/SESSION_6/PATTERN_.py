# Write a program using a while loop to print a right-angled triangle star pattern with 5 rows, like:
# *
# **
# ***
# ****
# *****


i = 1
while i <= 5:
     j = 1
     while j <= i:
        print("*",end = "")
        j+=1
     print()
     i += 1
     