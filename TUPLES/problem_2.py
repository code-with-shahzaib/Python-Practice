"""
Problem 2: Tuple Slicing
Given:
numbers = (10, 20, 30, 40, 50, 60, 70)

Print:
1- First 3 elements
2- Last 2 elements
3- All elements except the first and last
"""

numbers = (10, 20, 30, 40, 50, 60, 70)

print(f"\nThe First Three Elements of the Tuple: {numbers[0:3]}") # Task 1: Print First 3 Elements
print(f"\nThe Last Two Elements of the Tuple: {numbers[-2:]}") # Task 2: Print Last 2 Elements
print(f"\nThe Tuple Without First & Last Elements: {numbers[1:-1]}") # Task 3: The Tuple Without First & Last Elements
