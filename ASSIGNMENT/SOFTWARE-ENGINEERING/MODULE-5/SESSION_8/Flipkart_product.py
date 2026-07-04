# Given a Flipkart product description string, write a Python script that extracts and prints the first word, last word, and the total number of words using string methods split(), indexing, and len().


flipkart_discription = "Experience crystal-clear sound with these Wireless Bluetooth Earbuds. Designed for everyday use, they deliver powerful bass, stable Bluetooth 5.3 connectivity, and a comfortable fit for long listening sessions. The compact charging case provides up to 40 hours of battery"
splitz = flipkart_discription.split()
fist = splitz[0]
print(fist)
last = splitz[-1]
print(last)
lens = len(splitz)
print(lens)
print(splitz)