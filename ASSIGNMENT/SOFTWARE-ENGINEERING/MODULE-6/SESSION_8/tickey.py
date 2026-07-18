# Build a function book_movie_ticket(movie_name, seat_type='Regular', snacks=None) that prints a booking summary. Call the function using only positional arguments, only keyword arguments, and a mix of both to book tickets for 'Jawan' and 'Pathaan' with different seat types and snacks.<br><br><em><strong>Hint:</strong> Try calling book_movie_ticket('Jawan', snacks='Popcorn', seat_type='VIP')</em>
def book_movie_ticket(movie_name,seat_type="Regular",snacks=None):
    return movie_name,seat_type,snacks

print(book_movie_ticket("jawan",snacks="pocorn"))
