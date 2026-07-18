# Write a function called apply_coupon(amount, coupon_code=None) that applies a 10% discount if coupon_code is 'SAVE10'. Test the function with and without passing the coupon_code argument.<br><br><em><strong>Constraint:</strong> Use a default value for coupon_code so the function works even if no coupon is provided.</em>
def apply_coupan(amount,coupon_code=None):
    if coupon_code == "SAVE10":
            final =  amount/10 
            return amount - final
    
    
print(apply_coupan(100,"SAVE10"))
