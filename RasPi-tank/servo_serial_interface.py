import serial
import time
ser = serial.Serial('/dev/ttyUSB0', 9600)
print("Opened port at 9600 baud")
time.sleep(1.5) #Wait for arduino to reset
ser.write('*'.encode()) #identifier
ser.write('9'.encode()) #Value
ser.write('0'.encode()) #Value

ser.close()
print("Closed port")