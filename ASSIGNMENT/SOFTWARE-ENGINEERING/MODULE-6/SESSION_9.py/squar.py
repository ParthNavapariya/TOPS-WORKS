# Write a lambda function to calculate the square of a number and use it to print the squares of numbers from 1 to 5.
squ = lambda i:i*i
for i in range(1,6):
    print(squ(i))
