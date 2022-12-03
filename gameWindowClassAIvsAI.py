import tkinter.messagebox
from tkinter import *
import bh
import pygame


def get_digit(number, n):
    """ Gets the n-th digit position from the number, as a string
    :param number: The original number we're trying to get the digit from
    :type number: int or str
    :param n: The position (left-to-right), count starts from 0
    :type n: int
    :return: a string containing a single digit. e.g. '6'
    :rtype: str
    """

    stringNumber = str(number)
    return stringNumber[n]


class GameAIvsAI:
    def __init__(self, game_count=1, zero_included=0, num_of_digits=4, sound_included=1):
        """ init function
        :param game_count: Number of games to be played
        :type game_count: int
        :param zero_included: 0 if exclude the digit zero from the game, any other value otherwise
        :type zero_included: int
        :param num_of_digits: Number of digits to guess. This value commonly determines the size of a row
        :type num_of_digits: int
        :param sound_included: 0 if exclude the sound from the game, any other value otherwise
        :type sound_included: int
        """

        self.ans_label_1 = None  # [Per-Game] list of Labels, the size of [numOfDigits]
        self.ans_label_2 = None  # [Per-Game] list of Labels, the size of [numOfDigits]
        self.NH_1 = None  # [Per-Game] list of all Hits by order for AI1
        self.NB_1 = None  # [Per-Game] list of all Bulls by order for AI1
        self.NH_2 = None  # [Per-Game] list of all Hits by order for AI2
        self.NB_2 = None  # [Per-Game] list of all Bulls by order for AI2
        self.TableSizes1 = None  # [Per-Game] list of Table-Size per guess for AI1
        self.TableSizes2 = None  # [Per-Game] list of Table-Size per guess for AI2
        self.allGuesses_1 = None  # [Per-Game] list of all guesses by order for AI1
        self.allGuesses_2 = None  # [Per-Game] list of all guesses by order for AI2
        self.currentGame_1 = None  # The current game object for AI1
        self.currentGame_2 = None  # The current game object for AI2
        self.gameCount = game_count  # How many games we will play
        self.score = {"1 win": 0, "tie": 0, "2 win": 0}  # List the size of [gameCount] of how many guesses each game took to solve
        self.currentGameNumber = 1  # Current Game number out of [gameCount] games
        self.zeroIncluded = zero_included  # Boolean for including 0 or excluding
        self.soundIncluded = sound_included  # Boolean for including sound or excluding
        self.numOfDigits = num_of_digits  # How many numbers to guess (IS OFTEN USED FOR ROW SIZE)
        self.sleeping_Time = 1000  # Sleeping time adjustment
        self.offset = None
        self.root2 = Tk()  # ### THE CURRENT WINDOW.

        # ### ADJUST THE bh FILE PARAMETERS
        bh.Zero = zero_included
        bh.NumberOfGames = game_count
        bh.NumberOfDigits = num_of_digits

    def startGame(self):
        """
        Builds and launches a window, and invokes appropriate functions.
        Also initializes the sound, if necessary
        """

        if self.soundIncluded:
            pygame.mixer.init()
        self.currentGame_1 = bh.BH(0, self.numOfDigits)
        self.currentGame_2 = bh.BH(0, self.numOfDigits)
        self.offset = 3 + self.numOfDigits  # 1 added to account for Game_count label
        self.create_header()
        # After the windows are built, we launch it
        self.root2.title("AI vs AI")
        self.root2.mainloop()

    def create_header(self):
        """
        Place new header labels in the window, with '?' to signify a new game
        """

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
        """
        Starts a 'domino effect' by activating 'populateAllRows' with initial values
        """

        self.allGuesses_1 = self.currentGame_1.getGuesses()
        self.allGuesses_2 = self.currentGame_2.getGuesses()
        self.NB_1 = self.currentGame_1.getNBs()
        self.NB_2 = self.currentGame_2.getNBs()
        self.NH_1 = self.currentGame_1.getNHs()
        self.NH_2 = self.currentGame_2.getNHs()
        self.TableSizes1 = self.currentGame_1.getTableSizes()
        self.TableSizes2 = self.currentGame_2.getTableSizes()
        self.populateAllRows(1, 0)

    def populateAllRows(self, row_position, guess_index):
        """ Make a row of guess-controls, using recursion to fill the window with all rows
        :param row_position: Which row in the window should be written into
        :type row_position: int
        :param guess_index: The index in the self.allGuesses to extract info
        :type guess_index: int
        """

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
            SpinBoxList_1[column_idx].config(state=DISABLED, disabledforeground="RED")  # Disable the spinbox because users shouldn't interfere
            SpinBoxList_2[column_idx].config(state=DISABLED, disabledforeground="RED")
        # ### Place the label of the guess-results
        guess_result_label_1 = Label(self.root2, text="Bull:"+str(self.NB_1[guess_index])+" Hits:" + str(self.NH_1[guess_index]) + " Table Size:"+str(self.TableSizes1[guess_index]) + "  ")
        guess_result_label_2 = Label(self.root2, text="Bull:"+str(self.NB_2[guess_index])+" Hits:" + str(self.NH_2[guess_index]) + " Table Size:"+str(self.TableSizes2[guess_index]) + "  ")
        guess_result_label_1.grid(sticky="W", row=row_position, column=self.numOfDigits)
        guess_result_label_2.grid(sticky="W", row=row_position, column=self.numOfDigits + self.offset)
        # ### Next step
        if guess_index < len(self.allGuesses_1)-1 and guess_index < len(self.allGuesses_2)-1:
            if self.soundIncluded:
                pygame.mixer.music.load("Sounds/guess SFX.mp3")
                pygame.mixer.music.play(loops=0)
            # We need more guesses, in the next row
            guess_result_label_1.after(self.sleeping_Time, lambda: self.populateAllRows(row_position+1, guess_index+1))

        else:
            if self.soundIncluded:
                if len(self.allGuesses_1) == len(self.allGuesses_2):
                    pygame.mixer.music.load("Sounds/Human win sfx.mp3")
                elif len(self.allGuesses_2) > len(self.allGuesses_1):
                    pygame.mixer.music.load("Sounds/P1 win sfx.mp3")
                else:
                    pygame.mixer.music.load("Sounds/P2 win sfx.mp3")
                pygame.mixer.music.play(loops=0)

            # "current_guess" is equal to answer, and therefore we can send it as the answer
            guess_result_label_1.after(self.sleeping_Time, lambda: self.game_ender_setup(row_position+1))

    def game_ender_setup(self, row_position):
        """ Function called upon a correct guess, changes the Answer Labels to reveal the answer,
        and then call prepNextGame function
        :param row_position: The row position in the window to show the results
        :type row_position: int
        """

        # ### REVEAL THE ANSWER
        for column_idx in range(self.numOfDigits):
            self.ans_label_1[column_idx].config(text=get_digit(self.allGuesses_1[-1], column_idx), fg='Green', font="Helvetica 20 bold")
            self.ans_label_2[column_idx].config(text=get_digit(self.allGuesses_2[-1], column_idx), fg='Green', font="Helvetica 20 bold")
        # ### show how good was the attempt
        current_game_result = len(self.allGuesses_1) - len(self.allGuesses_2)
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
        """
        Check if this is the last game, and show final results, or clean the window, and start a new game.
        Increments appropriate attributes
        """

        if self.currentGameNumber == self.gameCount:  # happens if we played the LAST GAME
            self.showFinalResults()
        else:
            self.currentGameNumber += 1
            self.cleanWindow()
            self.currentGame_1 = bh.BH(0, self.numOfDigits)  # Play the next game in advance
            self.currentGame_2 = bh.BH(0, self.numOfDigits)
            self.create_header()  # This invokes the loop again
        
    def cleanWindow(self):
        """
        Remove every control from the window
        """

        for widget in self.root2.winfo_children():
            widget.destroy()

    def showFinalResults(self):
        """
        A function called when all games are finished, and shows the results of all games
        """

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
