"""
TASK: 02 Times Tables

# Skills: Loops,input validation
Ask the user for a number, print the multiplication from 1 to 12 in a readable format:

Extend by using a function you can call for easy entry

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def times_table():
    while True:
        try:
            number = int(input("Enter a number to view its times table: "))
            break
        except ValueError:
            print("Invalid input, enter a whole number: ")
    print("The", number, "times table:")
    for x in range(1, 13):
        print(number, "x", x, "=", number * x)

times_table()