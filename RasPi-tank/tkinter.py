from tkinter import *
import tkinter
import serial
import time

ser = serial.Serial('COM3', 115200)
print("Opened port at 115200 baud")
time.sleep(1.5) #Wait for arduino to reset

root = tkinter.Tk()
root.geometry("256x256")
##making the object
class servo:
    def __init__(self, designation, inputString):
        self.designation = designation
        self.inputString = inputString
    def motor(self):
        self.inputString = str(self.inputString)
        if len(self.inputString) < 2:
            self.inputString += "0"
            self.inputString = self.inputString[::-1]
        ##print(inputString)
        ser.write(self.designation.encode()) #identifier
        ser.write(self.inputString[0].encode()) #Value
        ser.write(self.inputString[1].encode()) #Value
        
        

varA = tkinter.IntVar()
varB = tkinter.IntVar()
varC = tkinter.IntVar()
varD = tkinter.IntVar()
varE = tkinter.IntVar()
varF = tkinter.IntVar()

variables = [varA,varB,varC,varD,varE,varF]

#Tkinter stuff
scale = Scale(root, variable = variables[0], from_=0, to=90, orient=HORIZONTAL)
scale.pack()
scale = Scale(root, variable = variables[1], from_=0, to=90, orient=HORIZONTAL)
scale.pack()
scale = Scale(root, variable = variables[2], from_=0, to=90, orient=HORIZONTAL)
scale.pack()
scale = Scale(root, variable = variables[3], from_=0, to=90, orient=HORIZONTAL)
scale.pack()
scale = Scale(root, variable = variables[4], from_=0, to=90, orient=HORIZONTAL)
scale.pack()
scale = Scale(root, variable = variables[5], from_=0, to=90, orient=HORIZONTAL)
scale.pack()

serv = servo("A", 0)

listOfServos = "abcdef"

while True:
    for i in range(5):
        serv.designation = listOfServos[i]
        print(serv.designation)
        serv.inputString = variables[i].get()
        print(serv.inputString)
        serv.motor()
        root.update_idletasks()
        root.update()

        
    
    ##All(varAll.get())
#root.mainloop()

