from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('Radio buttons')
root.iconbitmap('C:/Users/rodri/Desktop/In dev/VN-parser/tkinter use/Img examples/Bambúf.ico')

# IntVar es porque es un numero, si quisieramos fuera un string seria strVar
# r = IntVar()
# r.set('2')

MODES = [
    ('Pepperoni','Pepperoni'),
    ('Cheese','Cheese'),
    ('Mushroom','Mushroom'),
    ('Onion','Onion'),
]

pizza = StringVar()
pizza.set(' ')

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)

def click(value):
    myLabel = Label(root, text=value)
    myLabel.pack()

# Radiobutton(root, text='Option 1', variable=r, value=1, command=lambda: click(r.get())).pack()
# Radiobutton(root, text='Option 2', variable=r, value=2, command=lambda: click(r.get())).pack()




# myLabel = Label(root, text=pizza.get())
# myLabel.pack()

myButton = Button(root, text='Choose!', command=lambda: click(pizza.get()))
myButton.pack()

mainloop()