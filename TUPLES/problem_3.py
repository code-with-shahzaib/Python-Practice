"""
Problem 3: Tuple Immutability Test
Create a tuple:
colors = ("red", "green", "blue")

Try to:
1- Change "green" to "yellow"
2- Observe what error Python gives
3- Print the error message as a comment in your code explaining why it happens
"""

colors = ("red", "green", "blue")

colors[1] = "yellow"
print(colors)

# After this the Output is Below. It shows that the tuples can't be used to assign a value like this
# It show the immutability of the tuples.
"""Traceback (most recent call last):
  File "e:\PYTHON\Re\Practice\TUPLES\problem_3.py", line 14, in <module>
    colors[1] = "yellow"
    ~~~~~~^^^
TypeError: 'tuple' object does not support item assignment"""