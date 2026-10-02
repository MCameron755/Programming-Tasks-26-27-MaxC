"""
TASK: 05 File Word Search

# Skills: File reading, loops, Data mining
Ask user for a filename and a search term. https://sherlock-holm.es/ascii/ is a site that has the entire collection of Sherlock Holmes
Load the file and count how many lines contain the search term

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

filename = input("Enter the filename: ")
searchterm = input("Enter the search term: ")
try:
    linecount = 0
    with open(filename, 'r') as file:
        for line in file:
            if searchterm in line:
                linecount += 1
    print(f"The term '{searchterm}' was found in {linecount} lines")
except FileNotFoundError:
    print(f"File '{filename}' not found.")