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
    
employees = {
    1001: {"name": "Alice", "department": "IT", "salary": 75000},
    1002: {"name": "Bob", "department": "Sales", "salary": 50000},
    1003: {"name": "Charlie", "department": "IT", "salary": 80000},
    1004: {"name": "David", "department": "Marketing", "salary": 60000},
    1005: {"name": "Emma", "department": "IT", "salary": 45000}
}
total = 0
it_count = 0
for employee_id, employee in employees.items():
    if employee["salary"] > 60000:
        print(employee["name"], employee["salary"])
        total += employee["salary"]
    if employee["department"] == "IT":
        print(employee["name"], employee["department"])
        it_count += 1

print("total it employees:", it_count)
print(total)