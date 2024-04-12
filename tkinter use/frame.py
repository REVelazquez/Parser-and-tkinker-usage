from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('Frames in GUI')
root.iconbitmap('C:/Users/rodri/Desktop/In dev/VN-parser/tkinter use/Img examples/Bambúf.ico')

# Este padx y pady es para lo que se encuentra dentro del frame
frame = LabelFrame(root, padx=50, pady=50)
# Este padx y pady es para el espacio en donde se encuentra el frame
frame.pack(padx=10, pady=10)

b = Button(frame, text="Don't click here")
b2 = Button(frame, text="Or here")
b.grid(row=0, column=0)
b2.grid(row=1, column=1)

root.mainloop()