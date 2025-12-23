"""
🔹 Exercise 2: Type Casting Practice

1- Take age as a string
2- Convert it into an integer
3- Add 5 to it
4- Print the result

💡 This helps you understand why type casting is important.
"""

age_str = input("Enter your Age in Years: ")
age_int = int(age_str) # Convert it into integer

result = age_int + 5 # Add 5 in converted input
print(f"Your Age after 5 Years will be: {result}.")