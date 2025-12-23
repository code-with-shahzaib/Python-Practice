"""
Problem 3: Numbers Slice
Create a list of numbers from 1 to 10.

Then print:
1- First 5 numbers
2- Last 3 numbers
3- The list except the first and last element
"""

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(num_list[0:5]) # To print First 5 Numbers
print(num_list[len(num_list) - 3:]) # To print Last 3 Numbers
print(num_list[1:-1]) # To print List Except First and Last Number