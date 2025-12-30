"""
Mini Project:
Book Inventory Tracker (Phase 1)

User Input:
Add 5 book titles (strings) to a set.
After adding, ask the user: "Do you want to remove a book? (yes/no)"

If yes:
Ask for book name to remove.
If it exists, remove and show updated inventory.
If not, show error message "Book not found in inventory".

Finally:
Print complete inventory.
"""

book_inventory = set()

print("\n=============== Welcome to Book Inventory Tracker =================")

print("\n------------ Input Taking Section ------------")
for _ in range(5):
    book_name = input("Enter Book Name You Want to Add in Inventory: ").strip().title()
    book_inventory.add(book_name)

print("\n------------- Update Section -------------")

while True:
    choice = input("Do You Want to Remove a Book? (yes/no) ").strip().lower()

    if choice == "yes":
        book_name = input("Enter the Name of Book Do You Want to Remove: ").strip().title()

        if book_name in book_inventory:
            book_inventory.remove(book_name)

            print("Here is the updated Book Inventory:")
            for book in book_inventory:
                print(f"\t{book}")
            break

        else:
            print(f"{book_name} Book Not Found in Inventory")

    elif choice == "no":
        print("The Books in Your Inventory: ")
        for book in book_inventory:
            print(f"\t{book}")
        break

    else:
        print("Enter a Valid Input.\n")