from tkinter import *
from tkinter.ttk import *
import sys
import os
from tkinter.filedialog import askopenfilename

def caricaFile(button, fileType):
    file = askopenfilename(filetypes = fileType)

    if file != "":
        button['text'] = os.path.basename(file)
        button['state'] = "disabled"
        return
    button['text'] = "Errore! Riprovare"
    print(file + "\t" + button['text'])

def modifica(all_buttons, all_texts):
    print(valore.get())
    indice = 0
    for button in all_buttons:
        button['text'] = all_texts[indice]
        button['state'] = "enabled"
        indice += 1

try:
    nome_programma = "Programmino"
    buttons = []
    texts = []

    txt_pdf = "Selezione il file PDF"
    txt_xls = "Selezione il file EXCEL"
    txt_label = "Selezionare il PDF da leggere\n\n\nSelezionare l'Excel da leggere\n\n\nInserire il nome della cella"
    texts.extend([txt_pdf, txt_xls, txt_label])

    root = Tk()
    root.title(nome_programma)
    root.geometry('385x180')
    root.resizable(0, 0)

    valore = StringVar()

    label = Label(root, text= txt_label).pack(side= LEFT,anchor = NW, pady = 12, padx = 10)

    btn_pdf = Button(root, text = txt_pdf, command = lambda:caricaFile(btn_pdf, [(txt_pdf, "*.pdf")]))
    btn_xls = Button(root, text = txt_xls, command = lambda:caricaFile(btn_xls, [(txt_xls, "*.xls"), (txt_xls, "*.xlsx")]))
    field_txt = Entry(root, textvariable=valore, width = 15)
    buttons.extend([btn_pdf, btn_xls])

    btn_modifica = Button(root, text ='MODIFICA', command = lambda:modifica(buttons, texts))
    btn_conferma = Button(root, text ='CONFERMA', command = lambda:sys.exit(0))

    btn_pdf.pack(side = TOP, anchor = NW, pady = 10)
    btn_xls.pack(side = TOP, anchor = NW, pady = 10)
    field_txt.pack(anchor = NW, pady = 10)
    btn_modifica.place(relx=0.3, rely=0.83, anchor=CENTER)
    btn_conferma.place(relx=0.7, rely=0.83, anchor=CENTER)
   

    root.mainloop()
except Exception as errore:
    print(str(errore))