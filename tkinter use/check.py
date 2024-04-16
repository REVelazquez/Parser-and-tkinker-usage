from tkinter import *
from PIL import Image, ImageTk


root = Tk()
root.title('Slider')
root.iconbitmap('C:/Users/rodri/Desktop/In dev/VN-parser/tkinter use/Img examples/Bambúf.ico')
root.geometry('400x400')

var = StringVar()

c = Checkbutton(root, text='Check this box, I dare you!', variable=var, onvalue='on', offvalue='off')
c.deselect()
c.pack()
def show():
    my_label= Label(root, text=var.get()).pack()

button = Button(root, text='Show selection', command=show).pack()
mainloop()