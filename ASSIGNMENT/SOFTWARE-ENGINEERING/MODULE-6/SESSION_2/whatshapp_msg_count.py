# Build a WhatsApp-style unread messages counter: given a list unread_counts = [2, 0, 15, 120, 5], use a for loop to print '99+' if the count is greater than 99, otherwise print the actual count for each chat.
unread_counts = [2, 0, 15, 120, 5]
for i in unread_counts:
    if i > 99:
        print("99+")
    else :
        print(i)
        


