from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Image visor')

# esto es para añadir iconos, claro hay que cambiar la ruta segun donde este el archivo
root.iconbitmap('C:/Users/rodri/Desktop/In dev/VN-parser/tkinter use/Img examples/Bambúf.ico')

# Uso de imagenes.
my_img1 = ImageTk.PhotoImage(Image.open('C:/Users/rodri/Desktop/In dev/VN-parser/tkinter use/Img examples/Ejemplo1.png'))
my_img2= ImageTk.PhotoImage(Image.open('C:/Users/rodri/Desktop/In dev/VN-parser/tkinter use/Img examples/Ejemplo2.png'))
my_img3 = ImageTk.PhotoImage(Image.open('C:/Users/rodri/Desktop/In dev/VN-parser/tkinter use/Img examples/Ejemplo3.png'))
my_img4 = ImageTk.PhotoImage(Image.open('C:/Users/rodri/Desktop/In dev/VN-parser/tkinter use/Img examples/Ejemplo4.png'))

image_list =[my_img1, my_img2, my_img3, my_img4, ]

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, padx=50, pady=80, columnspan= 3)

# Funciones
def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text='>>', command= lambda: forward(image_number+1))
    button_back = Button(root, text='<<',width=2, command=lambda: back(image_number-1))

    if image_number == 4:
        button_forward =     button_forward = Button(root, text='>>', state=DISABLED)

    my_label.grid(row=0, column=0, columnspan= 3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

def back(image_number):
    global my_label
    global button_foward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text='>>', command= lambda: forward(image_number+1))
    button_back = Button(root, text='<<',width=2, command=lambda: back(image_number-1))

    if image_number== 1:
        button_back = Button(root, text='<<',width=2, state=DISABLED)

    my_label.grid(row=0, column=0, columnspan= 3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


# Botones
button_back = Button(root, text='<<',width=2, state=DISABLED)
button_exit = Button(root, text='Exit Program', command=root.quit)
button_forward = Button(root, text='>>', width=2, command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()