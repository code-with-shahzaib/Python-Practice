"""
Problem 4: Dictionary with Loop
Create a dictionary of 3 fruits and their prices.

Using a loop:
1- Print each fruit as Fruit: Price
2- Calculate the total price of all fruits
"""

# Fruit Data 
fruit_data = {}

print("\n-----------------Taking Inputs----------------")

for i in range(0,3):
    fruit_name = input("\nEnter the Fruit Name: ").strip()
    fruit_price = int(input(f"Enter {fruit_name} Price: "))

    fruit_data.update({fruit_name:fruit_price})

print("\n----------------Fruits Detail---------------")
# Task 1: Print Each Fruit with Price
for key, value in fruit_data.items():
    print(key, ":", value)

print("\n----------------Total Fruits Price---------------")
# Task 2: Calculate the Total Price of all Fruits
total_price = 0
for key in fruit_data:
    total_price += fruit_data[key]

print(f"The Total Price of All Fruits: {total_price}")

print("\n----------------Fruits Average Price---------------")
# Task 3 (Self Added): Calculate of the Average

average = total_price / len(fruit_data)
print(f"The Average Price of Fruits: {average:.2f}\n")