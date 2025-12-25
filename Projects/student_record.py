"""
MINI PROJECT (SMALL BUT IMPORTANT)
🧠 Mini Project: Student Record (Tuple-Based)
Requirements:

Take input:
student name
roll number
marks in 3 subjects
Store all data in ONE tuple

Print:
Full student record
Total marks
Average marks
"""

student_name = input("Enter Your Name: ")
roll_number = int(input("Enter Your Roll Number: "))
marks_list = []

for i in range(1,4):
    marks = float(input(f"Enter Your Marks of {i} Book: "))
    marks_list.append(marks)

total_marks = 0
for mark in marks_list:
    total_marks += mark
student_record = (student_name, roll_number, marks_list)

average = total_marks / len(marks_list)

print(f"Student Record: {student_record}")
print(f"\nTotal Marks of the Student {student_name}: {total_marks}")
print(f"Average of Marks of Student {student_name}: {average}")