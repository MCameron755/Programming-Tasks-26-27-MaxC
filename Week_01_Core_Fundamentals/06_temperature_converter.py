"""
TASK: 06 Temperature Converter

# Temperature Converter
Build a converter tool:
- Convert Celsius <-> Fahrenheit.
- Provide a looped menu.
- Validate user input.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def cels_fahr(celsius):
    return (celsius * 9 / 5) + 32

def fahr_cels(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def vaild_num(prompt):
    while True:
        try:
            return float(inptu(prompt))
        except ValueError:
            print("Invaild input")

def menu():
    while True:
        print("1. Convert Celsius to Fahrenheit")
        print("2. Convert Fahrenheit to Celsius")
        print("3. Exit")
        choice = input("Choose an option (1-3):")
        if choice == "1":
            c = vaild_num("Enter temperature in Celsius:")
            print(cels_fahr, "F")
        elif choice == "2":
            f = vaild_num("Enter temperature in Fahrenheit")
            print(fahr_cels, "C")
        elif choice == "3":
            print("Done")
            break
        else:
            print("Invaild choice")

if __name__ == "__main__":
    menu()
