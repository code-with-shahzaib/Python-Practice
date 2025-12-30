"""
Problem 5: Frozen Set
Create a frozenset that contains 3 countries of your choice.
Try to add a 4th country.

Expected behavior:

Python should throw an error.

Handle it gracefully using try/except and print a clear message instead of crashing.
"""

country = frozenset({"Pakistan", "Saudi Arabia", "India"})

try:
    country.add("Iran")

except Exception as e:
    print(f"The Country Can't Be Added.\n{e}")