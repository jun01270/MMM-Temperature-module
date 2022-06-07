#!/usr/bin/env python

import time
from bmp280 import BMP280

try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus

print("""temperature-and-pressure.py - Displays the temperature and pressure.

Press Ctrl+C to exit!

""")

# Initialise the BMP280
bus = SMBus(1)
bmp280 = BMP280(i2c_dev=bus)

while True:
    temp = bmp280.get_temperature()
    print('{:05.2f}'.format(temp))
    f = open("/dev/shm/temp.txt", "w")
    f.write(str(round(temp,1)))
    f.close()
    time.sleep(5)
