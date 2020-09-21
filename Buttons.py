# importing tkinter and tkinter.ttk
# and all their functions and classes
from tkinter import *
from tkinter.ttk import *
import sys
import os

# importing askopenfile function
# from class filedialog
from tkinter.filedialog import askopenfilename

root = Tk()
root.geometry('300x200')

nome=""
bottoni = []
# This function will be used to open
# file in read mode and only Python files
# will be opened
def open_file():
    file = askopenfilename(filetypes = [('FILE PDF', '*.pdf')])
    nome = file
    btn['text'] = os.path.basename(nome)
    btn['state'] = "disabled"
    print(file)

btn = Button(root, text ='Nome PDF', command = lambda:open_file())
btn2 = Button(root, text ='Nome Excel', command = lambda:open_file())
btn3 = Button(root, text ='Nome cella', command = lambda:open_file())
btn4 = Button(root, text ='Esci', command = lambda:sys.exit())
btn.pack(side = TOP, pady = 10)
btn2.pack(side = TOP, pady = 10)
btn3.pack(side = TOP, pady = 10)
btn4.pack(side = TOP, pady = 10)

bottoni.append(btn)
bottoni.append(btn2)
bottoni.append(btn3)
bottoni.append(btn4)

for i in bottoni:
    print("ojm")
    mainloop()
