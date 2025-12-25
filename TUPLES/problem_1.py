"""
Problem 1: Basic Tuple Operations

Create a tuple containing:
1- your name
2- your age
3- your city

Then:
1- Print the tuple
2- Print the first element
3- Print the last element using negative indexing
4- Print the length of the tuple
"""

name = input("Enter Your Name: ").strip()
age = int(input("Enter Your Age in Years: "))
city = input("Enter Your City Name: ").strip()

personal_tuple = (name, age, city)

length = len(personal_tuple)

print(f"\nYour Bio Data:\n{personal_tuple}") # Task 1: Print the tuple
print(f"\nYour Name is: {personal_tuple[0]}") # Task 2: Print only the First Element
print(f"\nYour City is: {personal_tuple[-1]}") # Task 3: Print the Last Element Using Negative Indexing
print(f"\nTotal Things in Your Bio Data Form: {length}") # Task 4: Print the Length of the Tuple
