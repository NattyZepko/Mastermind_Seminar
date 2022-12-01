import tkinter.messagebox
from tkinter import *
import manualbh
import time  # AND SPACE!


class GameHuman:
    def __init__(self, zero_included=0, num_of_digits=4):
        self.game_running = True
        self.ans_label = None
        self.timer_label = None
        self.currentGame = None
        self.timer = None
        self.current_row_number = 2
        self.numOfDigits = num_of_digits
        self.zeroIncluded = zero_included
        self.root2 = Tk()

    def startGame(self):
        self.currentGame = manualbh.ManualBH(self.numOfDigits, self.zeroIncluded)
        self.game_running = True
        self.current_row_number = 2
        self.create_header()
        self.make_guess_row()

    def create_header(self):
        self.ans_label = []
        for index in range(self.numOfDigits):
            self.ans_label.append(Label(self.root2, text="?"))
            self.ans_label[index].grid(row=0, column=index)
        self.timer_label = Label(self.root2, text="00:00:00")
        self.timer_label.grid(row=0, column=self.numOfDigits)
        self.timer = time.time()
        self.timer_label.after(1000, lambda: self.clock_update())

    def make_guess_row(self):
        spinBoxList = []
        values = []
        if self.zeroIncluded:
            minval = 0
        else:
            minval = 1
        for index in range(self.numOfDigits):
            values.append(tkinter.StringVar(value=minval))
            spinBoxList.append(Spinbox(self.root2,
                                       width=1,
                                       from_=minval,
                                       to=9,
                                       textvariable=values[index],
                                       wrap=True))

            spinBoxList[index].grid(row=self.current_row_number, column=index)
        submit_button = Button(self.root2, text="Submit", padx=5, pady=5, command=lambda: self.submit_guess(spinBoxList, submit_button))
        submit_button.grid(row=self.current_row_number, column=self.numOfDigits)

    def clock_update(self):
        elapsed_time = time.time() - self.timer
        self.timer_label.config(text=time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))
        if self.game_running:
            self.timer_label.after(1000, lambda: self.clock_update())

    def submit_guess(self, spin_box_list, button):
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
            self.game_running = False
            self.endgame()
        else:
            self.current_row_number += 1
            self.make_guess_row()

    def endgame(self):
        answer = self.currentGame.get_cypher()
        for index in range(self.numOfDigits):
            self.ans_label[index].config(text=str(answer[index]), fg='Green', font="Helvetica 20 bold")
        num_of_guesses = self.current_row_number - 1
        elapsed_time = self.timer_label.cget("text")
        tkinter.messagebox.showinfo("RESULTS", "Total guesses: " + str(num_of_guesses) + "\nTime: " + elapsed_time)
