from tkinter import *

dice = {
    0 : '🎲',
    1 : '⚀',
    2 : '⚁',
    3 : '⚂',
    4 : '⚃',
    5 : '⚄',
    6 : '⚅'
}


App = Tk()
App.title("Dice")
dic_e = Label(App, text=dice[0], font = ('Times', 100,), foreground="white")
dic_e.grid(row=0, column=0, pady=5, padx=25)


def roll():
    from random import randint
    i = randint(1,6)
    msg = Label(App, text=dice[i], font = ('Times', 100), foreground="white", width=2)
    msg.grid(row=0, column=0, padx=25, pady=5)


rollB = Button(App, text="Roll", command=roll)
rollB.grid(row=1, column=0)

App.mainloop()