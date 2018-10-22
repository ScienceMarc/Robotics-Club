from tkinter import *
import tkinter
import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 115200)
print("Opened port at 115200 baud")
time.sleep(1.5) #Wait for arduino to reset

root = tkinter.Tk()
root.geometry("256x256")
#Declairing the servo class with a motor method
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
        
variables = [tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar()]

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
    for i in range(6):
        serv.designation = listOfServos[i]
        print(serv.designation)
        serv.inputString = variables[i].get()
        print(serv.inputString)
        serv.motor()
        root.update_idletasks()
        root.update()

        
    
    ##All(varAll.get())
#root.mainloop()

