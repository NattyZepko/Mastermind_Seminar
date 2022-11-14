import tkinter.messagebox
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
    Sleeping_Time = 0

    if player_type == "AI":
        guess_count_per_game = []
        for game_num in range(game_count):  # For each game:
            picturesOfQuestionMarks = []
            for j in range(num_of_digits):
                picturesOfQuestionMarks.append(Label(root2, text="?"))
                picturesOfQuestionMarks[j].grid(row=0, column=j)

            CurrentGame = bh.BH(number=0, numberOfDigits=num_of_digits)  # Current Game object holds the current game
            guess_count_per_game.append(len(CurrentGame.getGuesses()))
            allGuesses = CurrentGame.getGuesses()  # Get all guesses
            allNB = CurrentGame.getNBs()  # Get all Bull (right color, wrong spot)
            allNH = CurrentGame.getNHs()  # Get all Hits (right color, right spot)
            print(allGuesses)  # SANITY CHECK
            Game_number_Label = Label(root2, text="Game number " + str(game_num + 1))  # Label with current game number
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
                    digitSpinBoxes.append(Spinbox(root2, width=2))# , state=DISABLED))  # Create a spin box
                    digitSpinBoxes[j].grid(row=Guess_index+1, column=j)  # Put it on the screen, index+1 because we want the count to start from 1.

                # ### ANIMATING A GUESS:
                time.sleep(Sleeping_Time)  # After drawing the guess line, wait
                for j in range(num_of_digits):
                    digitSpinBoxes[j].insert(0,get_digit(guess, j)) 
                    digitSpinBoxes[j].config(state=DISABLED)# ###run when it is not disable and fix*
                Guess_Result_Label = Label(root2, text="Bull:"+str(allNB[Guess_index])+" Hits:" + str(allNH[Guess_index]))
                Guess_Result_Label.grid(row=Guess_index+1, column=num_of_digits + 1)
            for index, pic in enumerate(picturesOfQuestionMarks):
                pic.config(text=get_digit(guess, index))  # REVEAL THE ANSWER
            Game_Result_Label = Label(root2, text="Win in " + str(len(allGuesses)) + " guesses.")  # Show number of guesses
            Game_Result_Label.grid(row=len(allGuesses) + 2, column=1, columnspan=5)
            tkinter.messagebox.showinfo("Game Ended", "Game #" + str(game_num+1) + " ended. Press OK to proceed.")
            # CLEAN THE WINDOW
            for widget in root2.winfo_children():
                widget.destroy()
        avg = round(sum(guess_count_per_game)/len(guess_count_per_game), 3)  # At most, 3 decimal places
        Total_Result_Label = Label(root2, text = "    After " + str(game_count) + " games:\nThe average amount of guesses is: " + str(avg) + "   ")
        Total_Result_Label.grid(row=0,column=0)

    else:
        print("TO DO")

    root2.mainloop()
