from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog

root = Tk()
root.title('Open files')
root.iconbitmap('C:/Users/rodri/Desktop/In dev/VN-parser/tkinter use/Img examples/Bambúf.ico')

def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir='C:/Users/rodri/Desktop/In dev/VN-parser/tkinter use/Img examples', title='Select a File', filetypes=(('png files', '*.png'),('all files', '*.*')))
    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()

my_btn = Button(root, text='Open File', command=open).pack()

mainloop()