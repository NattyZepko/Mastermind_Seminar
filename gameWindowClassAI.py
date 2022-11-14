import tkinter.messagebox
from tkinter import *
import bh
import time  # AND SPACE!


def get_digit(number, n):
    stringNumber = str(number)
    return stringNumber[n]


class GameAI:
    def __init__(self,game_count=1, zero_included=0, num_of_digits=4):
        self.NH = None
        self.NB = None
        self.allGuesses = None
        self.currentGame = None
        self.gameCount=game_count
        self.zeroIncluded=zero_included
        self.numOfDigits=num_of_digits 
        self.sleeping_Time = 1000
        self.root2 = Tk()

        bh.Zero = zero_included
        bh.NumberOfGames = game_count
        bh.NumberOfDigits = num_of_digits

    def startGame(self):
        for idx_game in range(self.gameCount):
            self.currentGame = bh.BH(0, self.numOfDigits)
            self.create_header(idx_game)
            # After the windows are built, we launch it
        self.root2.mainloop()

    def populate_window(self):
        self.allGuesses = self.currentGame.getGuesses()
        self.NB=self.currentGame.getNBs()
        self.NH=self.currentGame.getNHs()
        self.populateAllRows(1, 0)

    def populateAllRows(self, row_position, guess_index):
        SpinBoxList = []
        current_guess = self.allGuesses[guess_index]
        for column_idx in range(self.numOfDigits):  
            SpinBoxList.append(Spinbox(self.root2, width=2))
            SpinBoxList[column_idx].grid(row=row_position, column=column_idx)
            SpinBoxList[column_idx].insert(0, get_digit(current_guess, column_idx))
            SpinBoxList[column_idx].config(state=DISABLED)
        guess_result_label = Label(self.root2, text="Bull:"+str(self.NB[guess_index])+" Hits:" + str(self.NH[guess_index]))
        guess_result_label.grid(row=row_position, column=self.numOfDigits)
        if guess_index < len(self.allGuesses)-1:
            guess_result_label.after(self.sleeping_Time, lambda: self.populateAllRows(row_position+1, guess_index+1))

    def create_header(self, idx_game):
        ans_label=[]
        for i in range(self.numOfDigits):
            ans_label.append(Label(self.root2,text='?'))
            ans_label[i].grid(row=0,column=i)
        game_num_label= Label(self.root2,text="game # "+str(idx_game+1))    
        game_num_label.grid(row=0,column=self.numOfDigits)
        game_num_label.after(self.sleeping_Time, self.populate_window)

