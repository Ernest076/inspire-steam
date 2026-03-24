# Import RoboDK API
from robodk import robolink    # RoboDK API
from robodk import robomath    # Math toolbox

# Connect to RoboDK
RDK = robolink.Robolink()

# Get the robot (assumes one is loaded in RoboDK)
robot = RDK.Item('', robolink.ITEM_TYPE_ROBOT)

# Define four target positions (XYZ in mm, orientation as identity)
# You can adjust these coordinates to suit your setup
target_positions = [
    robomath.transl(200, 0, 300),    # Target 1
    robomath.transl(300, 100, 300),  # Target 2
    robomath.transl(400, 0, 300),    # Target 3
    robomath.transl(300, -100, 300)  # Target 4
]

# Create targets in RoboDK station
targets = []
for i, pos in enumerate(target_positions, start=1):
    target = RDK.AddTarget(f"Target {i}", robot)
    target.setPose(pos)
    targets.append(target)

# Move the robot through the targets
for target in targets:
    robot.MoveJ(target)   # Joint move to target
