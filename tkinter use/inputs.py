import tkinter as tk

root = tk.Tk()
# Es aqui tambien donde se puede cambiar el tamaño del "entry", 
# y tambien se puede cambiar el color del mismo modo que en los botones
# tambien se puede hacer con el borde con borderwidth=number
e = tk.Entry(root, width=50, borderwidth=5)
e.pack()
# Esto nos permite poner un texto que hay que borrar pero dice que hay que hacer
e.insert(0, 'Enter your name: ')

def myClick():
    hello = 'Hello ' + e.get()
    myLabel= tk.Label(root, text=hello)
    myLabel.pack()

# Se puede desabilitar con state='disabled' y los pads son el tamaño ya sea horizontal(x) o vertical(y)
# si queremos cambiar de colores: fg='color' haria que el texto tome ese color, bg='color' seria para el fondo
my_button = tk.Button(root, text= 'Submit', command=myClick)

my_button.pack()

root.mainloop()