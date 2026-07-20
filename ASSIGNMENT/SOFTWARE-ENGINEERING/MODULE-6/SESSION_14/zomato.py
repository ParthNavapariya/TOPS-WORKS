# Given a nested dictionary representing Zomato orders (order_id as key, value is another dictionary with 'restaurant', 'items' (list), and 'total'), write a function to add a new order and another function to update the total of an existing order.<br><br><em><strong>Hint:</strong> Use dict.setdefault() to handle missing keys dynamically.</em>


zomato = {
    "order_101":{
        "restuarant":"gopal",
        "items":["gujarati"],
        "total":2
    },
    "order_102":{
      "restuarant":"ladli",
      "items":["panni"],
      "total":1
    }
}


def add_order(order_id,resturant,item,total):
    zomato.setdefault(order_id,{
        "restuarnt":resturant,
        "items":item,
        "total":total
    })



def update_total(order_id,new_total):
    if order_id in zomato:
        zomato[order_id]["total"] = new_total


add_order("order_103", "mahavir", ["Punjabi Thali"], 2)
update_total("order_101", 5)

print(zomato)
