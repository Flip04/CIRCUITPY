import board
import pulseio
import time
import pwmio
import digitalio
import adafruit_irremote
from adafruit_motor import motor
import audiomp3, audiopwmio


# ------------------------------------- IR Receiver -------------------------------------
ir_receiver = pulseio.PulseIn(board.GP8, maxlen=100, idle_state=True)
decoder = adafruit_irremote.GenericDecode()

# ------------------------------------- Motor -------------------------------------------
M1_A = board.GP0
M1_B = board.GP1
motor1 = motor.DCMotor(pwmio.PWMOut(M1_A, frequency=500), pwmio.PWMOut(M1_B, frequency=500))

# ------------------------------------- Speaker? ----------------------------------------

audio = audiopwmio.PWMAudioOut(board.GP3) #Lautsprecher an Pin GP4 (D4)
kill_mp3 = audiomp3.MP3Decoder(open("04_sound/kill_loud.mp3", "rb"))
ace_mp3 = audiomp3.MP3Decoder(open("04_sound/ace_loud.mp3", "rb"))

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

# turn on all leds
def hpLedsOn():
    for i in range(3):
        leds[i].value = True
        
# turn off all leds
def hpLedsOff():
    for i in range(3):
        leds[i].value = False

        
# ------------------------------------- Health ------------------------------------------

my_health = 3
def decrease_health():
    global my_health
    if my_health == 0:
        # well you're dead
        return
    else:
        my_health -= 1
        leds[my_health].value = False
        # play sound
        if my_health == 0:
            audio.play(ace_mp3)
        else:
            audio.play(kill_mp3)
        throttle_interval = 0.05
        motor1.throttle = 1
        time.sleep(throttle_interval*2)
        motor1.throttle = 0
        time.sleep(throttle_interval)
        motor1.throttle = 1
        time.sleep(throttle_interval*2)
        motor1.throttle = 0
        time.sleep(throttle_interval)
        motor1.throttle = 1
        time.sleep(throttle_interval*2)
        motor1.throttle = 0
        if my_health == 0:
            reset()


# ------------------------------------- reset -------------------------------------------

def reset():
    time.sleep(2)
    blink_times = 6
    for i in range(blink_times):
        delay = 0.5
        hpLedsOn()
        time.sleep(delay)
        hpLedsOff()
        time.sleep(delay)
    for i in range(3):
        leds[i].value = True
        time.sleep(0.187)
    global my_health
    my_health = 3



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
hpLedsOn()
while True:
    run()
