import serial
import time
ser = serial.Serial('COM3', 9600)
print("Opened port at 9600 baud")

ser.write('*'.encode())
time.sleep(.300)
ser.write('9'.encode())
time.sleep(.300)
ser.write('0'.encode())
time.sleep(.300)

ser.close()
print("Closed port")