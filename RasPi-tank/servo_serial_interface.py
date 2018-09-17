import serial
import time
ser = serial.Serial('/dev/ttyUSB0', 9600)
print("Opened port at 9600 baud")
i = True

while i:
    chars = str(input())
    chars = chars.title()
    if (chars == "Right"):
        ser.write('p'.encode())
    if (chars == "Left"):
        ser.write('x'.encode())
    if (chars == "Exit"):
        i = False

ser.close()
print("Closed port")
