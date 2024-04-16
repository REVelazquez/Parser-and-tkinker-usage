from tkinter import *
from PIL import Image, ImageTk


root = Tk()
root.title('Dropdown')
root.iconbitmap('C:/Users/rodri/Desktop/In dev/VN-parser/tkinter use/Img examples/Bambúf.ico')
root.geometry('400x400')

# Drop Down boxes:
# Son generalmente llamados como option menus, o menus de opciones

def show():
    myLabel = Label(root, text = clicked.get()).pack()

options = [
    'Monday', 
    'Tuesday', 
    'Wednesday', 
    'Thurday', 
    'Friday',
    'Saturday'
]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
drop.pack()

my_button = Button(root, text='Show Selection', command=show).pack()

mainloop()