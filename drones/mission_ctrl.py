# drone_keyboard.py
import time
import keyboard   # pip install keyboard
from pysimverse  import simulators
from pysimverse import Drone

def main():
    # Initialize simulation
    sim = simulators()
    drone = Drone(sim, name="MyDrone")

    sim.start()
    drone.take_off()
    print("Drone is airborne. Use W/A/S/D to move, Q to quit.")

    speed = 5.0  # default speed

    try:
        while True:
            if keyboard.is_pressed("w"):
                drone.forward(speed=speed, duration=1)
                print("Moving forward")
            elif keyboard.is_pressed("s"):
                drone.backward(speed=speed, duration=1)
                print("Moving backward")
            elif keyboard.is_pressed("a"):
                drone.left(speed=speed, duration=1)
                print("Moving left")
            elif keyboard.is_pressed("d"):
                drone.right(speed=speed, duration=1)
                print("Moving right")
            elif keyboard.is_pressed("up"):
                speed += 1
                print(f"Speed increased to {speed}")
                time.sleep(0.3)
            elif keyboard.is_pressed("down"):
                speed = max(1, speed - 1)
                print(f"Speed decreased to {speed}")
                time.sleep(0.3)
            elif keyboard.is_pressed("q"):
                print("Landing and exiting...")
                break

            time.sleep(0.1)

    finally:
        drone.land()
        sim.stop()

if __name__ == "__main__":
    main()


