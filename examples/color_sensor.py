from ev3dev.ev3 import *

cs = ColorSensor('in4')
while True:
    v = cs.ambient_light_intensity()
    print(v)

