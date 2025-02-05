##    ------  NEOPIXEL  ------    ##
#   tested with tinkertanks moon   #

import time
import board
import digitalio
import neopixel

#color definitions
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0,0,0)
WHITE = (255,150,120)

numpixels = 60
pixels = neopixel.NeoPixel(board.GP13, numpixels, brightness=1, auto_write=False) #z.B. 1 Pixel an pin GP14 (der Mond)

while True:


    
    pixels[2] = WHITE
    pixels.show()
    time.sleep(0.5)
    pixels[2] = BLACK
    pixels.show()
    time.sleep(0.5)

