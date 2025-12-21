"""Write a program to detect double space in a string and replace it with single space."""

sentence = "I am Muhammad Shahaib  studying at VU."
print(sentence)
index = sentence.find("  ")
print(f"The double space in this string is at index: {index}")
new_sentence = sentence.replace("  ", " ")
print(f"The Replaced string is below:\n{new_sentence}")