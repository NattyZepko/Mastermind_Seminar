from tkinter import *
import bh
import time  # AND SPACE!


# ### Return the n-th digit of a number
def get_digit(number, n):
    stringNumber = str(number)
    return stringNumber[n]


def StartGame(player_type, game_count=1, zero_included=0, num_of_digits=4):
    # gameWindow = Toplevel()
    root2 = Tk()
    bh.Zero = zero_included
    bh.NumberOfGames = game_count
    bh.NumberOfDigits = num_of_digits
    Sleeping_Time = 0.001

    picturesOfQuestionMarks = []
    for i in range(num_of_digits):
        picturesOfQuestionMarks.append(Label(root2, text="?"))
        picturesOfQuestionMarks[i].grid(row=0, column=i)

    if player_type == "AI":
        for i in range(game_count):  # For each game:
            CurrentGame = bh.BH(number=0, numberOfDigits=num_of_digits)  # Current Game object holds the current game
            allGuesses = CurrentGame.getGuesses()  # Get all guesses
            allNB = CurrentGame.getNBs()  # Get all Bull (right color, wrong spot)
            allNH = CurrentGame.getNHs()  # Get all Hits (right color, right spot)
            print(allGuesses)  # SANITY CHECK
            Game_number_Label = Label(root2, text="Game number " + str(i + 1))  # Label with current game number
            Game_number_Label.grid(row=0, column=num_of_digits + 1)  # Put it after the question marks
            for Guess_index, guess in enumerate(allGuesses):  # For each guess
                time.sleep(Sleeping_Time)
                digitsGuess = []  # A list of int variables
                digitSpinBoxes = []  # A list of the Spin Box objects, controlled by the int variables
                for j in range(num_of_digits):  # j iterates items in a row
                    digitsGuess.append(IntVar())  # make an int variable
                    if zero_included:
                        digitsGuess[j].set(0)
                    else:
                        digitsGuess[j].set(1)
                    digitSpinBoxes.append(Spinbox(root2, textvariable=get_digit(guess, j), width=2, state=DISABLED))  # Create a spin box
                    digitSpinBoxes[j].grid(row=Guess_index+1, column=j)  # Put it on the screen, index+1 because we want the count to start from 1.

                # ### ANIMATING A GUESS:
                time.sleep(Sleeping_Time)  # After drawing the guess line, wait
                for j in range(num_of_digits):
                    digitsGuess[j].set(get_digit(guess, j))  # Set the spinbox value to match the digit of the guess
                    digitSpinBoxes[j].config(textvariable=get_digit(guess, j))
                Guess_Result_Label = Label(root2, text="Bull:"+str(allNB[Guess_index])+" Hits:" + str(allNH[Guess_index]))
                Guess_Result_Label.grid(row=Guess_index+1, column=num_of_digits + 1)
            for index, pic in enumerate(picturesOfQuestionMarks):
                pic.config(text=get_digit(guess, index))  # REVEAL THE ANSWER
            Game_Result_Label = Label(root2, text="Win in " + str(len(allGuesses)) + " guesses.")  # Show number of guesses
            Game_Result_Label.grid(row=len(allGuesses) + 2, column=1, columnspan=5)

    else:
        print("TO DO")

    root2.mainloop()
