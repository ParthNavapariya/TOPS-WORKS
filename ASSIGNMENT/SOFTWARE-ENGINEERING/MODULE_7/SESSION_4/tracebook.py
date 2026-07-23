# Given the following traceback from a Python program, use ChatGPT to explain in your own words what the error means and how you would fix it:<br><br>Traceback (most recent call last):<br> File "main.py", line 8, in <module><br> book_ticket('Avengers', -2)<br> File "main.py", line 4, in book_ticket<br> raise InvalidSeatNumberError('Seat number must be positive')<br>NameError: name 'InvalidSeatNumberError' is not defined
class InvalidSeatNumberError(Exception):
    pass


def book_ticket(movie, seat_number):
    if seat_number <= 0:
        raise InvalidSeatNumberError(
            "Seat number must be positive"
        )

    print(f"Ticket booked for {movie}, Seat: {seat_number}")


try:
    book_ticket("Avengers", -2)

except InvalidSeatNumberError as e:
    print(e)