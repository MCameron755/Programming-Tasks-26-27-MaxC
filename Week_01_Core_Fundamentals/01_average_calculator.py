"""
TASK: 01 Average Calculator

# Average Calculator
Write a Python program that:
- Prompts the user for a list of numbers.
- Stores them in a 1D list.
- Calculates the mean *without using built-in statistics libraries*.
- Includes input validation.
- Implements a reusable function: `calculate_average(values)`.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    list = []
    total = 0
    enterlist = input("Enter a list of numbers")
    list = enterlist.split()
    num = 0
    for i in range len(list):
        total = total + list[num]
        num = num + 1
    mean = total / len(list)
    pass



if __name__ == "__main__":
    main()
