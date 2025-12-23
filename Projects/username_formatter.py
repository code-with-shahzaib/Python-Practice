"""
🧠 Mini Project (No loops, no if)
📘 Project: Username Formatter

1- Create a program that:
2- Stores a full name (example: "Muhammad Shahzaib")
3- Converts it to lowercase
4- Removes spaces
5- Takes the first 8 characters
6- Prints the result as a username

Example output:
Generated Username: muhammad
"""

full_name = input("Enter Your Full Name: ").lower()
space_free_name = full_name.replace(" ", "")
print(space_free_name) # For Debug purpose only

username = space_free_name[0:8]

print(f"The username for {full_name.title()} is: {username}")
