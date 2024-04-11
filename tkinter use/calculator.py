import tkinter as tk
numbers_buttons= []
root = tk.Tk()
root.title('Calculadora con tk')
e = tk.Entry(root, width=35, borderwidth=5)
e.grid(row=1, column=0, columnspan=3, padx=30, pady=15)
# e.insert(0, '')


def button_click(number):
    current = e.get()
    e.delete(0, tk.END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, tk.END)

def button_add():
    global f_num
    global math
    first_number = e.get()
    math = 'addition'
    f_num= int(first_number)
    e.delete(0, tk.END)

def button_equal():
    second_number = e.get()
    e.delete(0, tk.END)
    if math == 'addition':
        e.insert(0, f_num + int(second_number))
    if math == 'subtraction':
        e.insert(0, f_num - int(second_number))
    if math == 'multiplication':
        e.insert(0, f_num * int(second_number))
    if math == 'division':
        e.insert(0, f_num / int(second_number))

def button_res():
    global f_num
    global math
    first_number = e.get()
    math = 'subtraction'
    f_num= int(first_number)
    e.delete(0, tk.END)
    
def button_mul():
    global f_num
    global math
    first_number = e.get()
    math = 'multiplication'
    f_num= int(first_number)
    e.delete(0, tk.END)

def button_div():
    global f_num
    global math
    first_number = e.get()
    math = 'division'
    f_num= int(first_number)
    e.delete(0, tk.END)


# Definir botones

for i in range(0, 10):
    button= tk.Button(root, text=f'{i}', padx=30, pady=15, command=lambda num=i: button_click(num))
    numbers_buttons.append(button)

# POner los botones en pantalla
for i in range(0, 10):
    if i == 0:
        row = 5
        column = 0
    else:
        row = (9 - i) // 3 + 2
        column = (i - 1) % 3

    numbers_buttons[i].grid(row=row, column=column)

buttonSum = tk.Button(root, text='+', padx=29, pady=15, command=button_add)
buttonRes = tk.Button(root, text='-', padx=30, pady=15, command=button_res)
buttonMul = tk.Button(root, text='*', padx=30, pady=15, command=button_mul)
buttonDiv = tk.Button(root, text='/', padx=30, pady=15, command=button_div)
buttonEqual = tk.Button(root, text='=', padx=77, pady=15, command=button_equal)
buttonClear = tk.Button(root, text='Clear', padx=67, pady=15, command=button_clear)



buttonClear.grid(row=5, column=1, columnspan=2)
buttonEqual.grid(row=6, column=1, columnspan=2)
buttonSum.grid(row=6, column=0)
buttonRes.grid(row=7, column=0, rowspan=2)
buttonMul.grid(row=7, column=1, rowspan=2)
buttonDiv.grid(row=7, column=2, rowspan=2)


root.mainloop()