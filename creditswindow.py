from tkinter import *
import webbrowser


def callback(url):
    webbrowser.open_new(url)


class CreditsWindow:
    def __init__(self):
        self.root2 = Tk()
        self.root2.title("Credits")
        Text0 = Label(self.root2, text="   Game made by:  \n\n  Natty Zepko   ")
        Text0.pack()

        Text1 = Label(self.root2, text="   Natty.zepko@gmail.com   ", fg="blue", cursor="hand2")
        Text1.pack()
        Text1.bind("<Button-1>", lambda e: callback("mailto:Natty.zepko@gmail.com"))

        Text2 = Label(self.root2, text="  \n  and \n\n  Eyal Itzhak  ")
        Text2.pack()

        Text3 = Label(self.root2, text="  Eyalpross101@gmail.com  ", fg="blue", cursor="hand2")
        Text3.pack()
        Text3.bind("<Button-1>", lambda e: callback("mailto:Eyalpross101@gmail.com"))

        self.root2.mainloop()




