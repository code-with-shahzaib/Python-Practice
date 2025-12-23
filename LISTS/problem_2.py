"""
Problem 2: Subjects Manager
Create a list of subjects, for example:

subjects = ["Math", "Physics", "CS"]
Do the following:

1- Add one new subject at the end
2- Insert one subject at index 1
3- Remove one subject by name
4- Print the final list
"""

subjects = ["Math", "Physics", "CS"]

subjects.append("Chemistry")
subjects.insert(1, "Biology")
subjects.remove("CS")

print(subjects)