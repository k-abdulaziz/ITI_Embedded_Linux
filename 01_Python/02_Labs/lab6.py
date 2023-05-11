import keyboard
from os import system

def SET_BIT(NUM, BIT):
    NUM = int(NUM)
    BIT = int(BIT)
    return (NUM | (1<<BIT))

def CLEAR_BIT(NUM, BIT):
    NUM = int(NUM)
    BIT = int(BIT)
    return (NUM & (~(1<<BIT)))

def GET_BIT(NUM, BIT):
    NUM = int(NUM)
    BIT = int(BIT)
    return (NUM & (1<<BIT))

options = {"1": SET_BIT, "2": CLEAR_BIT, "3": GET_BIT}

def ask_user():
    # Prompt user to continue or exit
    print('Press the Escape key to exit, or any other key to continue.')
    event = keyboard.read_event()
    if event.name == 'esc':
        exit()
    input()    

def bitwise_menu():
    while True:
        number = input("Enter the number: ")
        if not number.isdigit():
            print("Invalid Input. Please enter a valid integer value for number.")
            continue
        number = int(number)

        bit = input("Enter the bit number: ")
        if not bit.isdigit():
            print("Invalid Input. Please enter a valid integer value for bit.")
            continue
        bit = int(bit)

        for i, option in options.items():
            print(f"{i}: {option.__name__}")
        print("4: Exit")
        selected_option = input("\nPlease enter option number: ")
        if selected_option in options:
            print(f"{number} after {options[selected_option].__name__} bit no.{bit} results in : {options[selected_option](number, bit)}")
            ask_user()
        elif selected_option == '4':
            return
        else:
            print("Invalid Input")

bitwise_menu()