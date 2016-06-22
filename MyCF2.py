#sudo PYTHONPATH
#from example/ramp.py

import cflib.crtp, cflib.crazyflie, time

def motors():
    c.commander.send_setpoint(0, 0, 0, 0)
    time.sleep(0.1)
    c.commander.send_setpoint(1.5, 0, 0, 10000)
    time.sleep(1000)
    c.commander.send_setpoint(0, 0, 0, 0)

cflib.crtp.init_drivers()
c=cflib.crazyflie.Crazyflie()
c.open_link("radio://0/80/250K")

motors()



