from tkinter import *
from tkinter import ttk
import time

root = Tk()
root.title('Progress Bar')
root.geometry("640x400")

def run():
  progressBar['maximum'] = 100
  for i in range(101):
    time.sleep(0.05)
    i += 10
    progressBar["value"] = i
    progressBar.update()
    #progressBar["value"] = 0


buttonFrame = LabelFrame(text="Progress Bar")
buttonFrame.grid(column=0,row=0)

button1 = Button(buttonFrame, text="Run Progress Bar",command=run)
button1.grid(column = 0, row = 0)

progressBar = ttk.Progressbar(root, orient="horizontal", length=286,mode="determinate")
progressBar.grid(column = 0, row = 3, pady=10)

root.mainloop()
