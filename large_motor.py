from ev3dev.ev3 import *

d = LargeMotor('outD')
d.run_timed(time_sp=3000, speed_sp=500)
