# Define a list to store the ATM cards
import json
from os import system

# Load the data from the JSON file into a Python list of dictionaries
with open('Accounts.json', 'r') as f:
    Cards_List = json.load(f)

# Load the data from the JSON file into a Python list of dictionaries
with open('Langs.json', 'r', encoding='utf-8') as f:
    Languages = json.load(f)

#Cards_List = []

# Define a tuple to store the column names
#Columns = ('card_number', 'pin', 'balance')

# Define a dict to store the data types for each column
#Columns_Types = {'Card_Number': str, 'PIN': str, 'Balance': float}

def Check_Card_Number(Card_Number):
    for index, Card in enumerate(Cards_List):
        if Card['Card_Number'] == Card_Number:
            return True, index
    return False, None

def Check_PIN(index, PIN):
    for i, Card in enumerate(Cards_List):
        if i == index and Card['PIN'] == PIN:
            return True
    return False

import os

def select_language():
    while True:
        print(":من فضلك حدد اللغة")
        print("Please Select Language:")
        print("1. العربية\n2. English")
        selected_language = input()
        system('cls')
        if selected_language == '1':
            print("!بنك الخير والبركة يرحب بك\n")
            return "Arabic"
        elif selected_language == '2':
            print("Welcome to Bank of Khair & Baraka!\n")
            return "English"
        else:
            print("Invalid Input")
            input("Press Enter to continue...")
            os.system('cls' if os.name == 'nt' else 'clear')

def atm_menu(selected_language, account_index):

    print(Languages[selected_language]['welcome_message'])

    while True:
        for i, option in enumerate(Languages[selected_language]['options']):
            print(f"{i+1}: {option}")
        
        selected_option = input(Languages[selected_language]['select_option_number'])
        # print(f"You selected option {selected_option}")
        
        system('cls')

        if selected_option == '1':
            print(Languages[selected_language]['account_balance_message'].format(Cards_List[account_index]['Balance']))

        elif selected_option == '2':
            withdrawn_amount = float(input(Languages[selected_language]['amount_to_withdraw']))
            if withdrawn_amount <= Cards_List[account_index]['Balance'] and withdrawn_amount <= 5000:
                Cards_List[account_index]['Balance'] -= withdrawn_amount
                print(Languages[selected_language]['withdrawn_message'].format(Cards_List[account_index]['Balance']))
            elif withdrawn_amount > 5000:
                print(Languages[selected_language]['max_amount_exceeds_message'])
            else:
                print(Languages[selected_language]['insufficient_balance_message'])
            input(Languages[selected_language]['enter_to_continue_message'])

            
        elif selected_option == '3':
            deposited_amount = float(input(Languages[selected_language]['amount_to_deposit']))
            if deposited_amount > 5000.0:
                print(Languages[selected_language]['max_amount_exceeds_message'])
            else:
                Cards_List[account_index]['Balance'] += deposited_amount
                print(Languages[selected_language]['deposited_message'].format(Cards_List[account_index]['Balance']))
            input(Languages[selected_language]['enter_to_continue_message'])

        elif selected_option == '4':
            new_pin = input(Languages[selected_language]['new_pin_message'])
            new_pin_confirm = input(Languages[selected_language]['new_pin_confirm_message'])
            if new_pin == new_pin_confirm:
                Cards_List[account_index]['PIN'] = new_pin
                print(Languages[selected_language]['pin_changed_successfully_message'])
            else:
                print(Languages[selected_language]['not_matching_pins'])
            input(Languages[selected_language]['enter_to_continue_message'])

        elif selected_option == '5':
            print(Languages[selected_language]['thanks_message'])
            break

        else:
            print(Languages[selected_language]['invalid_option_message'])
            input(Languages[selected_language]['enter_to_continue_message'])

        choice = input(Languages[selected_language]['perform_another_operation_message'])

        if selected_language == 'English':
            if choice.lower() == "n" or choice.lower() == "no":
                print(Languages[selected_language]['thanks_message'])
                break
            elif choice.lower() == "y" or choice.lower() == "yes":
                pin_attempts = 0
                system('cls')
            else:
                print(Languages[selected_language]['invalid_choice_message'])
                input(Languages[selected_language]['enter_to_continue_message'])

        elif selected_language == 'Arabic':
            if choice == "لا":
                print(Languages[selected_language]['thanks_message'])
                break
            elif choice == "نعم":
                pin_attempts = 0
                system('cls')
            else:
                print(Languages[selected_language]['invalid_choice_message'])
                input(Languages[selected_language]['enter_to_continue_message'])

        else:
            print(Languages[selected_language]['invalid_choice_message'])
            input(Languages[selected_language]['enter_to_continue_message'])   


def main():
    selected_language = select_language()
    if not selected_language:
        return
    entered_card_number = input(Languages[selected_language]['enter_card_number'])
    check_result, account_index = Check_Card_Number(entered_card_number)
    if check_result:
        tries = 0
        while tries < 3:
            entered_pin = input(Languages[selected_language]['enter_pin_message'])
            check_result = Check_PIN(account_index, entered_pin)
            if check_result:
                system('cls')
                atm_menu(selected_language, account_index)
                return
            else:
                tries += 1
                if tries < 3:
                    print(Languages[selected_language]['incorrect_pin_message'])
                else:
                    print(Languages[selected_language]['atm_took_card'])
    else:
        print(Languages[selected_language]['invalid_card_message'])

if __name__ == '__main__':
    main()

# Write the updated data back to the JSON file
with open('Accounts.json', 'w') as f:
    json.dump(Cards_List, f, indent=4)
