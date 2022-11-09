from tkinter import *
import bh
import time  # AND SPACE!


def StartGame(player_type, game_count=1, zero_included=0, num_of_digits=4):
    # gameWindow = Toplevel()
    root2 = Tk()
    bh.Zero = zero_included
    bh.NumberOfGames = game_count
    bh.NumberOfDigits = num_of_digits
    # bh.main() # Run Ithak's code.

    picturesOfQuestionMarks = []
    for i in range(num_of_digits):
        picturesOfQuestionMarks.append(Label(root2, text="Q").grid(row=0, column=i))

    if player_type == "AI":
        for i in range(game_count):  # For each game:
            CurrentGame = bh.BH(number=0, numberOfDigits=num_of_digits)  # Current Game object holds the current game
            allGuesses = CurrentGame.getGuesses()  # Get all guesses
            allNB = CurrentGame.getNBs()  # Get all Bull (right color, wrong spot)
            allNH = CurrentGame.getNHs()  # Get all Hits (right color, right spot)
            print(allGuesses)  # SANITY CHECK
            Game_number_Label = Label(root2, text="Game number " + str(i + 1))  # Label with current game number
            Game_number_Label.grid(row=0, column=num_of_digits + 1)
            for index, guess in enumerate(allGuesses):  # For each guess
                time.sleep(1)
                digitsGuess = []
                digitSpinBoxes = []
                for j in range(num_of_digits):
                    digitsGuess.append(IntVar())
                    if zero_included:
                        digitsGuess[0].set(0)
                    else:
                        digitsGuess[0].set(1)
                    digitSpinBoxes.append(Spinbox(root2, from_=zero_included, to=9, textvariable=digitsGuess[j], width=2))
                    digitSpinBoxes[j].grid(row=index, column=j)
                    print(j)

    else:
        print("TO DO")

    # activate window (happens at THE END of the code)
    root2.mainloop()