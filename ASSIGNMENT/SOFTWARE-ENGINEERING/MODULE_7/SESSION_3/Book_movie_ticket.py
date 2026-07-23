# Create a function book_movie_ticket that takes the number of tickets as input and divides a fixed wallet balance by the number of tickets to get the price per ticket. Handle ZeroDivisionError and ValueError using multiple except blocks, and print a different message for each error.<br><br><em><strong>Hint:</strong> Use two separate except blocks for ZeroDivisionError and ValueError.</em>\

def Book_movie_ticket(calculate):
       final =  200/calculate
       return final
try:
       viewr = int(input("Enter ticket numbber"))
       print(Book_movie_ticket(viewr))
except ValueError:
       print("you have enter alphabet")
except ZeroDivisionError:
       print("not allow zero")


