from tkinter import *
import gamewindow as gw
import creditswindow
# noinspection PyUnresolvedReferences
import ui as UI

# THIS IS THE WINDOW. root is the "place" all the items will be places
root = Tk()
root.title = "Mastermind menu"
root.eval('tk::PlaceWindow . center')


# ### configurations: Running constants
MIN_NUMBER_OF_DIGITS = 2
MAX_NUMBER_OF_DIGITS = 8
MIN_NUMBER_OF_GAMES = 1
MAX_NUMBER_OF_GAMES = 100

# ### global variable
PLAYER_TYPE = "AI"


def radioChange(value):
    """ Function called upon main game-type radio-button change
    :param value: the number of radio-button to match
    :type value: int
    """

    if value == 1:
        gameCountSpinBox.config(state=NORMAL)
        delayScale.config(state=NORMAL)
        UI.PLAYER_TYPE = "AI"
    elif value == 2:
        gameCountSpinBox.config(state=NORMAL)
        delayScale.config(state=NORMAL)
        UI.PLAYER_TYPE = "AIvsAI"
    else:  # case 3 (default)
        gameCountSpinBox.config(state=DISABLED)
        delayScale.config(state=DISABLED)
        UI.PLAYER_TYPE = "PLAYER"


def showRules():
    print("TBD: this function was abandoned. Why keep this button anyway? Because we're lazy enough to leave it as it is, as an option to be implemented later. Maybe.")
    return


def showCredits():
    creditswindow.CreditsWindow()


# ### creating controls
welcomeLabel = Label(root, text="Mastermind", font=("David", 25))
Games_Num = Label(root, text=" Games")
MS_Label = Label(root, text="M\\s delay between guesses")

gameCount = IntVar()
gameCount.set(1)
gameCountSpinBox = Spinbox(root,
                           from_=MIN_NUMBER_OF_GAMES,
                           to=MAX_NUMBER_OF_GAMES,
                           textvariable=gameCount,
                           width=5,
                           wrap=True)
num_of_digits = IntVar()
num_of_digits.set(MIN_NUMBER_OF_DIGITS)
numOfDigitsSpinBox = Spinbox(root,
                             from_=MIN_NUMBER_OF_DIGITS,
                             textvariable=num_of_digits,
                             to=MAX_NUMBER_OF_DIGITS,
                             width=3,
                             wrap=True)
num_of_digits.set(4)
numToGuessLabel = Label(root, text="Number of Digits to guess       ")
startButton = Button(root, text="START!", height=5, width=20, command=lambda: gw.StartGame(UI.PLAYER_TYPE, gameCount.get(), CheckVar.get(), num_of_digits.get(), int(UI.delayScale.get()), SoundVar.get()))
rulesButton = Button(root, text="Rules of \nthe game", height=3, width=20, padx=10, command=showRules)
creditsButton = Button(root, text="CREDITS", height=2, width=20, command=showCredits)
blankLabel = Label(root)  # blank text, used for window spacing
delayScale = Scale(root, from_=0, to=1000, length=220, orient=HORIZONTAL)
delayScale.set(50)

v = IntVar()  # Controls the Radio Button for whom solves (v.get() returns the value of the radiobutton)
v.set(1)  # initializing the choice
RB1 = Radiobutton(root, text="AI Solve",  padx=20, pady=15,  variable=v, value=1, command=lambda: radioChange(v.get()))
RB2 = Radiobutton(root, text="AI vs AI",  padx=20, pady=15, variable=v, value=2, command=lambda: radioChange(v.get()))
RB3 = Radiobutton(root, text="Human Solve",  padx=20, pady=15, variable=v, value=3, command=lambda: radioChange(v.get()))


CheckVar = IntVar(value=1)  # Controls the checkbox. (CheckVar.get() returns 0/1 if checked or not)
includeZeroCheckBox = Checkbutton(root, text="Include the 0 digit", variable=CheckVar)

SoundVar = IntVar(value=1)
includeSoundCheckBox = Checkbutton(root, text="Play sound", variable=SoundVar)


# ### add to screen

welcomeLabel.grid(row=0, column=0, columnspan=10)
Games_Num.grid(row=1, column=2)
RB1.grid(sticky="W", row=1, column=0)
RB2.grid(sticky="W", row=2, column=0, columnspan=2)
RB3.grid(sticky="W", row=3, column=0, columnspan=2)
MS_Label.grid(sticky="W", row=2, column=1, columnspan=10)
delayScale.grid(row=3, column=1, columnspan=10)
gameCountSpinBox.grid(sticky="W", row=1, column=1)
includeZeroCheckBox.grid(row=4, column=0, columnspan=10)
includeSoundCheckBox.grid(row=5, column=0, columnspan=10)
numOfDigitsSpinBox.grid(sticky="E", row=6, column=0)
numToGuessLabel.grid(sticky="W", row=6, column=1, columnspan=10)
startButton.grid(sticky="W", row=7, column=0, rowspan=2)
rulesButton.grid(sticky="W", row=7, column=2, columnspan=5)
creditsButton.grid(sticky="W", row=8, column=2, columnspan=5)
blankLabel.grid(sticky="W", row=10, column=0)


# run the main loop (when interrupted, program ends)
root.mainloop()
