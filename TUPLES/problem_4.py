"""
Problem 4: Tuple with Loop
Create a tuple of 5 numbers.

Using a for loop:
1- Print each element on a new line
2- Calculate and print the total

No converting to list. No shortcuts.
"""

numbers = (10, 20, 30, 40, 50)

sum_of_numbers = 0
index = 1

for i in numbers:
    print(f"The {index} Element of the Tuple: {i}")
    sum_of_numbers += i
    index += 1

print(f"The Sum of All Numbers Stored in Tuple: {sum_of_numbers}")
