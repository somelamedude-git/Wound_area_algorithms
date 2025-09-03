import serial

ser = serial.Serial(
        port ='',
        baudrate = 9600,
        parity = serial.parity_NONE,
        stopbits = serial.STOPBITS_ONE,
        bytesize= serial.EIGHTBITS,
        timeout = 1
        )
