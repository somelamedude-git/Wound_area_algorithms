import serial
import time

try:
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
except serial.SerialException:
    print("Arduino not connected")
answer = 0
count = 0
while True:
    if ser.in_waiting>0:
        line = ser.readline().decode('utf-8').strip()
        count = count + 1
        try:
            sensor_value = int(line)
            answer= answer+sensor_value
            if count == 100:
                answer = answer/float(count)
                print(answer)
                count = 0
                answer = 0
        except ValueError:
            print('Value error')
    time.sleep(1)
