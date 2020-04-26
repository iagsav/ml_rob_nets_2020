from controller import Robot

robot = Robot()
MAXSPEED = 5

timestep = int(robot.getBasicTimeStep())
go_m = robot.getMotor('body pitch motor')
poworot = robot.getMotor('body yaw motor')
head_see = robot.getMotor('head yaw motor')
go_m.setPosition(float('inf'))
go_m.setVelocity(0.0)
poworot.setPosition(float('inf'))
poworot.setVelocity(0.0)
head_see.setPosition(float('inf'))
head_see.setVelocity(0.0)
acc = robot.getAccelerometer('body accelerometer')
acc.enable(64)
flag = True
i = 1
j = 0
while robot.step(timestep) != -1:
    r = acc.getValues()
    if j!= 0:
        j -= 1
        continue
    elif abs(r[0])>2:
        go_m.setVelocity(-i/4)
        poworot.setVelocity(-i*1.5)
        j = 10
    elif flag:
        go_m.setVelocity(2.0)
        poworot.setVelocity(0.0)
        head_see.setVelocity(2.0)
    else:
        go_m.setVelocity(-2.0)
        poworot.setVelocity(8.0)
        head_see.setVelocity(0.0)
    flag = True
    if i%3 == 0:
        flag = False
        i = 0
    i += 1
