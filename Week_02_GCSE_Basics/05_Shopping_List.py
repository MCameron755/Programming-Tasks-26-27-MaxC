"""
TASK: 05 Shopping List

# Skills: Loops, lists
Allow the user to add itemds to a shopping list until they type DONE
When they type DONE, print the list and ask if they want to edit any item.
They should select an item by number and allow them to ammend the item.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

shoppinglist = []
while True:
    item = input("Enter an item to add to the shopping list (Type 'DONE' when finished): ")
    if item == "DONE":
        break
    shoppinglist.append(item)
print("Your shopping list: ")
for x, item in enumerate(shoppinglist, start=1):
    print(x,".",item)
edititem = input("Do you want to edit an item? (Y/N)")
if edititem =="Y":
    itemnum = int(input("Enter the number of the item you want to edit: "))
    if 1 <= itemnum <= len(shoppinglist):
        olditem = shoppinglist[itemnum - 1]
        newitem = input("Enter new item to replace '" + olditem + "': ")
        shoppinglist[itemnum - 1] = newitem
        print("Item updated")
    else:
        print("Invalid item number")