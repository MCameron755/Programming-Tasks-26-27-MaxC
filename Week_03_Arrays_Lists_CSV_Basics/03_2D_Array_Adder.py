"""
TASK: 03 2D Array Adder

# 2D Array Added
Create a 2D arraw and allow user to:
- Append new values in
- read all current values
- delete a chosen entry

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

array2d = []
while True:
    print("1. Append new values")
    print("2. Read all current values")
    print("3. Delete a chosen entry")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        rowinput = input("Enter row values separated by spaces: ")
        newrow = rowinput.split()
        array2d.append(newrow)
        print("Row added successfully.")
    elif choice == "2":
        if not array2d:
            print("The array is empty.")
        else:
            print("Current values in the 2D array:")
            for i, row in enumerate(array2d):
                print(f"Row {i}: {row}")
    elif choice == "3":
        if not array2d:
            print("The array is empty. Nothing to delete.")
        else:
            rowindex = int(input("Enter the row index to delete: "))
            if 0 <= rowindex < len(array2d):
                del array2d[rowindex]
                print(f"Row {rowindex} deleted successfully.")
            else:
                print("Invalid row index.")
    elif choice == "4":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")