"""
TASK: 03 Array Reversal

# Array Reversal
Create a program that:
- Generates a list of random integers.
- Reverses the list manually (no slicing or .reverse).
- Includes a function `reverse_list(values)` that returns a new reversed list.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

import random

def reverse_list(values):
    reversed_values = []
    for i in range(len(values) - 1, -1, -1):
        reversed_values.append(values[i])
    return reversed_values

if __name__ == "__main__":
    original_list = [random.randint(1, 100) for _ in range(10)]
    reversed_list = reverse_list(original_list)
    print("Original list:", original_list)
    print("Reversed list:", reversed_list)
