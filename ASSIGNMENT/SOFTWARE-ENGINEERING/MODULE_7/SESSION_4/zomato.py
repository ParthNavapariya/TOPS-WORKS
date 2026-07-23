# Create a custom exception class called InvalidCouponCodeError for a Zomato-style food ordering app, and raise this exception if a user tries to apply a coupon code that is not in the list of valid codes.

class InvalidCouponCodeError(Exception):
    pass
coupan_code = ["ORD123","ZOM","ATO"]

try:
    user_Code = input("Enter coupd code")
    if user_Code not in coupan_code:
            raise InvalidCouponCodeError("your code is not right")
    
    print("Your coupan code is right")
except InvalidCouponCodeError as e:
    print(e)

