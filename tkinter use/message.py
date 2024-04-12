from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title('Message boxes')
root.iconbitmap('C:/Users/rodri/Desktop/In dev/VN-parser/tkinter use/Img examples/Bambúf.ico')


# dependiendo de lo que pongamos luego del punto mostrara una u otra cosa: showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    response = messagebox.askquestion('This is a Popup!', 'Hello world')
    Label(root, text=response).pack()

# El siguiente if puede ser con strings o con numeros
    if response == 'yes':
        Label(root, text='You clicked yes').pack()
    else:
        Label(root, text='You clicked no').pack()

Button(root, text='Popup', command=popup).pack()

mainloop()