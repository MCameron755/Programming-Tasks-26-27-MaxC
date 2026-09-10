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

def calculate_avg(values):
    total = 0
    count = 0
    for value in values:
        total = total + value
        count = count + 1
    total = total / count
    return total

def user_list():
    numlist = []
    print("Enter your list of number. Type 'done' when finished")
    while True:
        numinput = input("Enter a number:").strip()
        if numinput == "done":
            break
        try:
            number = float(numinput)
            numlist.append(number)
        except ValueError:
            print("Invalid input")
    return numlist

if __name__ == "__main__":
    userinput = user_list()
    avg = calculate_avg(userinput)
    print("Your list was:", userinput)
    print("Calculated Average:", avg)
