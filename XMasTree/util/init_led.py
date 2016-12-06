from __future__ import print_function
from bibliopixel import LEDStrip
from bibliopixel import colors
# from bibliopixel.drivers.visualizer import DriverVisualizer
from bibliopixel.drivers.serial_driver import DriverSerial, LEDTYPE, ChannelOrder

num_pixels = 300


def setup():
    global led
    # driver = DriverVisualizer(num=num_pixels, stayTop=True)
    driver = DriverSerial(LEDTYPE.NEOPIXEL, 300, c_order=ChannelOrder.RGB, gamma=None)
    return LEDStrip(driver, threadedUpdate=True, masterBrightness=255)
