"""wheels1 controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

leftWheel = robot.getMotor('FrontLeftWheel')
rightWheel = robot.getMotor('FrontRightWheel')

leftArmMotor = robot.getMotor('FrontLeftArm')
rightArmMotor = robot.getMotor('FrontRightArm')

leftWheel.setPosition(float('inf'))
rightWheel.setPosition(float('inf'))

leftWheel.setVelocity(0.6)
rightWheel.setVelocity(0.6)

leftArmMotor.setPosition(float(0.3))
rightArmMotor.setPosition(float(0.3))

leftArmMotor.setVelocity(2)
rightArmMotor.setVelocity(2)

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getMotor('motorname')
#  ds = robot.getDistanceSensor('dsname')
#  ds.enable(timestep)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    pass

# Enter here exit cleanup code.
