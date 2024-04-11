from tkinter import *
root = Tk()
root.title('Hi')
# esto es para añadir iconos, claro hay que cambiar la ruta segun donde este el archivo
root.iconbitmap('C:/Users/rodri/Downloads/dev Img/Bambúf.ico')

# Uso de imagenes





button_quit = Button(root, text='Exit Program', command= root.quit)
button_quit.pack()

root.mainloop()