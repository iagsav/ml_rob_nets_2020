from controller import Robot

TIME_STEP = 164
robot = Robot()
ds = []
dsNames = ['back_sensor', 'front_center_sensor', 'front_left_sensor','front_right_sensor','side_left_sensor','side_right_sensor']
for i in range(6):
    ds.append(robot.getDistanceSensor(dsNames[i]))
    ds[i].enable(TIME_STEP)
    
    
wheels = []
wheelsNames = ['left_front_wheel', 'right_front_wheel', 'left_rear_wheel', 'right_rear_wheel']
for i in range(4):
    wheels.append(robot.getMotor(wheelsNames[i]))
       
wheels[0].setPosition(float('inf'))
wheels[0].setVelocity(0.0)
wheels[1].setPosition(float('inf'))
wheels[1].setVelocity(0.0)
wheels[2].setPosition(float('inf'))
wheels[2].setVelocity(0.0)
wheels[3].setPosition(float('inf'))
wheels[3].setVelocity(0.0)  
    
avoidObstacleCounter = 0
while robot.step(TIME_STEP) != -1:
    leftSpeed = 10.0
    rightSpeed = 10.0
    if avoidObstacleCounter > 0:
        avoidObstacleCounter -= 1
        leftSpeed = 10.0
        rightSpeed = -1.0
    else: 
        for i in range(6):
            if ds[i].getValue() < 950.0:
                avoidObstacleCounter = 100
    wheels[0].setVelocity(leftSpeed)
    wheels[1].setVelocity(rightSpeed)
    wheels[2].setVelocity(leftSpeed)
    wheels[3].setVelocity(rightSpeed)