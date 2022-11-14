import tkinter.messagebox
from tkinter import *
import bh
import time  # AND SPACE!
import gameWindowClassAI


def run_manual_games():
    return    


def StartGame(player_type, game_count=1, zero_included=0, num_of_digits=4):
    if player_type == "AI":
        print("AI")
        my_game = gameWindowClassAI.GameAI(game_count, zero_included, num_of_digits)
        my_game.startGame()

    else:
        print("TO DO") 
        run_manual_games()

