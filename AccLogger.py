import serial
import time
import logging
import atexit
import re
# Loggt acc Values

logger = logging.getLogger('locationLogger')
hdlr = logging.FileHandler('/var/tmp/AccLogger.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.INFO)

counter = 0

time.sleep(1)
ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate=115200,
    timeout=0.5
)
time.sleep(1)
ser.write(b'\r')
ser.write(b'\r')
time.sleep(3)
ser.write(b'av\r')
time.sleep(0.5)
res2 = 'test'
numbers2 = [0,0,0]
while True:
	time.sleep(0.05)
	ser.write(b'\r')
	res = ser.readline()
	counter += 1
	if len(res)>10:
		if res!=res2:
			numbers = map(int, re.findall(r'-*\d+', res))
			logger.info('DIFF: \t%i; \t%i; \t%i;\n',numbers2[0]-numbers[0],numbers2[1]-numbers[1],numbers2[2]-numbers[2])
			res2 = res
			numbers2 = numbers



