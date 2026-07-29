# Create a Python class called User with attributes username and email, then create an object and print its details.

class user:
    def __init__(self,username,email):
        self.username = username
        self.email = email

p1 = user("ParthNavapariya","parthnavapariya8@gmail.com")
print(p1.username,p1.email)
