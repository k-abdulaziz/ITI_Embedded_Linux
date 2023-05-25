from tkinter import *

def ButtonPressTracker():
    ButtonPressTracker.counter += 1 
    print("The button pressed", ButtonPressTracker.counter)

ButtonPressTracker.counter = 0

window_1 = Tk()
window_1.title("Welcome Tkinter")
window_1.geometry('500x500')

Label(window_1, text="Image Button", font=('Verdana', 30)).pack(side=TOP)

photo_1 = PhotoImage(file=r'D:\Embedded_Systems\ITI\ITI_Embedded_Linux\01_Python\02_Labs\moon-knight.gif')
photo_1 = photo_1.subsample(2, 2)

B_1 = Button(window_1, text="Increment The button", bd=5, image=photo_1, command=ButtonPressTracker)
B_1.pack(side=TOP)

B_2 = Button(window_1, text="Close the window", bd=5, command=window_1.destroy)
B_2.pack(side=BOTTOM)

window_1.mainloop()
