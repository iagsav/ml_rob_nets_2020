"""AndryControl"""

from controller import Robot

robot = Robot()

leftMotor = robot.getMotor('left wheel')

rightMotor = robot.getMotor('right wheel')

leftMotor.setPosition(float('inf'))

rightMotor.setPosition(float('inf'))

leftMotor.setVelocity(0.5)

rightMotor.setVelocity(0.3)

pass