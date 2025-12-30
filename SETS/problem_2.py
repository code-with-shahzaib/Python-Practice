"""
Problem 2: Operations

Given:
backend = {"Python", "Django", "Flask"}
frontend = {"HTML", "CSS", "JavaScript", "Python"}

Tasks:
1- Print technologies common in both sets.
2- Print all technologies someone should learn for full-stack (combine without duplicates).
3- Print what is only in backend (not in frontend).
"""


backend = {"Python", "Django", "Flask"}
frontend = {"HTML", "CSS", "JavaScript", "Python"}

print("\n=========== Common in Both Sets ============")
common_technologies = backend.intersection(frontend)
print(f"The Common Technologies are:")
for technology in common_technologies:
    print(f"\t{technology}")

print(f"The Total Number of Common Technologies is: {len(common_technologies)}")

print("\n=========== Technologies Someone Should Learn ============")
combined_technologies = backend.union(frontend)
print("The Technologies Someone Should Learn are For Full Stack:")
for technology in combined_technologies:
    print(f"\t{technology}")

print(f"The Total Number of Technologies Someone Should Learn For Full Stack: {len(combined_technologies)}")

print("\n=========== Technologies For Backend ============")
backend_only = backend.difference(frontend)
for technology in backend_only:
    print(f"\t{technology}")

print(f"The Total Number of Technologies For Backend: {len(backend)}")
