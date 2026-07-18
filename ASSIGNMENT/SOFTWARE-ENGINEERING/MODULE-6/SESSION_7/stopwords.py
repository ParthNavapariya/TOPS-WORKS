# Modify your word frequency program to ignore common stopwords like 'the', 'and', 'in', 'of', 'a', 'to', 'is' when counting word frequencies.<br><br><em><strong>Constraint:</strong> Use a list of stopwords and filter them out before counting.</em>

word = "the cat is in the gardern"
stopword = ["the","is","in","the","garden"]
result = word.split()
final = []

for i in result:
    if i not in stopword:
        final.append(i)
print(final)


