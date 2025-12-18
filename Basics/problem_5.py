"""Write a python program to find an average of two numbers entered by the user."""

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

average = (a + b) / 2

print(f"Average of {a} and {b} is = {average}")

"""Write a python program to calculate the square of a number entered by the user."""

# First way to do this
num = int(input("Enter a number: "))
square = num ** 2
print(f"The square of {num} is {square}")

# Second way to do this
num = int(input("Enter a number: "))
square = num * num
print(f"The square of {num} is {square}")