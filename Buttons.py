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
root.title("Programmino")
root.geometry('320x180')
root.resizable(0, 0)
label = Label(root, text="Selezionare il PDF da leggere\n\n\nSelezionare l'Excel da leggere\n\n\nInserire il nome della cella").pack(side= LEFT,anchor = NW, pady = 12, padx = 10)


valore = StringVar()
nome=""
bottoni = []
# This function will be used to open
# file in read mode and only Python files
# will be opened
def open_file(i):
    file = askopenfilename(filetypes = [('FILE PDF', '*.pdf')])
    nome = file
    btn = bottoni[i]
    btn['text'] = os.path.basename(nome)
    btn['state'] = "disabled"
    print(file)

def submit():
    print(valore.get())
    btn = bottoni[0]
    btn['text'] = 'Seleziona file PDF'
    btn['state'] = "enabled"

bottoni.append(Button(root, text ='Seleziona file PDF', command = lambda:open_file(0)))
bottoni.append(Button(root, text ='Seleziona file Excel', command = lambda:open_file(1)))
bottoni.append(Button(root, text ='MODIFICA', command = lambda:submit()))
bottoni.append(Button(root, text ='CONFERMA', command = lambda:sys.exit()))

bottoni[0].pack(side = TOP, anchor = NW, pady = 10)
bottoni[1].pack(side = TOP, anchor = NW, pady = 10)
bottoni[2].place(relx=0.3, rely=0.83, anchor=CENTER)
bottoni[3].place(relx=0.7, rely=0.83, anchor=CENTER)
testo = Entry(root, textvariable=valore, width = 20).pack(anchor = NW, pady = 10)

root.mainloop()
