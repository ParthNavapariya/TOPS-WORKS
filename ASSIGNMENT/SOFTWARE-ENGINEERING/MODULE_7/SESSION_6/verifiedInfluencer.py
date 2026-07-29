# Demonstrate multilevel inheritance by creating a class VerifiedInfluencer that inherits from Influencer and adds a badge attribute; create a VerifiedInfluencer object and display all its properties.


class user:
    def __init__(self,username,email):
        self.username = username
        self.email = email
    
class influncer(user):
    def __init__(self, username, email,follwer):
        super().__init__(username, email)
        self.follwer = follwer
class verifiedinfluencer(influncer):
    def __init__(self, username, email, follwer,badge):
        super().__init__(username, email, follwer)
        self.badge = badge

p1 = verifiedinfluencer("ParthNAvapariya","parthnavapariya8@gmail.com",90,"verfied")
print(p1.username,p1.email,p1.follwer,p1.badge)
         