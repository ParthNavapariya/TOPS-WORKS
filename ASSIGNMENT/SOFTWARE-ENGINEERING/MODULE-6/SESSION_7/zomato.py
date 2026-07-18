# Create a program that reads a short review (multi-line string) about your favorite food delivery app (like Zomato or Swiggy) and counts the frequency of each word, displaying the results as a dictionary.<br><br><em><strong>Hint:</strong> Convert all words to lowercase and remove punctuation for accurate counting.</em>

zomato = "Zomato's, paren"
lower = zomato.lower()
final = lower.replace(",","")
words = final.split()
count = {}
for i in words:
     if i in count:
          count[i]=+1
     else:
          count[i] = 1
print(count) 