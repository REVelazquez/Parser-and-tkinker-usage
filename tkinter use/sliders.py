from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog

root = Tk()
root.title('Slider')
root.iconbitmap('C:/Users/rodri/Desktop/In dev/VN-parser/tkinter use/Img examples/Bambúf.ico')
root.geometry('400x400')

vertical = Scale(root, from_=0, to=200)
vertical.pack()

def slide():
    my_label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + 'x' + str(vertical.get()))


horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL)
horizontal.pack()

my_label = Label(root, text=horizontal.get()).pack()

my_btn = Button(root, text='Click me!', command=slide).pack()


mainloop()