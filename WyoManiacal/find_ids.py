from __future__ import print_function
import sys
from bibliopixel.drivers.serial_driver import DriverSerial

ports = DriverSerial.findSerialDevices(hardwareID="16C0:0483")
for p in ports:
    i = DriverSerial.getDeviceID(p)
    print('{} -> {}'.format(p, i))
