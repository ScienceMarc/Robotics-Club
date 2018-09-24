from tkinter import *
import tkinter
import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 9600)
print("Opened port at 9600 baud")
time.sleep(1.5) #Wait for arduino to reset

top = tkinter.Tk()
top.geometry("256x256")

def Aa():
    ser.write('a'.encode()) #identifier
    ser.write('9'.encode()) #Value
    ser.write('0'.encode()) #Value
def All():
    ser.write('*'.encode()) #identifier
    ser.write('9'.encode()) #Value
    ser.write('0'.encode()) #Value    


butt = Button(top, text = "a", command = Aa)
butt2 = Button(top, text = "*", command = All)
butt.place(x = 100,y = 0)
butt2.place(x = 100,y = 40)

top.mainloop()

