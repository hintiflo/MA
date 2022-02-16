import serial
from time import sleep

ser = serial.Serial()
ser.port = 'COM31'

ser.open()
ser.write(b'*IDN?\n')
sleep(0.1)
print (ser.read(ser.inWaiting()))

ser.write(b'SOUR1:MODE free			\n')
sleep(0.05)
ser.write(b'SOUR1:VOLT:LEV -2.95	\n')
sleep(0.05)
ser.write(b'TRIGB:pre 64\n')
sleep(0.05)
ser.write(b'TRIGB:tcou 36500\n')
sleep(0.05)
ser.write(b'TRIGA:cou 1000\n')
sleep(0.05)
ser.write(b'TRIGgerB:Mode CONTinuous\n')
sleep(0.5)
ser.write(b'TRIGgerB:STATe RUN		\n')

sleep(0.05)
print (ser.read(ser.inWaiting()))

sleep(0.5)

ser.close()