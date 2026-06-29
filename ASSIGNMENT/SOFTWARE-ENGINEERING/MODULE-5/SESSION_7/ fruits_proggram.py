# Write a Python program that loops through a list of fruits: ['Apple', 'Banana', 'Mango', 'Orange'] and prints each fruit, but uses the continue statement to skip printing 'Banana'.


fruits = ['Apple','Banana','Mango','Orange']
for i in fruits:
    if i == "Banana":
        continue
    print(i)

