from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('New windows')
root.iconbitmap('C:/Users/rodri/Desktop/In dev/VN-parser/tkinter use/Img examples/Bambúf.ico')

def open():
    global my_img
    top = Toplevel()
    top.title('New windows 2')
    top.iconbitmap('C:/Users/rodri/Desktop/In dev/VN-parser/tkinter use/Img examples/Bambúf.ico')
    my_img = ImageTk.PhotoImage(Image.open('C:/Users/rodri/Desktop/In dev/VN-parser/tkinter use/Img examples/Ejemplo1.png'))
    my_label = Label(top, image=my_img).pack()  
    btn2 = Button(top, text='Close window', command=top.destroy).pack()

btn = Button(root, text='Open 2nd Window', command=open).pack()

mainloop()