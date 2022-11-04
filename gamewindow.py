from tkinter import *
import bh


def StartGame(player_type, game_count = 1, black_included=0, num_of_colors=4):
    gameWindow = Toplevel()
    bh.Zero = black_included
    bh.NumberOfGames = game_count
    bh.NumberOfDigits = num_of_colors
    bh.main()



