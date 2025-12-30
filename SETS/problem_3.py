"""
Problem 3: Attendance System

Make a set:

1- present = set()
2- Input 5 names (like attendance). Before adding each name:
    (i)     If the name already exists, print: "Already marked present".
    (ii)    Otherwise add it.

End result:
Print final attendance list (the set).
"""

present = set()

print("\n=========== Marking Attendance ============")
for _ in range(5):
    name = input("What's Your Name: ")

    if name in present:
        print(f"{name.capitalize()} is Already Marked Present.")
    
    else:
        present.add(name)

print("\n========== Today's Attendence Sheet ===========")
for name in present:
    print(f"\t{name}")

print("\n========= Total Attendace Today ==========")
print(f"Total Number of Students Present Today: {len(present)}\n")