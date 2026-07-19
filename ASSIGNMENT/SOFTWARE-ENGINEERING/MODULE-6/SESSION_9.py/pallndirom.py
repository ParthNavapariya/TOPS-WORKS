# Use ChatGPT to generate a lambda function that takes a string and returns True if it is a palindrome (reads the same forwards and backwards), otherwise False. Test it with 'madam', 'python', and 'noon'.

palindrome = lambda word: word == word[::-1]
print(palindrome("python"))
print(palindrome("madam"))
print(palindrome("noon"))