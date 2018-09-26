from tkinter import *
import tkinter
import serial
import time

ser = serial.Serial('COM5', 9600)
print("Opened port at 9600 baud")
time.sleep(1.5) #Wait for arduino to reset

root = tkinter.Tk()
root.geometry("256x256")

def A(inputString):
    inputString = str(inputString)
    if len(inputString) < 2:
        inputString += "0"
        inputString = inputString[::-1]
    ##print(inputString)
    ser.write('a'.encode()) #identifier
    ser.write(inputString[0].encode()) #Value
    ser.write(inputString[1].encode()) #Value

def B(inputString):
    inputString = str(inputString)
    if len(inputString) < 2:
        inputString += "0"
        inputString = inputString[::-1]
    ##print(inputString)
    ser.write('b'.encode()) #identifier
    ser.write(inputString[0].encode()) #Value
    ser.write(inputString[1].encode()) #Value

def C(inputString):
    inputString = str(inputString)
    if len(inputString) < 2:
        inputString += "0"
        inputString = inputString[::-1]
    ##print(inputString)
    ser.write('c'.encode()) #identifier
    ser.write(inputString[0].encode()) #Value
    ser.write(inputString[1].encode()) #Value

def D(inputString):
    inputString = str(inputString)
    if len(inputString) < 2:
        inputString += "0"
        inputString = inputString[::-1]
    ##print(inputString)
    ser.write('d'.encode()) #identifier
    ser.write(inputString[0].encode()) #Value
    ser.write(inputString[1].encode()) #Value

def E(inputString):
    inputString = str(inputString)
    if len(inputString) < 2:
        inputString += "0"
        inputString = inputString[::-1]
    ##print(inputString)
    ser.write('e'.encode()) #identifier
    ser.write(inputString[0].encode()) #Value
    ser.write(inputString[1].encode()) #Value
def F(inputString):
    inputString = str(inputString)
    if len(inputString) < 2:
        inputString += "0"
        inputString = inputString[::-1]
    ##print(inputString)
    ser.write('f'.encode()) #identifier
    ser.write(inputString[0].encode()) #Value
    ser.write(inputString[1].encode()) #Value

def All(inputString):
    inputString = str(inputString)
    if len(inputString) < 2:
        inputString += "0"
        inputString = inputString[::-1]
    ##print(inputString)
    ser.write('*'.encode()) #identifier
    ser.write(inputString[0].encode()) #Value
    ser.write(inputString[1].encode()) #Value

varA = tkinter.IntVar()
varB = tkinter.IntVar()
varC = tkinter.IntVar()
varD = tkinter.IntVar()
varE = tkinter.IntVar()
varF = tkinter.IntVar()
varAll = tkinter.IntVar()

scale = Scale(root, variable = varA, from_=0, to=90, orient=HORIZONTAL)
scale.pack()
scale = Scale(root, variable = varB, from_=0, to=90, orient=HORIZONTAL)
scale.pack()
scale = Scale(root, variable = varC, from_=0, to=90, orient=HORIZONTAL)
scale.pack()
scale = Scale(root, variable = varD, from_=0, to=90, orient=HORIZONTAL)
scale.pack()
scale = Scale(root, variable = varE, from_=0, to=90, orient=HORIZONTAL)
scale.pack()
scale = Scale(root, variable = varF, from_=0, to=90, orient=HORIZONTAL)
scale.pack()

while True:
    root.update_idletasks()
    root.update()
    A(varA.get())
    B(varB.get())
    C(varC.get())
    D(varD.get())
    E(varE.get())
    F(varF.get())
    ##All(varAll.get())
#root.mainloop()

