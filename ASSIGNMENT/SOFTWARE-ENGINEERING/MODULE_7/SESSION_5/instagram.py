# Write a Python class called InstagramPost with attributes caption, likes, and comments (a list). Add a method add_comment(comment_text) that appends a new comment to the comments list and increases the likes by 1.
class Instagrampost:
    def __init__(self,caption,like,comments):
        self.caption = caption
        self.likes = like
        self.comments = comments
    def add_comment(self,comment_text):
        self.comments.append(comment_text)
        self.likes+=1

        
post1 = Instagrampost("my first post",100,["Nice","great"])
post1.add_comment("amazing post")
print(post1.caption,post1.likes,post1.comments)

