from ev3dev.ev3 import *

ts = TouchSensor('in1')
while True:
    Leds.set_color(Leds.LEFT, (Leds.GREEN, Leds.RED)[ts.value()])
