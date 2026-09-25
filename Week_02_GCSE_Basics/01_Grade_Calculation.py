"""
TASK: 01 Grade Calculation

# Skills: Input, output, selection
Write a program that asks the user for a percentage grade and prints the corresponding letter grade:
- A: 80-100
- B: 60-79
- C: 40-59
- D: <40
Include a function def get_grade(score):

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def get_grade(score):
    if score >= 80:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= "40":
        return "C"
    else:
        return "D"

usergrade = int(input("Enter your grade percentage: "))
lettergrade = get_grade(usergrade)
print("Your letter grade is :", lettergrade)