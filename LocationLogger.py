import serial
import time
import logging
import atexit

@atexit.register
def goodbye():
    ser.write(b'lep\r')

# lep sendet Position (aufgr. des C-Moduls) bei jedem DWM Event. Wird abgebrochen, laeuft lep noch weiter. Beim naechsten Skriptaufruf stoppt das Skript das bereits laufende lep, anstatt das "eigene" zu starten. Loesung: Wird das Skript abgebrochen, wird das laufende "lep" Kommando beendet.

logger = logging.getLogger('locationLogger')
hdlr = logging.FileHandler('/var/tmp/locationLogger.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.INFO)

counter = 0
print('Test')
time.sleep(1)
ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate=115200,
    timeout=0.1
)
time.sleep(1)
ser.write(b'\r')
ser.write(b'\r')
time.sleep(3)
ser.write(b'lep\r')
time.sleep(0.5)
while True:
	res = ser.readline()
	counter += 1
	if len(res)>12:
		if "dwm" not in res: 
			logger.info('%i: %s',counter,res)


