## ------- NEOPIXEL BLINK ------- ##
#   tested with tinkertanks moon   #

import board, time, neopixel
from adafruit_led_animation.animation.blink import Blink

TEAL = (255,50,0)

pixels = neopixel.NeoPixel(board.GP12, 56, brightness=0.5, auto_write=False)

blink = Blink(pixels, speed=0.2, color=TEAL)

while True:
    blink.animate()