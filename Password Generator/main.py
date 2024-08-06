import tkinter as tk
from tkinter import messagebox as mbox
from passwordGenerator import generatePassword as gp

class Window:

    def __init__(root):
        root.root = tk.Tk()
        root.root.geometry("")
        root.root.title("Password Generator GUI")
        root.__create_entries()

    def __create_entries(root):

        variable = tk.StringVar()
        menu = tk.OptionMenu(root.root,variable,"True","False")

        root.entries_to_create = {"Length":tk.Entry(root.root,width=2),"No of Uppercase Letters":tk.Entry(root.root,width=2),"No of Lowercase Letters":tk.Entry(root.root,width=2),"No of Special Charachters":tk.Entry(root.root,width=2),"No of Numeric Digits":tk.Entry(root.root,width=2),"Duplicates Allowed":menu}
        row = 0 
        for entry in root.entries_to_create.keys():
            label = tk.Label(root.root, text=entry)
            label.grid(row=row, column=0, padx=10, pady=5, sticky='e') 
            root.entries_to_create[entry].grid(row=row, column=1, padx=10, pady=5, sticky='w')  
            row += 1  
        root.entries_to_create['Duplicates Allowed'] = tk.BooleanVar()

        generate_button = tk.Button(root.root, text="Generate", width=20, height=2,command=root.__generate_password)  
        generate_button.grid(row=0, column=2, rowspan=row, padx=20, pady=5) 
             
    def __generate_password(root):
        length,uCase,lCase,specialCase,numbers,duplicates = (int(argument.get()) if argument.get() else 0 for argument in root.entries_to_create.values())
        password = gp(lenght=length,uppercase=uCase,lowercase=lCase,special_chars=specialCase,nums=numbers,duplicates=duplicates)
        _ = tk.Label(root.root,text=f"Password:{password}",font= ("Courier",30)).grid(
            row=7,columns=3, columnspan=3,padx=20,pady=20
        )
        root.root.geometry("")

    def create_window(root):
        root.root.mainloop()

test = Window()
test.create_window()