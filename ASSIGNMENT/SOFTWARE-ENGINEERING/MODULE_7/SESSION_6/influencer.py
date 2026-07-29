# Build a single inheritance example where a class Influencer inherits from User and adds a followers attribute; create an Influencer object and print all its details.

class user:
    def __init__(self,username,email):
        self.username = username
        self.email = email
class Influencer(user):
    def __init__(self, username, email,follwers):
        super().__init__(username, email)
        self.followers = follwers
    
p1 = Influencer("ParthNavapariya","parthnavapariya8@gmail.com",90)
print(p1.username,p1.email,p1.followers)