from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Hi')
# esto es para añadir iconos, claro hay que cambiar la ruta segun donde este el archivo

root.iconbitmap('C:/Users/rodri/Desktop/In dev/VN-parser/tkinter use/Img examples/Bambúf.ico')

# Uso de imagenes, claro esto es solo para una imagen.
my_img = ImageTk.PhotoImage(Image.open('C:/Users/rodri/Desktop/In dev/VN-parser/tkinter use/Img examples/Ejemplo1.png'))
my_label = Label(image=my_img)
my_label.pack()



button_quit = Button(root, text='Exit Program', command= root.quit)
button_quit.pack()

root.mainloop()