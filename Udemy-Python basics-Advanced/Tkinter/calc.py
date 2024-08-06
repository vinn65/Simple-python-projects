from tkinter import *
from datetime import datetime

bg = 'black'
fg = 'cyan'
App = Tk()

App.title("Age Calculator")
App['background'] = bg

App.geometry('250x250')

msg = Label(App, text="Enter DOB", background=bg, foreground=fg)
msg.grid(row=0, column=0, columnspan=3)

dayl = Label(App, text='Day: ', background=bg, foreground=fg)
dayE = Entry(App, width = 2, background=bg, foreground=fg)

monl = Label(App, text='Month: ', background=bg, foreground=fg)
monE = Entry(App, width = 2, background=bg, foreground=fg)

yrl = Label(App, text='Year: ', background=bg, foreground=fg)
yrE = Entry(App, width = 2, background=bg, foreground=fg)

dayl.grid(row=1, column=0)
dayE.grid(row=1, column=1)
monl.grid(row=1, column=2)
monE.grid(row=1, column=3)
yrl.grid(row=1, column=4)
yrE.grid(row=1, column=5)

def find_days():
    date = int(dayE.get())
    mon = int(monE.get())
    year = int(yrE.get())

    dob = datetime(day = date, month=mon, year=year)

    time_now = datetime.now()
    time_dif = time_now - dob


    age = Label(App, text="Your Age : " + str(time_dif), background=bg, foreground=fg)
    age.grid(row=3, column=0, columnspan=4)

def find_seconds():
    date = int(dayE.get())
    mon = int(monE.get())
    year = int(yrE.get())

    dob = datetime(day = date, month=mon, year=year)

    time_now = datetime.now()
    time_dif = time_now - dob
    
    seonds = Label(App, text="Your age in seconds: " +str(time_dif.total_seconds()) + 'Seconds', background=bg, foreground=fg)
    seonds.grid(row=4, column=0, columnspan=6)

dysB = Button(App, text="Total Days", command=find_days, background=bg, foreground=fg)
scsB = Button(App, text="Total Seconds", command=find_seconds, background=bg, foreground=fg)

dysB.grid(row=2, column=0, columnspan=3)
scsB.grid(row=2, column=3, columnspan=3)


    

App.mainloop()

