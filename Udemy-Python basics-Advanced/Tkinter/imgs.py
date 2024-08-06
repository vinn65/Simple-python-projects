from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

app = Tk()

app.title("")

# app.iconbitmap(r'loc/location.ico')

# img=  ImageTk.PhotoImage(Image.open(r'Figure_1.png'))

# lbl = Label(app, image=img)
# lbl.pack()
def img_select():
    global img
    app.fname = filedialog.askopenfilename(initialdir='.', title="Choose", filetypes=(('Images','*.jpg'),("All",'*.*') ))

    img=  ImageTk.PhotoImage(Image.open(app.fname))

    lbl = Label(app, image=img)
    lbl.pack()
B = Button(app, text="view", command=img_select)
B.pack()
app.mainloop()