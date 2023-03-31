import time
import serial

ser=serial.Serial('/dev/ttyS0',9600)
ser.timeout = 5

while True :
    data = input('enter data : ')
    ser.write(data.encode())
    time.sleep(0.1)