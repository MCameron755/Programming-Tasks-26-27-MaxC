"""
TASK: 06 Simple Login

# Skills: Selection, string comparison
Start with a correct username/password (extend if saved in a text file separately):
- Ask for login
- Print "Welcome" or "Access Denied {number} attempts remaining"
Only allow 3 attempts and close the file

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

correct_username = "admin"
correct_password = "123456"

max_attempts = 3
for attempt in range(1, max_attempts + 1):
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == correct_username and password == correct_password;
        print("Welcome")
        break
    else:
        attemptsremaining = max_attempts - attempt
        print("Access denied, ",attemptsremaining, "attempts remaining")
        if attemptsremaining == 0:
            print("No attempts left, Access denied")