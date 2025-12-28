"""
Problem 3: Nested Dictionary Access
Given:

student = {
    "name": "Ali",
    "marks": {
        "math": 88,
        "cs": 92,
        "english": 74
    }
}

Tasks:
1- Print CS marks
2- Increase math marks by 5
3- Add "physics": 81 inside marks
4- Print the updated student dict
"""

student = {
    "name": "Ali",
    "marks": {
        "math": 88,
        "cs": 92,
        "english": 74
    }
}

print("\n------------------ Only CS Marks ------------------")
print(f"The Marks of CS is: {student['marks']['cs']}")

# Increase math marks by 5
student["marks"]["math"] += 5

# Add physics marks
student["marks"]["physics"] = 81

print("\n------------------ Complete Updated Data of Student ------------------")
print(f"The Name of Student is: {student['name']}\n")

for subject, marks in student['marks'].items():
    print(f"The Marks of {subject.capitalize()} is {marks}.")







