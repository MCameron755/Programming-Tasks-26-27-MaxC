"""
TASK: 02 Simple Logger System

# Create a script that appends time-stamped log entries to a file.
Menu:
- Add Log
- View Log
- Clear Log

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

import datetime
logfile = "app.log"
def addlog():
    message = input("Enter log message: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(logfile, "a") as f:
        f.write(f"{timestamp} - {message}\n")
    print("Log entry added.")

def viewlog():
    try:
        with open(logfile, "r") as f:
            content = f.read()
            if content:
                print("Log entries:")
                print(content)
            else:
                print("Log is empty.")
    except FileNotFoundError:
        print("Log file does not exist.")

def clearlog():
    with open(logfile, "w") as f:
        pass
    print("Log cleared.")

def main():
    while True:
        print("\nMenu:")
        print("1. Add Log")
        print("2. View Log")
        print("3. Clear Log")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            addlog()
        elif choice == "2":
            viewlog()
        elif choice == "3":
            clearlog()
        elif choice == "4":
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
