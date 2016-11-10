from ev3dev.ev3 import *

d = UltrasonicSensor('in1')
while True:
    k = d.distance_centimeters()
    print(k)

