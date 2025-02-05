## ----  Temperatursensor & Feuchtigkeit DHT-11 ---- ##
#           tested with tinkertanks frisbee           #

import digitalio
import neopixel
import time, adafruit_dht, board

WARM = (255, 0, 0)
GREEN = (0, 255, 0)
KALT = (0, 0, 255)
BLACK = (0,0,0)
WHITE = (255,150,120)

numpixels = 50
pixels = neopixel.NeoPixel(board.GP12, numpixels, brightness=1, auto_write=False)

dht = adafruit_dht.DHT11(board.GP8)

while True:
    try:
        print("Temperature:", dht.temperature, "  Humidity:", dht.humidity)        
    
    except RuntimeError as e:
        print("Reading from DHT failure: ", e.args)
    if dht.temperature>10:
        print("warm")
        pixels.fill(WARM)  #set all pixels to green
        pixels.show()

    else:
        print ("kalt")
        pixels.fill(KALT)  #set all pixels to green
        pixels.show()

    time.sleep(1)
    

# DHT11 PINOUT:

    ###
    ###
    ###
#   |||
#  D - + 	 