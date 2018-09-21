import serial
import time
ser = serial.Serial('COM3', 9600)
print("Opened port at 9600 baud")
time.sleep(1.5) #Wait for arduino to reset
ser.write('*'.encode())
ser.write('9'.encode())
ser.write('0'.encode())

ser.close()
print("Closed port")