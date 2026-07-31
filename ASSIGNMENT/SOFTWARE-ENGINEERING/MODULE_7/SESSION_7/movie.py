# Given the following code, fix it so that the Movie class overrides the display() method to show the movie's title and year, instead of just the title:<br><br>class Content: def display(self, title): print('Title:', title)
class Content:
   def display(self, title):
      print('Title:', title)

class Movie(Content):
    def display(self, title, year):
       print(title,year)
    

p1 = Movie()
p1.display("spidermane",2026)
# your code here<br><br>Call display() on a Movie object with both title and year.ay() on a Movie object with both title and year.