"""
TASK: 02 Dice Roll

# Skills: RNG, Loops
Simulate rolling a six-sided die X number of times:
Print each roll, store all values in a list of updated totals for each number (56 ones for example):
Allow the user to print:
- Totals for each side
- average dice roll
- Counts for each of the 6 sides
- Extend (look up how to use mathplotlib and produce a bar graph for all of the statistics)

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

import random

def roll_die():
    try:
        x = int(input("Enter the number of times to roll the die: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return
    rolls = []
    print("Rolling the die")
    for _ in range(x):
        roll = random.randint(1, 6)
        rolls.append(roll)
        print(f"Roll: {roll}")
    counts = [rolls.count(side) for side in range(1, 7)]
    totalsperside = [counts[i] * (i + 1) for i in range(6)]
    averageroll = sum(rolls) / x if x > 0 else 0
    while True:
        print("\nOptions:")
        print("1. Print totals for each side")
        print("2. Print average dice roll")
        print("3. Print counts for each of the 6 sides")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            print(f"Totals for each side: {totalsperside}")
        elif choice == '2':
            print(f"Average dice roll: {averageroll:.2f}")
        elif choice == '3':
            print(f"Counts for each side: {counts}")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    roll_die()