"""
TASK: 04 Password Strength

# Skills: Strings, loops, selection
Ask the user to enter a password, and check that they meet these conditions:
- At least 8 characters
- Contains a number
- Contains a captial and lower cased letter
- Extend for one special character
Print a response of weak, medium or strong for how many they pass.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

password = input("Enter a password: ")

has_length = len(password) >= 8
has_num = False
has_upper = False
has_lower = False
has_special = False
special_characters = "!@#~£$%^&*()_+-={}[]:;/\|,.<>?`¬"

for char in password:
    if char.isdigit():
        has_num = True
    if char.isupper():
        has_upper = True
    if char.islower():
        has_lower = True
    if char in special_characters:
        has_special = True

score = 0
if has_length:
    score += 1
if has_num:
    score += 1
if has_upper and has_lower:
    score += 1
if has_special:
    score += 1

if score <= 2:
    print("Current password strength: Weak")
elif score == 3:
    print("Current password strength: Medium")
else:
    print("Current password strength: Strong")