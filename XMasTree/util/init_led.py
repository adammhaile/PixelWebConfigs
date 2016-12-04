from __future__ import print_function
from bibliopixel import LEDStrip
from bibliopixel import colors
from bibliopixel.drivers.visualizer import DriverVisualizer

num_pixels = 350


def setup():
    global led
    driver = DriverVisualizer(num=num_pixels, stayTop=True)
    return LEDStrip(driver, threadedUpdate=True, masterBrightness=255)
