import tkinter.messagebox
from tkinter import *
import bh
import time  # AND SPACE!
import gameWindowClassAI
import gameWindowClassAIvsAI
import gameWindowClassHuman


def run_manual_games():
    return    


def StartGame(player_type, game_count=1, zero_included=0, num_of_digits=4, delayvalue=0):
    if player_type == "AI":
        my_game = gameWindowClassAI.GameAI(game_count, zero_included, num_of_digits)
        my_game.sleeping_Time = delayvalue
        my_game.startGame()

    elif player_type == "AIvsAI":
        my_game = gameWindowClassAIvsAI.GameAIvsAI(game_count, zero_included, num_of_digits)
        my_game.sleeping_Time = delayvalue
        my_game.startGame()

    else:
        my_game = gameWindowClassHuman.GameHuman(zero_included, num_of_digits)
        my_game.startGame()

