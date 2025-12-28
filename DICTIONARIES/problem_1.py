"""
Problem 1: Bio Dictionary

Create a dictionary:
1- name
2- age
3- city
4- favorite_language

Then:
1- Print the dictionary
2- Print only the keys
3- Print only the values
4- Access and print city without using hard-coded strings like "Karachi" or whatever

Success metric: No typos in keys, no runtime errors.
"""

bio_dict = {}

name = input("Enter Your Name: ").strip()
age = int(input("Enter Your Age in Years: "))
city = input("Enter Your City Name: ").strip()
favorite_language = input("Enter Your Favorite Programming Language: ").strip()
print() # For Some Output Formation

bio_dict.update({
                "Name":name, 
                "Age":age, 
                "City":city, 
                "Favorite Language":favorite_language
})


# Task 1: Print The Dictionary

print("\n-------------Bio Data-------------")
for key, value in bio_dict.items():
    print(key, ":", value)


# Task 2: Print the Keys Only
print("\n--------------Keys Only--------------")
for key in bio_dict:
    print(key)

# Task 3: Print only the Values
print("\n--------------Values Only--------------")
for key in bio_dict:
    print(bio_dict[key])