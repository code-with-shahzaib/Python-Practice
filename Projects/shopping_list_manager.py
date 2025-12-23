"""
🧠 Mini Project: Shopping List Manager (No fancy stuff)
Requirements:
1- Create an empty list called shopping_list
2- Ask the user to enter 3 items
3- Add each item to the list

Print:
1- Full shopping list
2- Total number of items
3- First item and last item

If you know loops, use a loop.
If not, ask input 3 times manually. Both are acceptable.
"""

shopping_list = []

for item in range(0,3):
    item = input("Enter the Name of Item: ").strip().title()
    shopping_list.append(item)

print(f"\nFull Shopping List:\n{shopping_list}\n")

total_num_of_items = len(shopping_list)
print(f"\nTotal Items You have Purchased: {total_num_of_items}\n")

# It's what Problem Asking For
print(f"\nThe First Item in Your Shopping List: {shopping_list[0]}.\nThe Last Item in Your Shopping List: {shopping_list[-1]}")

# It's only for User Output Formatting
print(f"\nFirst Item You Purchased: {shopping_list[0]}")
print(f"Last Item You Purchased: {shopping_list[-1]}")