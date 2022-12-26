import tkinter.messagebox
from tkinter import *
import manualbh
import time  # AND SPACE!
import pygame


class GameHuman:
    def __init__(self, zero_included=0, num_of_digits=4, sound_included=1):
        """ init function
        :param zero_included: 0 if exclude the digit zero from the game, any other value otherwise
        :type zero_included: int
        :param num_of_digits: Number of digits to guess. This value commonly determines the size of a row
        :type num_of_digits: int
        :param sound_included: 0 if exclude the sound from the game, any other value otherwise
        :type sound_included: int
        """

        self.game_running = True
        self.ans_label = None
        self.timer_label = None
        self.currentGame = None
        self.timer = None
        self.current_row_number = 2
        self.numOfDigits = num_of_digits
        self.zeroIncluded = zero_included
        self.soundIncluded = sound_included
        self.root2 = Tk()
        self.root2.attributes("-topmost", True)

    def startGame(self):
        """
        Builds and launches a window, and invokes appropriate functions.
        Also initializes the sound, if necessary
        """

        if self.soundIncluded:
            pygame.mixer.init()
        self.currentGame = manualbh.ManualBH(self.numOfDigits, self.zeroIncluded)
        self.game_running = True
        self.current_row_number = 2
        self.create_header()
        self.make_guess_row()

    def create_header(self):
        """
        Place new header labels in the window, with '?' to signify a new game
        Header includes creating a clock
        """

        self.ans_label = []
        for index in range(self.numOfDigits):
            self.ans_label.append(Label(self.root2, text="?"))
            self.ans_label[index].grid(row=0, column=index)
        self.timer_label = Label(self.root2, text="00:00:00")
        self.timer_label.grid(row=0, column=self.numOfDigits)
        self.timer = time.time()
        self.timer_label.after(1000, lambda: self.clock_update())

    def make_guess_row(self):
        """
        Create a new guess row, including controls
        """

        spinBoxList = []
        values = []
        if self.zeroIncluded:
            min_val = 0
        else:
            min_val = 1
        for index in range(self.numOfDigits):
            values.append(tkinter.StringVar(value=min_val))
            spinBoxList.append(Spinbox(self.root2,
                                       width=1,
                                       from_=min_val,
                                       to=9,
                                       textvariable=values[index],
                                       wrap=True,
                                       state = 'readonly'))

            spinBoxList[index].grid(row=self.current_row_number, column=index)
        submit_button = Button(self.root2, text="Submit", padx=5, pady=5, command=lambda: self.submit_guess(spinBoxList, submit_button))
        submit_button.grid(row=self.current_row_number, column=self.numOfDigits)

    def clock_update(self):
        """
        Change the clock label every second, and invoke itself one second later (if game is running)
        """

        elapsed_time = time.time() - self.timer
        self.timer_label.config(text=time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))
        if self.game_running:
            self.timer_label.after(1000, lambda: self.clock_update())

    def submit_guess(self, spin_box_list, button):
        """ Function invoked on 'submit' button-press, check if guess is correct
        :param spin_box_list: A list of spin-boxes of the current row
        :type spin_box_list: list of tkinter.Spinbox
        :param button: The 'submit' button of the current row. It will be replaced with a Label
        :type button: tkinter.Button
        """

        guess = []
        button.destroy()  # Delete the button
        for index in range(self.numOfDigits):
            guess.append(int(spin_box_list[index].get()))
            spin_box_list[index].config(state=DISABLED, disabledforeground="RED")
        self.currentGame.get_guess(guess)
        nh = self.currentGame.nh
        nb = self.currentGame.bh
        res_label = Label(self.root2, text="Bull:"+str(nb)+" Hits:"+str(nh))
        res_label.grid(row=self.current_row_number, column=self.numOfDigits)
        if nb == self.numOfDigits:
            pygame.mixer.music.load("Sounds/Human win sfx.mp3")
            pygame.mixer.music.play(loops=0)
            self.game_running = False
            self.endgame()
        else:
            pygame.mixer.music.load("Sounds/guess SFX.mp3")
            pygame.mixer.music.play(loops=0)
            self.current_row_number += 1
            self.make_guess_row()

    def endgame(self):
        """
        Function called upon a correct guess, changes the Answer Labels to reveal the answer, and show the results
        """

        answer = self.currentGame.get_cypher()
        for index in range(self.numOfDigits):
            self.ans_label[index].config(text=str(answer[index]), fg='Green', font="Helvetica 20 bold")
        num_of_guesses = self.current_row_number - 1
        elapsed_time = self.timer_label.cget("text")
        # tkinter.messagebox.showinfo("RESULTS", "Total guesses: " + str(num_of_guesses) + "\nTime: " + elapsed_time)
        resultText = "Total guesses: " + str(num_of_guesses) + "\nTime: " + elapsed_time
        finalResultLabel = Label(self.root2, text=resultText)
        finalResultLabel.grid(row=self.current_row_number+1, column=0, columnspan=10)
