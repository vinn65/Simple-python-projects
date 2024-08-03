from tkinter import *
from random import randint, sample

App = Tk()

# App.title('App')
# App.title('Random Generator')
App.title('Entry')
App.geometry('220x150')
App['background'] = 'white'
# Display = Label(App, text="Application Window")
# Display.grid()

# # def shw_msg():
# #     msg = Label(App, text=randint(1,100))
# #     msg.grid()

no_choice = IntVar()

# rb1 = Radiobutton(App, text='1', variable=no_choice, value=1)
# rb2 = Radiobutton(App, text='2', variable=no_choice, value=2)
# rb1.grid(row=1, column=0)
# rb2.grid(row=1, column=2)

sld = Scale(App, from_= 1, to=5, variable=no_choice, orient=HORIZONTAL)

sld.grid(row=1, column=0, columnspan=2, padx=25, pady=5)
# chek = Checkbutton(App, text='Double', variable=no_choice, onvalue=2, offvalue=1)
# chek.deselect()
# chek.grid(row=1, column=0, columnspan=2, padx=25, pady=5)

def pick():
    INP = (inp.get()).split()
    if no_choice.get() >= 1:
        ele = sample(INP, no_choice.get())
        lbl = '' 
        for e in ele:
            lbl += '' + e
        chos = "Choice: "+str(lbl)
    else: 
        ele = sample(INP, 1)
        chos = "Choice: " + str(ele[0])
    # msg = Label(App, text=chos, font=('Courier', 12), background='white', foreground='black')

    butwin = Toplevel()
    butwin.title("Output")

    msg = Label(butwin, text=chos, relief='raised', width=25, borderwidth=4)
    msg.grid(row=3, column=0, padx=25, pady=5)


    if quitB['state'] == DISABLED:
        quitB['state'] = NORMAL

# B.grid()
inp =  Entry(App, relief='raised', borderwidth=1, width=25)
inp.grid(row=0, column=0, columnspan=2, padx=25, pady=5)
B = Button(App, text='Choose', relief='groove', command=pick, borderwidth=5)
B.grid(row=2, column=0, padx=25, pady=5)

quitB = Button(App, text='Cancel', command=App.quit, state=DISABLED, relief='groove', borderwidth=5)
quitB.grid(row=2, column=1, padx=25, pady=5)

App.mainloop()