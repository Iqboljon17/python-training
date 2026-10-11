# products = {
#     "Laptop": 1200,
#     "Phone": 800,
#     "Mouse": 25,
#     "Keyboard": 50,
#     "Monitor": 300
# }
# overalPrice = 0
# for product, price in products.items(): 
#     if price > 100:
#         print(product,price)
#         overalPrice += price
# print("Overal price is",overalPrice)
    
# employees = {
#     1001: {"name": "Alice", "department": "IT", "salary": 75000},
#     1002: {"name": "Bob", "department": "Sales", "salary": 50000},
#     1003: {"name": "Charlie", "department": "IT", "salary": 80000},
#     1004: {"name": "David", "department": "Marketing", "salary": 60000},
#     1005: {"name": "Emma", "department": "IT", "salary": 45000}
# }
# total = 0
# it_count = 0
# for employee_id, employee in employees.items():
#     if employee["salary"] > 60000:
#         print(employee["name"], employee["salary"])
#         total += employee["salary"]
#     if employee["department"] == "IT":
#         it_count += 1

# print("total it employees:", it_count)
# print("total salary of employee's: ",total)

# print("third exercise")
# higherst_salary = {}


# employees = {
#     1001: {"name": "Alice", "department": "IT", "salary": 75000},
#     1002: {"name": "Bob", "department": "Sales", "salary": 50000},
#     1003: {"name": "Charlie", "department": "IT", "salary": 80000},
#     1004: {"name": "David", "department": "Marketing", "salary": 60000},
#     1005: {"name": "Emma", "department": "IT", "salary": 45000}
# }
# highest_salary = 0 

# for employee_id, employee in employees.items():
#     if employee["salary"] > highest_salary:
#         highest_salary = employee["salary"]
#         highest_paid_employee = employee["name"]

# print(highest_paid_employee, highest_salary)


# print("fourth exercise")

# employees = {
#     1001: {"name": "Alice", "department": "IT", "salary": 75000},
#     1002: {"name": "Bob", "department": "Sales", "salary": 50000},
#     1003: {"name": "Charlie", "department": "IT", "salary": 80000},
#     1004: {"name": "David", "department": "Marketing", "salary": 60000},
#     1005: {"name": "Emma", "department": "IT", "salary": 45000}
# }
# total = 0
# count = 0
# avaregeSalary = 0
# for employee_id, employee in employees.items():
#     if employee["department"] == "IT":
#         count += 1
#         total += employee["salary"]
#         averageSalary = total / count 
# print(count)
# print(total)
# print(averageSalary)

# print("fifth exercise")

# employees = {
#     1001: {"name": "Alice", "department": "IT", "salary": 75000},
#     1002: {"name": "Bob", "department": "Sales", "salary": 50000},
#     1003: {"name": "Charlie", "department": "IT", "salary": 80000},
#     1004: {"name": "David", "department": "Marketing", "salary": 60000},
#     1005: {"name": "Emma", "department": "IT", "salary": 45000}
# }
# IT = 0
# Marketing = 0
# Sales = 0
# for el_id, el in employees.items():
#     if el["department"] == "IT":
#         IT += 1
#     if el["department"] == "Marketing":
#         Marketing += 1
#     if el["department"] == "Sales":
#         Sales += 1    
# print("IT department employees: ", IT)
# print("Marketing department employees: ", Marketing)
# print("Sales department employees: ", Sales)