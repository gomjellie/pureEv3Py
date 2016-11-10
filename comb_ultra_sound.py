
from ev3dev.ev3 import *

d = UltrasonicSensor('in1')
while True:
    k = d.distance_centimeters()
    if 392< k < 800:
        Sound.tone([(k,100,10) ]).wait()
    print(k)

