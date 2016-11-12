#!venv/bin/python3
import rpyc
conn = rpyc.classic.connect('192.168.0.14') # host name or IP address of the EV3
ev3 = conn.modules['ev3dev.ev3']      # import ev3dev.ev3 remotely
left_motor = ev3.LargeMotor('outB')
right_motor = ev3.LargeMotor('outC')

left_motor.run_timed(time_sp=1000, speed_sp=600)
right_motor.run_timed(time_sp=1000, speed_sp=500)
