from pysimverse import Drone
import cv2
import time

# Initialize drone with desired speed
drone = Drone(speed=100)
drone.connect()
time.sleep(1)

# Start video stream and take off
drone.streamon()
drone.take_off()

rc_speed = 250

while True:
    frame, is_success = drone.get_frame()

    if is_success:
        cv2.imshow("Drone Feed", frame)

    # Standard OpenCV practice for cross-platform stability
    key = cv2.waitKey(1) & 0xFF

    # Reset all velocities to 0 (Hover mode) on every loop iteration
    left_right, forward_backward, up_down, yaw = 0, 0, 0, 0

    if key == ord("w"):
        forward_backward = rc_speed
    elif key == ord("s"):
        forward_backward = -rc_speed
    elif key == ord("a"):
        left_right = -rc_speed
    elif key == ord("d"):
        left_right = rc_speed
    elif key == ord("f"):
        up_down = rc_speed
    elif key == ord("c"):
        up_down = -rc_speed
    elif key == ord("q"):
        yaw = -1   # rotate left
    elif key == ord("e"):
        yaw = 1    # rotate right
    elif key == ord("l") or key == 27:  # 'l' or ESC key
        drone.land()
        time.sleep(2)
        break

    # Send control command
    drone.send_rc_control(left_right, forward_backward, up_down, yaw)

# Cleanup
drone.shutdown()
cv2.destroyAllWindows()
