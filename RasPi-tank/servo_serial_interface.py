import serial
import time
ser = serial.Serial('/dev/ttyUSB0', 9600)
print("Opened port at 9600 baud")
time.sleep(1.5) #Wait for arduino to reset
for i in range(10):
    inputString = str(input())
    ser.write('*'.encode()) #identifier
    ser.write(inputString[0].encode()) #Value
    ser.write(inputString[1].encode()) #Value

ser.close()
print("Closed port")
