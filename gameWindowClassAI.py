import tkinter.messagebox
from tkinter import *
import bh
import time  # AND SPACE!


def get_digit(number, n):
    stringNumber = str(number)
    return stringNumber[n]


class GameAI:
    def __init__(self, game_count=1, zero_included=0, num_of_digits=4):
        self.ans_label = None  # [Per-Game] list of Labels, the size of [numOfDigits]
        self.NH = None  # [Per-Game] list of all Hits by order
        self.NB = None  # [Per-Game] list of all Bulls by order
        self.allGuesses = None  # [Per-Game] list of all guesses by order
        self.currentGame = None  # The current game object
        self.gameCount = game_count  # How many games we will play
        self.allGuessCounts = []  # List the size of [gameCount] of how many guesses each game took to solve
        self.currentGameNumber = 1  # Current Game number out of [gameCount] games
        self.zeroIncluded = zero_included  # Boolean for including 1 or excluding
        self.numOfDigits = num_of_digits  # How many numbers to guess (IS OFTEN USED FOR ROW SIZE)
        self.sleeping_Time = 1000  # Sleeping time adjustment
        self.root2 = Tk()  # ### THE CURRENT WINDOW.

        # ### ADJUST THE bh FILE PARAMETERS
        bh.Zero = zero_included
        bh.NumberOfGames = game_count
        bh.NumberOfDigits = num_of_digits

    def startGame(self):
        self.currentGame = bh.BH(0, self.numOfDigits)
        self.create_header()
        # After the windows are built, we launch it
        self.root2.title("AI solves the game")
        # ### SET THE GAME PACE
        # if self.gameCount > 15:
        #     self.sleeping_Time = 50
        # elif self.gameCount > 10:
        #     self.sleeping_Time = 200
        # elif self.gameCount > 5:
        #     self.sleeping_Time = 500
        self.sleeping_Time = round(1000 / self.gameCount)
        #  self.root2.geometry('300x400')  # ENABLE TO FIX THE WINDOW SIZE
        self.root2.mainloop()

    def populate_window(self):
        self.allGuesses = self.currentGame.getGuesses()
        self.NB = self.currentGame.getNBs()
        self.NH = self.currentGame.getNHs()
        self.populateAllRows(1, 0)

    def populateAllRows(self, row_position, guess_index):
        SpinBoxList = []
        current_guess = self.allGuesses[guess_index]  # Get the current guess
        # ### Place the numbers
        for column_idx in range(self.numOfDigits):
            SpinBoxList.append(Spinbox(self.root2, width=2))  # Make a new spinbox
            SpinBoxList[column_idx].grid(row=row_position, column=column_idx)  # Put it on screen
            SpinBoxList[column_idx].insert(0, get_digit(current_guess, column_idx))  # Put a value in the spinbox
            SpinBoxList[column_idx].config(state=DISABLED)  # Disable the spinbox because users shouldn't interfere
        # ### Place the label of the guess-results
        guess_result_label = Label(self.root2, text="Bull:"+str(self.NB[guess_index])+" Hits:" + str(self.NH[guess_index]))
        guess_result_label.grid(row=row_position, column=self.numOfDigits)
        # ### Next step
        if guess_index < len(self.allGuesses)-1:
            # We need more guesses, in the next row
            guess_result_label.after(self.sleeping_Time, lambda: self.populateAllRows(row_position+1, guess_index+1))
        else:
            # "current_guess" is equal to answer, and therefore we can send it as the answer
            guess_result_label.after(self.sleeping_Time, lambda: self.game_ender_setup(row_position+1, current_guess))

    def game_ender_setup(self, row_position, answer):
        # ### REVEAL THE ANSWER
        for column_idx in range(self.numOfDigits):
            self.ans_label[column_idx].config(text=get_digit(answer, column_idx), fg='Green', font="Helvetica 20 bold")
        # ### show how good was the attempt
        result_label = Label(self.root2, text="Solved in " + str(len(self.allGuesses)) + " Guesses")
        result_label.grid(row=row_position, column=1, columnspan=5)
        self.allGuessCounts.append(len(self.allGuesses))  # Record how many guesses, and add to a list
        # ### Temp label for next game
        tempLabel = Label(self.root2, text="")  # TEMP LABEL IS NEEDED TO MATCH THE TIMING.
        tempLabel.grid(row=row_position, column=0)  # By design, an empty slot
        tempLabel.after(self.sleeping_Time * 2, self.prepNextGame)

    def prepNextGame(self):
        if self.currentGameNumber == self.gameCount:  # happens if we played the LAST GAME
            self.showFinalResults()
        else:
            self.currentGameNumber += 1
            self.cleanWindow()
            self.currentGame = bh.BH(0, self.numOfDigits)  # Play the next game in advance
            self.create_header()  # This invokes the loop again

    def showFinalResults(self):
        resultAVG = sum(self.allGuessCounts) / len(self.allGuessCounts)
        tkinter.messagebox.showinfo("RESULTS", "In " + str(self.gameCount) + " games, the average number of guesses is: " + str(round(resultAVG, 2)))

    def cleanWindow(self):
        for widget in self.root2.winfo_children():
            widget.destroy()

    def create_header(self):
        self.ans_label = []
        for i in range(self.numOfDigits):
            self.ans_label.append(Label(self.root2, text='?'))
            self.ans_label[i].grid(row=0, column=i)
        game_num_label = Label(self.root2, text="game # "+str(self.currentGameNumber))
        game_num_label.grid(row=0, column=self.numOfDigits)
        game_num_label.after(self.sleeping_Time, self.populate_window)

