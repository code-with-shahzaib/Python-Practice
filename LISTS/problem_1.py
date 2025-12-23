"""
Problem 1: Personal List
Create a list containing:
1- your name
2- your age
3- your favorite programming language

Then:
1- Print the list
2- Print only the first element
3- Print the last element using negative indexing
"""

personal_data = []

name = input("Enter Your Name: ").strip().title()
personal_data.append(name)

age = int(input("Enter Your Age in Years: "))
personal_data.append(age)

fav_programming_lang = input("Enter the Name of Your Favorite Programming Language: ").strip().title()
personal_data.append(fav_programming_lang)


print(f"Personal Data List:\n{personal_data}")
print(f"\nThe only First Element of the Personal Data List:\n{personal_data[0]}")
print(f"\nThe Last Element of the Personal Data List:\n{personal_data[-1]}")