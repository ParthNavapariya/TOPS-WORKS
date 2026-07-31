# Simulate method overloading in Python by creating a class ZomatoOrder with a method add_item(). Use default arguments so that add_item() can be called with just an item name or with item name and quantity. Show both usages with print statements.<br><br><em><strong>Hint:</strong> Python does not support true method overloading, but you can use default or *args parameters.</em>

class ZomatoOrder:
    def add_item(self,item_name,Quentity=1):
        print({item_name})
        print(Quentity)
p1 = ZomatoOrder()
p1.add_item("burger")
p1.add_item("burger",3)
