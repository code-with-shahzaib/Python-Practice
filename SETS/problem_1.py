"""
Problem 1: Unique Students

Input:
1- Take 6 student names from the user.
2- Some names may repeat.

Output:
1- Store them in a set and print only the unique names.
2- Print the count of unique students.
"""

names = set()


print("\n------------------ Input Taking Section-------------------")
for _ in range(6):
    name = input("Enter Student Name: ").strip().title()
    names.add(name)


print("\n------------------ Showing Unique Names -------------------")
for name in names:
    print(f"The Name of Student is: {name}")

print("\n------------------ How Many Unique Names Given -------------------")
print(f"Total Unique Names Given by User is {len(names)}\n")