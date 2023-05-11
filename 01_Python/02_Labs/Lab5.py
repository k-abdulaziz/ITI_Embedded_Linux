import keyboard
from os import system

options = ["rjust()", "translate()", "maketrans()", "Exit"]

def ask_user():
    # Prompt user to continue or exit
    print('Press the Escape key to exit, or any other key to continue.')
    event = keyboard.read_event()
    if event.name == 'esc':
        exit()
    input()

def understand_functions():
    while True:
        for i, option in enumerate(options):
            print(f"{i+1}: {option}")

        print("\nPlease enter option number: ")

        selected_option = input()

        if selected_option == '1':
            print("""The rjust() method will right align the string,
            using a specified character (space is default) as the fill character.""")

            txt = "banana"
            print('txt = "{}"'.format(txt))

            print("x = txt.rjust(20)")

            x = txt.rjust(20)

            print(x, "is my favorite fruit.")

            ask_user()

        elif selected_option == '2':
            print("""The translate() method returns a string where some specified characters are replaced 
            with the character described in a dictionary, or in a mapping table.
            Use the maketrans() method to create a mapping table.
            If a character is not specified in the dictionary/table, the character will not be replaced.
            If you use a dictionary, you must use ascii codes instead of characters.""")

            #use a dictionary with ascii codes to replace 83 (S) with 80 (P):
            mydict = {83:  80}
            print("mydict = {83:  80}")

            txt = "Hello Sam!"
            print('txt = "{}"'.format(txt))

            print("txt.translate(mydict)")

            print(txt.translate(mydict))

            ask_user()

        elif selected_option == '3':
            print("The maketrans() method returns a mapping table that can be \nused with the translate() method to replace specified characters.")

            txt = "Hello Sam!"
            print('txt = "{}"'.format(txt))

            mytable = str.maketrans("S", "P")
            print('mytable = str.maketrans("S", "P")')
            print("txt.translate(mytable)")
            print(txt.translate(mytable))

            ask_user()

        elif selected_option == '4':
            return

        else:
            print("Invalid Input")
            input("Press Enter to continue...")
            system('cls')

understand_functions()
