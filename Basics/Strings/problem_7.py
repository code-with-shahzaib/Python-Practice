"""
🔹 Exercise 4: String Functions
Given:
sentence = "  learning python is FUN  "

Do the following:
1- Remove extra spaces
2- Convert it to lowercase
3- Replace fun with awesome

"""

sentence = "  learning python is FUN  "

print(f"Sentence Before Formatting:\n\t{sentence}")

sentence = sentence.strip()
sentence = sentence.lower()
sentence = sentence.replace("fun", "awesome")

print(f"Sentence After Formatting:\n\t{sentence}")