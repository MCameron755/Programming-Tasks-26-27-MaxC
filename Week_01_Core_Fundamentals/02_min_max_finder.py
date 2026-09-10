"""
TASK: 02 Min Max Finder

# Min/Max Finder
Write a program that:
- Accepts a list of integers.
- Manually finds the min and max (no built-in min/max).
- Includes a function `find_min_max(values)` returning `(min_value, max_value)`.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def find_min_max(values):
    minvalue = values[0]
    maxvalue = values[0]
    for value in values[1:]:
        if value < minvalue:
            minvalue = value
        if value > maxvalue:
            maxvalue = value
    return minvalue, maxvalue

def user_list():
    numlist = []
    print("Enter your list of numbers. Type 'done' when finished")
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
    mni, max = find_min_max(userinput)
    print("Minimum value from list inputted:", min)
    print("Maximum value from list inputted:", max)
