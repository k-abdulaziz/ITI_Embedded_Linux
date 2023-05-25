from os import system
import math

sc_options = {
    '1': 'Addition',
    '2': 'Subtraction',
    '3': 'Multiplication',
    '4': 'Division',
    '5': 'Exponentiation',
    '6': 'Division with Remainder',
    '7': 'Square Root',
    '8': 'Factorial',
    '9': 'Return'
}

pr_options = {
    '1': 'HEX',
    '2': 'DEC',
    '3': 'OCT',
    '4': 'BIN',
    '5': 'Return'
}

def main_menu():
    print("Welcome to Calculator")
    print("\n1. Scientific \n2. Programmer \n3. Exit")
    mode = input("\nPlease select an option: ")

    if mode == '1':
        sc_menu()
    elif mode == '2':
        pr_menu()
    elif mode == '3':
        print("Thank you for using Calculator")
        exit()
    else:
        print("Invalid option. Please try again.")
        main_menu()

def sc_menu():
    system('cls')
    print("Please select the option you want to perform:")
    for key, option in sc_options.items():
        print(f"{key}. {option}")

    optn = input("Option: ")

    if optn in sc_options:
        if optn == '9':
            print("Returning to the main menu...")
            main_menu()
        else:
            sc_calculator(optn)
    else:
        print("Invalid Option. Try again.")
        sc_menu()

def sc_calculator(optn):
    while True:
        if optn in ['1', '2', '3', '4', '5', '6']:
            op1 = input("Enter first Operand: ")
            op2 = input("Enter second Operand: ")

            if not op1.isdigit() or not op2.isdigit():
                print("Invalid input. Operands must be digits. Try again.")
                return sc_menu()

            operand1 = int(op1)
            operand2 = int(op2)

        elif optn in ['7', '8']:
            op1 = input("Enter Operand: ")

            if not op1.isdigit():
                print("Invalid input. Operand must be a digit. Try again.")
                return sc_menu()

            operand1 = int(op1)
            operand2 = None

        if optn in ['4', '6'] and operand2 == 0:
            print("Fatal Error: Division by zero")
        else:
            operator = sc_options[optn]

            if optn == '1':
                result = operand1 + operand2
            elif optn == '2':
                result = operand1 - operand2
            elif optn == '3':
                result = operand1 * operand2
            elif optn == '4':
                result = operand1 / operand2
            elif optn == '5':
                result = operand1 ** operand2
            elif optn == '6':
                result = operand1 // operand2
            elif optn == '7':
                result = math.sqrt(operand1)
            elif optn == '8':
                result = math.factorial(operand1)

            print(f"{operand1} {operator} {operand2 if operand2 is not None else ''} = {result}")
            loop()


def pr_menu():
    while True:
        system('cls')
        print("Please select the option you want to perform:")
        for key, option in pr_options.items():
            print(f"{key}. {option}")

        optn = input("Option: ")

        if optn == '5':
            print("Returning to the main menu...")
            break
        elif optn in pr_options:
            pr_calculator(optn)
        else:
            print("Invalid Option. Try again.")

def pr_calculator(optn):
    while True:
        if optn == '1':
            number = input("Enter hexadecimal number: ")
            if not all(c in '0123456789abcdefABCDEF' for c in number):
                print("Invalid input. Try again.")
                continue
            operand1 = int(number, 16)
        elif optn == '2':
            number = input("Enter decimal number: ")
            if not number.isdigit():
                print("Invalid input. Try again.")
                continue
            operand1 = int(number)
        elif optn == '3':
            number = input("Enter octal number: ")
            if not all(c in '01234567' for c in number):
                print("Invalid input. Try again.")
                continue
            operand1 = int(number, 8)
        elif optn == '4':
            number = input("Enter binary number: ")
            if not all(c in '01' for c in number):
                print("Invalid input. Try again.")
                continue
            operand1 = int(number, 2)

        print(f"Decimal: {operand1}")
        print(f"Hex: {hex(operand1)}")
        print(f"Octal: {oct(operand1)}")
        print(f"Binary: {bin(operand1)}")
        loop()

def loop():
    choice = input("Do you want to continue? (Y/N): ")
    if choice.upper() == "Y":
        sc_calculator()
    elif choice.upper() == "N":
        print("Goodbye!")
        exit()
    else:
        print("Invalid input!")
        loop()

# Run the calculator
main_menu()