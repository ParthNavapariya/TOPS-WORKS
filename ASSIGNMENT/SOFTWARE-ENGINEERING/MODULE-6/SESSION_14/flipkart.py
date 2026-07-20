# Create a dynamic nested dictionary in Python to represent a Flipkart shopping cart where each user (by username) can have multiple items, and each item has a name, quantity, and price. Add two users with at least two items each, then print the entire cart.


filpkart = {
    "user_1":{
        "item1":{
            "name":"phone",
            "qun":2,
            "price":1000
        },
        "item2":{
            "name":"laptop",
            "qun":1,
            "price":100000
        }
    },
    "user_2":{
        "item1":{
            "name":"headphone",
            "qun":2,
            "price":100
        },
        "item2":{
            "name":"mouse",
            "qun":3,
            "price":120
        }
    }
}
print(filpkart)