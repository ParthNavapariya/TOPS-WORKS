# Given a list of messages: ['Hi', 'Spam', 'Hello', 'Spam', 'How are you?'], build a loop that prints only non-spam messages by skipping any message that is 'Spam' using continue, and stops reading further if the message 'How are you?' is found using break.<br><br><em><strong>Hint:</strong> Use both continue and break in the same loop for this task.
lst = ['Hi', 'Spam', 'Hello', 'Spam', 'How are you?']

for i in lst:
    if i == "Spam":
        continue
    elif i == "How are you?":
        break
    else :
        print(i)