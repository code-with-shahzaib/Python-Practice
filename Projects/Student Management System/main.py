"""
🚀 MINI PROJECT
📚 Student Management System (Phase 1)
You're building the MVP of a student record tool. Don’t over-engineer.

Requirements
Take input from the user:
1- Student name
2- Roll number
3- 3 subjects and their marks (dictionary inside dictionary)

Example structure:

{
    "name": "...",
    "roll": "...",
    "marks": {
        "subject1": score,
        "subject2": score,
        "subject3": score
    }
}

 
Then print:
1- Full student record
2- Total marks
3- Average marks
4- Highest mark subject (optional, but if you do this, it shows initiative)
"""

student_record = {}

print("\n================== Welcome To Student Management System ===================")

name = input("Enter Your Name: ").strip()
roll_no = int(input("Enter Your Roll Number: "))

student_record = {
    "name": name,
    "roll_no": roll_no,
    "marks": {}
}

for _ in range(3):
    subject = input("\nEnter Subject Name: ").strip()
    marks = int(input(f"Enter {subject}'s Marks: "))
    student_record["marks"][subject] = marks

print("\n------------- Student Record --------------")
print(f"Name: {student_record['name'].title()}")
print(f"Roll No: {student_record['roll_no']}")

for subject, marks in student_record["marks"].items():
    print(f"{subject}: {marks}")

total = sum(student_record["marks"].values())
average = total / len(student_record["marks"])

print(f"\nTotal Marks: {total}")
print(f"Average Marks: {average:.2f}")

highest_subject = max(student_record["marks"], key=student_record["marks"].get)
print(f"Highest Marks: {student_record['marks'][highest_subject]} in {highest_subject}")