from pysimverse import Drone

import time

drone = Drone()
drone.connect()

drone.take_off(5)
# distance in cm
drone.set_speed(1100)
drone.move_forward(300)

drone.move_right(520)
drone.land()
