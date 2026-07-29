# Implement multiple inheritance by creating a class BrandPartner that inherits from both Influencer and a new class Brand (with attribute brand_name); create a BrandPartner object and print the username, followers, and brand_name.


class user:
    def __init__(self,username,email):
        self.username = username
        self.email = email
class influncer(user):
        def __init__(self, username, email,follower):
             super().__init__(username, email)
             self.follower = follower
class Verifiedinfluncer(influncer):
     def __init__(self, username, email, follower,badge):
          super().__init__(username, email, follower)
          self.badge = badge
class brand:
     def __init__(self,brandname):
          self.brandname = brandname
class brandpartner(influncer,brand):
     def __init__(self, username, email, follower,brandname):
          influncer.__init__(self,username,email,follower)
          brand.__init__(self,brandname)

          

p1 =brandpartner("ParthNavapariya","parthnavapariya8@gmail.com",90,"patels")
print(p1.username,p1.email,p1.follower,p1.brandname)

