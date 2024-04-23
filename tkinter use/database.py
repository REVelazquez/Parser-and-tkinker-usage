from tkinter import *
from PIL import Image, ImageTk
import sqlite3


root = Tk()
root.title('Database')
root.iconbitmap('C:/Users/rodri/Desktop/In dev/VN-parser/tkinter use/Img examples/Bambúf.ico')
root.geometry('400x400')

# Databases

# Create or connect a database
conn = sqlite3.connect('address_book.db')

# Cursor: es el que hace todo en la base de datos
# Instancia de cursor, o crear el cursor
c = conn.cursor()

# Create table:
# c.execute("""CREATE TABLE addresses (
#           first_name text,
#           last_name text,
#           address text,
#           city text,
#           state text,
#           zipcode integer
#     )""")

# Create submit function
def submit():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    # Inset into Table
    c.execute('INSERT INTO addresses VALUES (:f_name, :last_name, :address, :city, :state, :zipcode)', 
                {
                    'f_name': f_name.get(),
                    'last_name': last_name.get(),
                    'address': address.get(),
                    'city': city.get(),
                    'state': state.get(),
                    'zipcode': zipcode.get()
                })

    conn.commit()
    conn.close()
    # Clear the text boxes
    f_name.delete(0, END)
    last_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

def update():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    record_id = delete_box.get()

    c.execute(""" UPDATE addresses SET
            first_name = :first,
            last_name = :last,
            address = :address,
            city = :city,
            state = :state,
            zipcode = :zipcode
              
            WHERE oid = :oid """,
            {

                'first': f_name_editor.get(),
                'last' : last_name_editor.get(),
                'address' : address_editor.get(),
                'city' : city_editor.get(),
                'state' : state_editor.get(),
                'zipcode': zipcode_editor.get(),
                'oid': record_id
            })

    conn.commit()
    conn.close()

    editor.destroy()

# Create query func
def query():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    #Query the database
    c.execute('SELECT *, oid FROM addresses')
    records = c.fetchall()
    # print(records)
    print_records = ''
    
    for record in records:
        print_records += str(record[0])+ ' ' + str(record[1]) +' '+ '\t'+ str(record[6]) + '\n '
    
    query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)


    conn.commit()
    conn.close() 

# Create Function to Delete A Record
    
def delete():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    # Delete record
    c.execute('DELETE FROM addresses WHERE oid= '+ delete_box.get())
    delete_box.delete(0, END)

    conn.commit()
    conn.close() 

# Create Function to Edit a Func
def edit():
    global editor
    editor = Tk()
    editor.title('Update a record')
    editor.iconbitmap('C:/Users/rodri/Desktop/In dev/VN-parser/tkinter use/Img examples/Bambúf.ico')
    editor.geometry('400x400')
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    # Create Global Varaibles for Text boxes
    global f_name_editor
    global last_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor

    record_id = delete_box.get()
    #Query the database
    c.execute('SELECT * FROM addresses WHERE oid=' + record_id)
    records = c.fetchall()

    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row = 0, column=1, padx=20, pady=(5, 0))

    last_name_editor = Entry(editor, width=30)
    last_name_editor.grid(row = 1, column=1, padx=20)

    address_editor = Entry(editor, width=30)
    address_editor.grid(row = 2, column=1, padx=20)

    city_editor = Entry(editor, width=30)
    city_editor.grid(row = 3, column=1, padx=20)

    state_editor = Entry(editor, width=30)
    state_editor.grid(row = 4, column=1, padx=20)

    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row = 5, column=1, padx=20)

    # Create Text box label
    f_name_label = Label(editor, text='First name')
    f_name_label.grid(row=0, column=0)

    last_name_label = Label(editor, text='Last name')
    last_name_label.grid(row=1, column=0, pady=(5, 0))

    adress_label = Label(editor, text='Adress')
    adress_label.grid(row=2, column=0)

    city_label = Label(editor, text='City')
    city_label.grid(row=3, column=0)

    state_label = Label(editor, text='State')
    state_label.grid(row=4, column=0)

    zipcode_label = Label(editor, text='Zipcode')
    zipcode_label.grid(row=5, column=0)


        # Loop thru results
    for record in records:
        f_name_editor.insert(0, record[0])
        last_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])

    # Create a button to save a edited record
    edit_btn = Button(editor, text='Save', command=update)
    edit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=135)
    



# Create text boxes
f_name = Entry(root, width=30)
f_name.grid(row = 0, column=1, padx=20, pady=(5, 0))

last_name = Entry(root, width=30)
last_name.grid(row = 1, column=1, padx=20)

address = Entry(root, width=30)
address.grid(row = 2, column=1, padx=20)

city = Entry(root, width=30)
city.grid(row = 3, column=1, padx=20)

state = Entry(root, width=30)
state.grid(row = 4, column=1, padx=20)

zipcode = Entry(root, width=30)
zipcode.grid(row = 5, column=1, padx=20)

delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1)

# Create Text box label
f_name_label = Label(root, text='First name')
f_name_label.grid(row=0, column=0)

last_name_label = Label(root, text='Last name')
last_name_label.grid(row=1, column=0, pady=(5, 0))

adress_label = Label(root, text='Adress')
adress_label.grid(row=2, column=0)

city_label = Label(root, text='City')
city_label.grid(row=3, column=0)

state_label = Label(root, text='State')
state_label.grid(row=4, column=0)

zipcode_label = Label(root, text='Zipcode')
zipcode_label.grid(row=5, column=0)

delete_box_label = Label(root, text='ID Number')
delete_box_label.grid(row=9, column= 0)

# Create Submit Button
submit_btn = Button(root, text='Add Record To Database', command = submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)



# Create a query button:
query_btn = Button(root, text='Show Records', command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=129)

# Create a delete button
delete_btn = Button(root, text='Select Record', command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=128)

edit_btn = Button(root, text='Edit Records', command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=135)




#Commit changes
conn.commit()

# Close Connection:
conn.close()

root.mainloop()