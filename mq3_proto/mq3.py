import serial
import RPi.GPIO as GPIO
import time

ser = serial.Serial(
        port ='',
        baudrate = 9600,
        parity = serial.parity_NONE,
        stopbits = serial.STOPBITS_ONE,
        bytesize= serial.EIGHTBITS,
        timeout = 1
        )

digital_output_pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(digital_output_pin, GPIO.IN)
try:
    while True:
        sensor_state = GPIO.input(digital_output_pin)
        if sensor_state == GPIO.HIGH:
            print('Awesome')
        else:
            print('Not so awesome')
        time.sleep(1)
except KeyboardInterrupt:
    print('Exiting')
finally:
    GPIO.cleanup()
