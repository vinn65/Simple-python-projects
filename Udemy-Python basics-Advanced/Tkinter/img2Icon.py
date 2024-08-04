from tkinter import *

App =Tk()
App.title("Ico Convertor")

def open_img():
    global img
    from PIL import Image
    from tkinter import filedialog
    App.img_dir = filedialog.askopenfilename(initialdir=".", title= "Image to convert", filetypes=(
        ("PNG Files", "*.png"),("JPG files",'*.jpg'), ('All files','*.*')

    ))
    img = Image.open(App.img_dir)

def convrt_img():
    from PIL import Image
    # App.ico_name
    img.save(f'{ico_name.get()}.ico', format='ICO', sizes= [(ico_size.get(), ico_size.get())])

    success = Toplevel()
    success.title("Success")

    msg = Label(success, text = "Conversion Completed")
    msg.pack()

    success.mainloop()

def preview():
    from PIL import Image, ImageTk
    prev = Toplevel()
    prev.title("Icon preview")
    prev.iconbitmap(f'{ico_name.get()}.ico')

    pre_lbl = Label(prev, text="Checkout your Icon!")
    pre_lbl.pack()

    previmg = ImageTk.getimage(photo={ico_name.get()})
    lbld = Label(prev, image=previmg)
    lbld.pack()

    prev.mainloop()

choose_lbl = Label(App, text="Select your image:")
choose_lbl.grid(row=0, column=0, pady=10)

choosB = Button(App, text="Choose", command=open_img)
choosB.grid(row=0,  column=1, pady=10)


sizel = Label(App,text="Size for Icon" )
sizel.grid(row=1, column=0, pady=10)
ico_size = IntVar()
sizes_opts = [16,24,32,48,64,128,256]
ico_size.set(32)

size_menu = OptionMenu(App, ico_size, *sizes_opts)
size_menu.grid(row=1, column=2, pady=10)

fnameL = Label(App, text="Enter Icon name:")
fnameL.grid(row=2, column=0, pady=10)

ico_name = Entry(App)
ico_name.grid(row=2, column=1, pady=10)

convB = Button(App, text= "Convert", command=convrt_img)
convB.grid(row=3, column=0, pady=10)

prevB = Button(App, text="Preview", command=preview)
prevB.grid(row=3, column=1, pady=10)


App.mainloop()
