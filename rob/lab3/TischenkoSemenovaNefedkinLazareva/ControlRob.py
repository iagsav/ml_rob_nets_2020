"""ControlRob controller."""

from controller import Robot

robot = Robot()

timestep = int(robot.getBasicTimeStep())

left_motor = robot.getMotor('wheel1')
right_motor = robot.getMotor('wheel2')

left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

ds_left = robot.getDistanceSensor('ds_left')
ds_left.enable(timestep)
ds_right = robot.getDistanceSensor('ds_right')
ds_right.enable(timestep)

k = 0
n = 1 

while robot.step(timestep) != -1:
    left = ds_left.getValue()
    right = ds_right.getValue()
    if k != 0:
        k -= 1
        continue
    left_speed = 1
    right_speed = 1
    
    if right > 50*n or left > 50*n:
        k = 10
        if right<left:
            left_speed = 1
            right_speed = -1
        else:
            left_speed = -1
            right_speed = 1
            
    left_motor.setVelocity(left_speed)
    right_motor.setVelocity(right_speed)
    pass