"""
Problem 4: List → Set Sanitization

Given list:
data = ["apple", "banana", "apple", "grape", "banana", "mango", "apple"]

Tasks:
Convert to a set.
Print the sanitized set.
Explain in a comment (in your own code) why the output order looks random.
"""

data = ["apple", "banana", "apple", "grape", "banana", "mango", "apple"]

sanitized_data = set(data)
print("\n------------- Sanitized Data --------------")
for fruit in sanitized_data:
    print(f"\t{fruit.title()}")

# The output order looked Random and Unique because data is a list in original but after changing it to set it changed the output. The reason is that sets are unordered and store only unique things because the set is a collection of wel defined objects only not duplicates.
