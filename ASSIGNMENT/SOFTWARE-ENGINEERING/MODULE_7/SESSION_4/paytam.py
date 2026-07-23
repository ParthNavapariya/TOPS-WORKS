# Simulate a Flipkart-style checkout process where a function process_payment(amount) raises a PaymentFailedError (custom exception) if the amount is less than or equal to zero, and prints 'Payment Successful' otherwise.
class paymentfaileError(Exception):
 pass
def process_payment(amount):
    if amount <= 0:
        raise paymentfaileError("paymentfaildError")
    print("payment Successfull")
    

try:
    user = int(input("Enter amount"))
    process_payment(user)
except paymentfaileError as e:
    print(e)
