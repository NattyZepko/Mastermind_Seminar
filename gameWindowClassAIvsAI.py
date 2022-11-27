import tkinter.messagebox
from tkinter import *
import bh
import time  # AND SPACE!


def get_digit(number, n):
    stringNumber = str(number)
    return stringNumber[n]


class GameAIvsAI:
    def __init__(self, game_count=1, zero_included=0, num_of_digits=4):
        self.ans_label_1 = None  # [Per-Game] list of Labels, the size of [numOfDigits]
        self.ans_label_2 = None  # [Per-Game] list of Labels, the size of [numOfDigits]
        self.NH_1 = None  # [Per-Game] list of all Hits by order
        self.NB_1 = None  # [Per-Game] list of all Bulls by order
        self.NH_2 = None  # [Per-Game] list of all Hits by order
        self.NB_2 = None  # [Per-Game] list of all Bulls by order
        self.allGuesses_1 = None  # [Per-Game] list of all guesses by order
        self.allGuesses_2 = None  # [Per-Game] list of all guesses by order
        self.currentGame_1 = None  # The current game object
        self.currentGame_2 = None  # The current game object
        self.gameCount = game_count  # How many games we will play
        self.score = {"1 win" : 0 , "tie" : 0, "2 win" : 0}  # List the size of [gameCount] of how many guesses each game took to solve
        self.currentGameNumber = 1  # Current Game number out of [gameCount] games
        self.zeroIncluded = zero_included  # Boolean for including 1 or excluding
        self.numOfDigits = num_of_digits  # How many numbers to guess (IS OFTEN USED FOR ROW SIZE)
        self.sleeping_Time = 1000  # Sleeping time adjustment
        self.offset = None
        self.root2 = Tk()  # ### THE CURRENT WINDOW.

        # ### ADJUST THE bh FILE PARAMETERS
        bh.Zero = zero_included
        bh.NumberOfGames = game_count
        bh.NumberOfDigits = num_of_digits

    def startGame(self):
        self.currentGame_1 = bh.BH(0, self.numOfDigits)
        self.currentGame_2 = bh.BH(0, self.numOfDigits)
        self.offset = 3 + self.numOfDigits  # 1 added to account for Game_count label
        self.create_header()
        # After the windows are built, we launch it
        self.root2.title("AI vs AI")
        #  self.root2.geometry('300x400')  # ENABLE TO FIX THE WINDOW SIZE
        self.root2.mainloop()

    def create_header(self):
        self.ans_label_1 = []
        self.ans_label_2 = []
        for i in range(self.numOfDigits):
            self.ans_label_1.append(Label(self.root2, text='?'))
            self.ans_label_2.append(Label(self.root2, text='?'))
            self.ans_label_1[i].grid(row=0, column=i)
            self.ans_label_2[i].grid(row=0, column=i+self.offset)
        game_num_label = Label(self.root2, text="game # "+str(self.currentGameNumber))
        game_num_label.grid(row=0, column=self.numOfDigits)
        game_num_label.after(self.sleeping_Time, self.populate_window)

    def populate_window(self):
        self.allGuesses_1 = self.currentGame_1.getGuesses()
        self.allGuesses_2 = self.currentGame_2.getGuesses()
        self.NB_1 = self.currentGame_1.getNBs()
        self.NB_2 = self.currentGame_2.getNBs()
        self.NH_1 = self.currentGame_1.getNHs()
        self.NH_2 = self.currentGame_2.getNHs()
        self.populateAllRows(1, 0)

    def populateAllRows(self, row_position, guess_index):
        SpinBoxList_1 = []
        SpinBoxList_2 = []
        current_guess_1 = self.allGuesses_1[guess_index]  # Get the current guess
        current_guess_2 = self.allGuesses_2[guess_index]
        # ### Place the numbers
        for column_idx in range(self.numOfDigits):
            SpinBoxList_1.append(Spinbox(self.root2, width=2))  # Make a new spinbox
            SpinBoxList_2.append(Spinbox(self.root2, width=2))  # Make a new spinbox
            SpinBoxList_1[column_idx].grid(row=row_position, column=column_idx)
            SpinBoxList_2[column_idx].grid(row=row_position, column=column_idx + self.offset)  # Put it on screen
            SpinBoxList_1[column_idx].insert(0, get_digit(current_guess_1, column_idx))  # Put a value in the spinbox
            SpinBoxList_2[column_idx].insert(0, get_digit(current_guess_2, column_idx))
            SpinBoxList_1[column_idx].config(state=DISABLED)  # Disable the spinbox because users shouldn't interfere
            SpinBoxList_2[column_idx].config(state=DISABLED)
        # ### Place the label of the guess-results
        guess_result_label_1 = Label(self.root2, text="Bull:"+str(self.NB_1[guess_index])+" Hits:" + str(self.NH_1[guess_index]))
        guess_result_label_2 = Label(self.root2, text="Bull:"+str(self.NB_2[guess_index])+" Hits:" + str(self.NH_2[guess_index]))
        guess_result_label_1.grid(row=row_position, column=self.numOfDigits)
        guess_result_label_2.grid(row=row_position, column=self.numOfDigits + self.offset)
        # ### Next step
        if guess_index < len(self.allGuesses_1)-1 and guess_index < len(self.allGuesses_2)-1:
            # We need more guesses, in the next row
            guess_result_label_1.after(self.sleeping_Time, lambda: self.populateAllRows(row_position+1, guess_index+1))
        else:
            # "current_guess" is equal to answer, and therefore we can send it as the answer
            guess_result_label_1.after(self.sleeping_Time, lambda: self.game_ender_setup(row_position+1))

    def game_ender_setup(self, row_position):
        # ### REVEAL THE ANSWER
        for column_idx in range(self.numOfDigits):
            self.ans_label_1[column_idx].config(text=get_digit(self.allGuesses_1[-1], column_idx), fg='Green', font="Helvetica 20 bold")
            self.ans_label_2[column_idx].config(text=get_digit(self.allGuesses_2[-1], column_idx), fg='Green', font="Helvetica 20 bold")
        # ### show how good was the attempt
        current_game_result = len(self.allGuesses_1) - len(self.allGuesses_2)
        res_text = "" 
        if current_game_result == 0:
            res_text = "Tie"
            self.score["tie"] += 1 
        elif current_game_result < 0:  # 1 wins
            res_text = "AI 1 wins"
            self.score["1 win"] += 1
        else:  # 2 wins
            res_text = "AI 2 wins"
            self.score["2 win"] += 1
            
        result_label = Label(self.root2, text=res_text)
        result_label.grid(row=row_position, column=self.numOfDigits, columnspan=5)
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
            self.currentGame_1 = bh.BH(0, self.numOfDigits)  # Play the next game in advance
            self.currentGame_2 = bh.BH(0, self.numOfDigits)
            self.create_header()  # This invokes the loop again
        
    def cleanWindow(self):
        for widget in self.root2.winfo_children():
            widget.destroy()


    def showFinalResults(self):
        # {"1 win" : 0 , "tie" : 0, "2 win" : 0} 
        res_text = "Times 1 won: " + str(self.score["1 win"]) + "\n"
        res_text += "Times 2 won: " + str(self.score["2 win"]) + "\n"
        res_text += "Times they tied: " + str(self.score["tie"]) + "\n"
        if self.score["1 win"] > self.score["2 win"]:
            res_text += "The winner is AI 1!"
        elif self.score["1 win"] < self.score["2 win"]:
            res_text += "The winner is AI 2!"
        else:
            res_text += "The result is a tie!"

        
        tkinter.messagebox.showinfo("RESULTS", res_text)


    




