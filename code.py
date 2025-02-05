import board
import pulseio
import time
import pwmio
import digitalio
import adafruit_irremote
from adafruit_motor import motor


# IR Receiver an den entsprechenden Pin anschließen (z. B. D6)
ir_receiver = pulseio.PulseIn(board.GP27, maxlen=100, idle_state=True)
decoder = adafruit_irremote.GenericDecode()

# OUTPUT 1
M1_A = board.GP0
M1_B = board.GP1
motor1 = motor.DCMotor(pwmio.PWMOut(M1_A, frequency=500), pwmio.PWMOut(M1_B, frequency=500))


print("Warte auf IR-Signal...")

while True:
    pulses = decoder.read_pulses(ir_receiver, blocking=True)
    try:
        decoded = decoder.decode_bits(pulses)
        print("Empfangenes Signal:", decoded)
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
    except adafruit_irremote.IRNECRepeatException:
        print("(Wiederholungssignal)")
    except adafruit_irremote.IRDecodeException:
        print("Fehler beim Dekodieren")
