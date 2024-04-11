import tkinter as tk

root = tk.Tk()

def myClick():
    myLabel= tk.Label(root, text='Look! I clicked a Button')
    myLabel.pack()

# Se puede desabilitar con state='disabled' y los pads son el tamaño ya sea horizontal(x) o vertical(y)
# si queremos cambiar de colores: fg='color' haria que el texto tome ese color, bg='color' seria para el fondo
my_button = tk.Button(root, text= 'Click me!', command=myClick)

my_button.pack()

root.mainloop()