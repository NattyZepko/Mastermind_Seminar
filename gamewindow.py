import tkinter.messagebox
from tkinter import *
import bh
import time  # AND SPACE!
import gameWindowClassAI

# gameCount=1
# zeroIncluded=0
# numOfDigits = 4
# SleepingTime=0



# ### Return the n-th digit of a number


# def create_header(idx_game,root2):
#     ans_label=[]
#     for i in range(numOfDigits):
#         ans_label.append(Label(root2,text='?'))
#         ans_label[i].grid(row=0,column=i)
#     game_num_label= Label(root2,text="game # "+str(idx_game+1))    
#     game_num_label.grid(row=0,column=numOfDigits)


# def run_AI_games(root2):
#     # for idx_game in range(gameCount):
#         create_header(0,root2)


   

def run_menual_games():
    return    

def StartGame(player_type, game_count=1, zero_included=0, num_of_digits=4):
    # # gameWindow = Toplevel()
    # root2 = Tk()
    # bh.Zero = zero_included
    # bh.NumberOfGames = game_count
    # bh.NumberOfDigits = num_of_digits
    # # updating blobal parameters
    # gameCount=game_count
    # zeroIncluded=zero_included
    # numOfDigits=num_of_digits
    # SleepingTime = 0

    if player_type == "AI":
        print("AI")
        # run_AI_games(root2)
        my_game=gameWindowClassAI.Game_AI(game_count,zero_included,num_of_digits)
        my_game.startGame()

    else:
        print("TO DO") 
        run_menual_games()

    # root2.mainloop()
