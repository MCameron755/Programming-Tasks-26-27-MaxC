"""
TASK: 01 Csv Writer

# Skills: CSV writing
CAsk the user for:
- Name
- age
- favourite colour
- anything you want
Append this to a CSV file (Extend: allow user to choose to edit the file and read the file)

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

import csv
import os

filename = "userdata.csv"
name = input("Enter your name: ")
age = input("Enter your age: ")
favouritecolour = input("Enter your favourite colour: ")
anything = input("Enter anything you want: ")
fileexists = os.path.exists(filename)
with open(filename, "a", newline="") as csvfile:
    writer = csv.writer(csvfile)
    if not fileexists:
        writer.writerow(["Name", "Age", "Favourite Colour", "Anything"])
    writer.writerow([name, age, favouritecolour, anything])
print(f"Data saved to {filename}.")