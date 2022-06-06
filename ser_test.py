import serial
from time import sleep

ser = serial.Serial()
ser.port = 'COM40'
# ser.port = 'COM3'
# ser.port = 'COM25'
# ser.port = 'COM5'

ser.open()
ser.write(b'*IDN?\n')
sleep(0.1)
print (ser.read(ser.inWaiting()))

# ser.close()

sleep(0.051)
# ser.write(b'SOURce1:FUNCtion:Amplitude 10\n')
# ser.write(b'SOURce1:FUNCtion:Offset 0\n')
# ser.write(b'SOURce2:FUNCtion:Amplitude 4\n')
# ser.write(b'SOURce2:FUNCtion:Offset 0\n')

ser.write(b'SOURce1:VOLTage:LEVel 2.2\n')		
			
			

# ser.write(b'TRIGC:STAT run\n')
sleep(0.051)
print (ser.read(ser.inWaiting()))

sleep(0.5)

ser.close()