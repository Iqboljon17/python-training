products = {
    "Laptop": 1200,
    "Phone": 800,
    "Mouse": 25,
    "Keyboard": 50,
    "Monitor": 300
}
overalPrice = 0
for product, price in products.items(): 
    if price > 100:
        print(product,price)
        overalPrice += price
print("Overal price is",overalPrice)
    
