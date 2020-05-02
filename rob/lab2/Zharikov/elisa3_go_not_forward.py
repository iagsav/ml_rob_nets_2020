from controller import Robot
MAX_SPEED = 3
robot = Robot()

timestep = int(robot.getBasicTimeStep())

leftMotor = robot.getMotor("left wheel motor")
rightMotor = robot.getMotor("right wheel motor")

leftMotor.setVelocity(2*MAX_SPEED)
rightMotor.setVelocity(3*MAX_SPEED)

leftMotor.setPosition(float("inf"))
rightMotor.setPosition(float("inf"))





while robot.step(timestep) != -1:

    pass

