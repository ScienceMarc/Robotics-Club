import tkinter
from tkinter import *
tab = tkinter.Tk()
tab.geometry("100x100")

press = Button(text = "press me",command = print("why?"))
press.place(x = 10, y = 10)
tab.mainloop()
