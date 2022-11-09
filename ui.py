from tkinter import *
import gamewindow as gw

# THIS IS THE WINDOW. root is the "place" all the items will be places
root = Tk()
root.title = "Mastermind menu"


# ### configurations: Running constants
MIN_NUMBER_OF_DIGITS = 4
MAX_NUMBER_OF_DIGITS = 6
MIN_NUMBER_OF_GAMES = 1
MAX_NUMBER_OF_GAMES = 8



# ### Creating function
def radioChange(value):
    if value == 2:
        gameCountSpinBox.config(state=DISABLED)
    else:
        gameCountSpinBox.config(state=NORMAL)


# ### creating controls
welcomeLabel = Label(root, text="Mastermind", font=("David", 25))
Games_Num = Label(root, text=" Games")

gameCount = IntVar()
gameCount.set(1)
gameCountSpinBox = Spinbox(root, from_=MIN_NUMBER_OF_GAMES, to=MAX_NUMBER_OF_GAMES, textvariable=gameCount, width=5)
num_of_digits = IntVar()
num_of_digits.set(MIN_NUMBER_OF_DIGITS)
numOfDigitsSpinBox = Spinbox(root, from_=MIN_NUMBER_OF_DIGITS, textvariable=num_of_digits, to=MAX_NUMBER_OF_DIGITS, width=3)

numToGuessLabel = Label(root, text="Number of Digits to guess       ")
startButton = Button(root, text="START!", command=lambda: gw.StartGame("AI", gameCount.get(), CheckVar.get(), num_of_digits.get()))
rulesButton = Button(root, text="Rules of \nthe game", padx=10)
creditsButton = Button(root, text="CREDITS")
blankLabel = Label(root)  # blank text, used for window spacing

v = IntVar()  # Controls the Radio Button for whom solves (v.get() returns the value of the radiobutton)
v.set(1)  # initializing the choice
RB1 = Radiobutton(root, text="AI Solve",  padx=20,  variable=v, value=1, command=lambda: radioChange(v.get()))
RB2 = Radiobutton(root, text="You Solve",  padx=20,  variable=v, value=2, command=lambda: radioChange(v.get()))


CheckVar = IntVar(value=1)  # Controls the checkbox. (CheckVar.get() returns 0/1 if checked or not)
includeZeroCheckBox = Checkbutton(root, text="Include the 0 digit", variable=CheckVar)


# ### add to screen

welcomeLabel.grid(row=0, column=0, columnspan=10)
Games_Num.grid(row=1, column=2)
RB1.grid(row=1, column=0)
RB2.grid(row=2, column=0)
gameCountSpinBox.grid(row=1, column=1)
includeZeroCheckBox.grid(row=3, column=0, columnspan=10)
numOfDigitsSpinBox.grid(row=4, column=0)
numToGuessLabel.grid(row=4, column=1, columnspan=10)
startButton.grid(row=5, column=1)
rulesButton.grid(row=6, column=0)
creditsButton.grid(row=6, column=2)
blankLabel.grid(row=7, column=0)

# run the main loop (when interrupted, program ends)
root.mainloop()