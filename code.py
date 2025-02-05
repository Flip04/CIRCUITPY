import board
import pulseio
import time
import pwmio
import digitalio
import adafruit_irremote
from adafruit_motor import motor


# ------------------------------------- IR Receiver -------------------------------------
ir_receiver = pulseio.PulseIn(board.GP8, maxlen=100, idle_state=True)
decoder = adafruit_irremote.GenericDecode()

# ------------------------------------- Motor -------------------------------------------
M1_A = board.GP0
M1_B = board.GP1
motor1 = motor.DCMotor(pwmio.PWMOut(M1_A, frequency=500), pwmio.PWMOut(M1_B, frequency=500))

# ------------------------------------- Speaker? ----------------------------------------

# ------------------------------------- LEDs --------------------------------------------

# pins
leds = [
    digitalio.DigitalInOut(board.GP26),
    digitalio.DigitalInOut(board.GP27),
    digitalio.DigitalInOut(board.GP28)]

# set digital pin to out
def hpLedsInit():
    for i in range(3):
        leds[i].direction = digitalio.Direction.OUTPUT

# all leds should start on (3hp)
def hpLedsReset():
    for i in range(3):
        leds[i].value = True

        
# ------------------------------------- Health ------------------------------------------

my_health = 3
def decrease_health():
    global my_health
    my_health -= 1
    leds[my_health].value = False
    # play sound?
    motor1.throttle = 1
    time.sleep(0.2)
    motor1.throttle = 0
    time.sleep(0.2)
    motor1.throttle = 1
    time.sleep(0.2)
    motor1.throttle = 0
    time.sleep(0.2)
    motor1.throttle = 1
    time.sleep(0.2)
    motor1.throttle = 0



# ------------------------------------- main loop ---------------------------------------
def run():
    # get ir signal
    pulses = decoder.read_pulses(ir_receiver, blocking=True)
    try:
        decoded = decoder.decode_bits(pulses)
        print("Empfangenes Signal:", decoded)
        decrease_health()
    except adafruit_irremote.IRNECRepeatException:
        print("(Wiederholungssignal)")
    except adafruit_irremote.IRDecodeException:
        print("Fehler beim Dekodieren")



# public static void main(string[] args)
hpLedsInit()
hpLedsReset()
while True:
    run()
