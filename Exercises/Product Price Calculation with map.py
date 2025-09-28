products = [ 
 {"name": "Laptop", "quantity": 2, "price_per_unit": 1200}, 
 {"name": "Mouse", "quantity": 5, "price_per_unit": 25}, 
 {"name": "Keyboard", "quantity": 3, "price_per_unit": 75} 
] 

value = map(lambda lst: str(lst[0])+": $"+str(lst[1]),list(map(lambda product: [product.get("name"),\
                             product.get("quantity")*product.get("price_per_unit")],\
                                products)))

print(list(value))