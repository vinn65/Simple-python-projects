from tkinter import *
from random import randint, choice

App = Tk()

# App.title('App')
# App.title('Random Generator')
App.title('Entry')
App.geometry('350x100')

Display = Label(App, text="Application Window")
Display.pack()

# # def shw_msg():
# #     msg = Label(App, text=randint(1,100))
# #     msg.pack()

def pick():
    INP = (inp.get()).split()
    msg = Label(App, text=choice(INP))
    msg.pack()
# B.pack()
inp =  Entry(App)
inp.pack()
B = Button(App, text='Choose', command=pick)
B.pack()

quitB = Button(App, text='Cancel', command=App.quit)
quitB.pack()

App.mainloop() 