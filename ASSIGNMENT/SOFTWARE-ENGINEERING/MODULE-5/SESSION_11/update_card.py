# Build a function update_cart(cart, item, qty) that adds a new item to a Flipkart-style cart dictionary or updates the quantity if the item already exists, then returns the updated cart.<br><br><em><strong>Hint:</strong> Use the dictionary's update() method or direct assignment for adding/updating entries.</em>
def update_cart(cart,item,qty):     
        cart [item] = qty
        return cart

flipkart= {
    "phone" : 3,
    "hanshpree" : 4,
    "mic" :5,
    "cabel" : 6
}
print(update_cart(flipkart,"phone",19))
print(update_cart(flipkart,"adaptor",19))