from ev3dev.ev3 import *

d = UltrasonicSensor('in1')
scale = [
        130.8, 146.8, 164.8, 174.6, 195.0, 220.0, 246.9, 261.6,
        ]
for i in range(len(scale)):
    scale.append(scale[i]*2)

while True:
    k = d.distance_centimeters()
    if 392< k < 2550:
        t = scale[int((k-400)/100)] * 2
        Sound.tone([(t,300) ]).wait()
        #Sound.tone([(k,100,10) ]).wait()
    print(k)

