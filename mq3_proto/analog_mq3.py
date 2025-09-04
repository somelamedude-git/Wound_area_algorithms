import serial
import time

try:
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
except serial.SerialException:
    print("Arduino not connected")

while True:
    if ser.in_waiting>0:
        line = ser.readline().decode('utf-8').strip()
        try:
            sensor_value = int(line)
            print(sensor_value)
        except ValueError:
            print('Value error')
