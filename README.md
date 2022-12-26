
# Mastermind - Game

A Python-based project that aims to simulate the board game "Mastermind".
In addition, an AI was built that solves the problem through the implementation of Knuth's algorithm (an efficient solution to the problem).

- [About the game](https://en.wikipedia.org/wiki/Mastermind_(board_game))

- [The algorithm](https://www.cs.uni.edu/~wallingf/teaching/cs3530/resources/knuth-mastermind.pdf)








## Authors

- [@NattyZepko](https://github.com/NattyZepko)

- [@eyalItzhak](https://github.com/eyalItzhak)


 
## Features

- AI Solve - solving the problem by the computer. At the end, statistics will be displayed (i.e. how many guesses on average the computer guessed in order to reach the solution).
- AI vs AI - similar to AI Solve only that this time the computer plays against itself and at the end prepares statistics about how many times computer 1 won, how many times computer 2 won, or there was a tie between the computers.
- Human Solve - an option for the user to try playing the game himself.



## Documentation

tkinter library is used for graphical display:

[tkinter package](https://docs.python.org/3/library/tkinter.html)

Python documentation -(In Red):
![App Screenshot](https://user-images.githubusercontent.com/62293316/209551292-43ca17e8-d756-4f61-b193-de6b70845850.png)

bh class - Algorithm AI, the implementation of Knuth's algorithm.

gameWindowClass X class - Creating a new game window according to the user's choice.

Ui class - The main window.
## Installation

It is recommended to install all the relevant files using "pip install"
```bash
  pip instal ...
```
Then run the ui.py file

```bash
  python3 ui.py
```

## Screenshots
main page:

![App Screenshot](https://user-images.githubusercontent.com/62293316/209550050-63b324a5-d1e7-4297-b560-bef8b65b356f.png)


AI solve :

![App Screenshot](https://user-images.githubusercontent.com/62293316/209550196-d5964672-3942-4407-8699-d64eb94f5934.png)

![App Screenshot](https://user-images.githubusercontent.com/62293316/209550237-254a453a-97a6-4cbe-9e62-6615118f8e41.png)

AI vs AI:

![App Screenshot](https://user-images.githubusercontent.com/62293316/209550337-f9e2025e-a131-494a-83e8-472e2fc5f815.png)

Human Solve:

![App Screenshot](https://user-images.githubusercontent.com/62293316/209550392-7be43f31-fd2c-49f2-a383-2718c812cbde.png)
