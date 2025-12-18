"""Write a python program to find remainder when a number is divided by z."""

num = float(input("Enter a number: "))
z = float(input("Enter z: "))

remainder = num % 2

print(f"The remainder of {num} divided by {z} is = {remainder}")

num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))

# Practice Different arithmetic operators along with f string

addition = num_1 + num_2
difference = num_1 - num_2
product = num_1 * num_2
division = num_1 / num_2

print(f"The addition of {num_1} + {num_2} = {addition}")
print(f"The difference of {num_1} - {num_2} = {difference}")
print(f"The product of {num_1} x {num_2} = {product}")
print(f"The division of {num_1} ÷ {num_2} = {division}")