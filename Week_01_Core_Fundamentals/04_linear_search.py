"""
TASK: 04 Linear Search

# Linear Search
Implement a linear search algorithm:
- Ask the user for a target value.
- Search a generated random list.
- Return the index or -1.
- Include `linear_search(values, target)`.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

import random

def linear_search(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

if __name__ == "__main__":
    randomlist = [random.randint(1, 20) for _ in range(10)]
    print("Generated list:", randomlist)
    try:
        userinput = input("Enter a target integer to search for:")
        targetvalue = int(userinput)
        resultinder = linear_search(randomlist, targetvalue)
        if resultindex != -1:
            print("Target:", targetvalue, "found at index:", resultindex)
        else:
            print("Target", target value, "not found in the list")
