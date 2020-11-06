from tkinter import *
from tkinter import ttk
import time

def creaProgresso():
    """Questa funzione contiene banalmente il codice per creare una barra del progresso;
    può essere inserita in un qualsiasi root.loop fatto con Tk()"""

    progressBar = ttk.Progressbar(root, orient="horizontal", length=100, mode="determinate")
    progressBar.pack(anchor = NW, pady = 10, padx = 10)

    #Maximum imposta quanto la barra può riempirsi
    progressBar['maximum'] = 100

    #Queste due righe permettono di far progredire la barra, time.sleep è opzionale
    progressBar["value"] = 10
    progressBar.update()
    #time.sleep(10)

    #Il return è importante, così è più semplice fare l'update della barra fuori dal codice del frame grafico
    return progressBar

def main():
    root = Tk()
    root.title('Progress Bar')
    root.geometry("150x50")

    creaProgresso()

    root.mainloop()
