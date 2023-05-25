import os
import time

def arrow_up():
    for i in range(6):
        print(21 * " ", end=' ')
        for j in range(i, 6):
            print(" ", end=' ')

        for j in range(i):
            print("*", end=' ')

        for j in range(i + 1):
            print("*", end=' ')

        print()

    for i in range(12):
        print(34 * " " + "*")

def arrow_down():
    for i in range(17):
        print()
    for i in range(12):
        print(34 * " " + "*")

    for i in range(6):
        print(21 * " ", end=' ')
        for j in range(i + 1):
            print(" ", end=' ')

        for j in range(i, 6 - 1):
            print("*", end=' ')

        for j in range(i, 6):
            print("*", end=' ')

        print()

def arrow_right():
    for i in range(11):
        print()
    for i in range(6 * 2):
        print(33 * " ", end=' ')
        if i < 6:
            print(6 * 4 * " " + i * "* ")
        elif i > 6:
            print(6 * 4 * " " + (6 * 2 - i) * "* ")
        else:
            print(6 * 3 * "* ")

def arrow_left():
    for i in range(11):
        print()
    for i in range(12):
        if i < 6:
            for j in range(i, 6):
                print(" ", end=' ')
            for j in range(i):
                print("*", end=' ')

            print()
        elif i > 6:
            for j in range(i - 6):
                print(" ", end=' ')
            for j in range(i, 12):
                print("*", end=' ')
            print()
        else:
            print(6 * 3 * "* ")

def rotate_clockwise(speed):
    for _ in range(4):
        os.system('cls')
        arrow_up()
        time.sleep(speed)
        os.system('cls')
        arrow_right()
        time.sleep(speed)
        os.system('cls')
        arrow_down()
        time.sleep(speed)
        os.system('cls')
        arrow_left()
        time.sleep(speed)

def rotate_anticlockwise(speed):
    for _ in range(4):
        os.system('cls')
        arrow_up()
        time.sleep(speed)
        os.system('cls')
        arrow_left()
        time.sleep(speed)
        os.system('cls')
        arrow_down()
        time.sleep(speed)
        os.system('cls')
        arrow_right()
        time.sleep(speed)

while True:
    os.system('cls')

    print("Select the rotation:")
    print("1. Clockwise")
    print("2. Anti-clockwise")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        speed = float(input("Enter the speed of rotation (in seconds): "))
        rotate_clockwise(speed)
    elif choice == '2':
        speed = float(input("Enter the speed of rotation (in seconds): "))
        rotate_anticlockwise(speed)
    elif choice == '3':
        break
