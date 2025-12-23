"""
Problem 4: Simple Total (only if you know loops)
Create a list of numbers:
marks = [70, 85, 90, 60, 75]
Using a for loop:
Calculate and print the total marks
"""

marks = [70, 85, 90, 60, 75]

sum_of_marks = 0

for i in marks:
    sum_of_marks += i

# print(sum(marks)) # This is only for test
print(f"Sum of Marks List is: {sum_of_marks}")