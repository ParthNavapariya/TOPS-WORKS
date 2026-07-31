# Build a class Payment with a pay() method that takes amount as a parameter and prints 'Paying amount'. Then, create a subclass UPI that overrides pay() to print 'Paying amount via UPI'. Demonstrate both methods by making objects and calling pay().

class payment():
    def __init__(self,amount):
        self.amount = amount
    def pay(self):
        print(f"paying amount {self.amount}")
class upi(payment):
    def __init__(self, amount):
        super().__init__(amount)
    def pay(self):
        print(f"pay {self.amount} via upi")

p1 = payment(100)
p2 = upi(200)

p1.pay()
p2.pay()
