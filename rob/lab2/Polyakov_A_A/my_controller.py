from controller import Robot
SPEED = 1.0
robot = Robot()

timestep = int(robot.getBasicTimeStep())
left_motor = robot.getMotor('left wheel motor')
right_motor = robot.getMotor('right wheel motor')
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

ds_c = robot.getDistanceSensor('floor sensor')
ds_c.enable(timestep)

iter = 0
flag = True
while robot.step(timestep) != -1:
    iter += 1
    value = ds_c.getValue()
    if value < 101:
        left_motor.setVelocity(-SPEED)
        right_motor.setVelocity(SPEED)
        continue
    if iter % 10 == 0:
        if flag:
            SPEED += 0.1
        else:
            SPEED -= 0.2
        if SPEED == 10 or SPEED == 2:
            flag = not flag
    left_motor.setVelocity(-SPEED*1.25)
    right_motor.setVelocity(-SPEED)