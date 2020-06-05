from controller import Robot
MAX_SPEED = 6.28 # максимальная скорость

robot = Robot()


timestep = int(robot.getBasicTimeStep())

leftMotor = robot.getMotor('left wheel motor')   # подключение левого 
rightMotor = robot.getMotor('right wheel motor') # и правого мотора

leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))

leftMotor.setVelocity(0.0)
rightMotor.setVelocity(0.0)

rightFor = robot.getDistanceSensor('ps0') # подключаем датчики расстояния:
rightFor.enable(timestep)                 # правый и передний правый,
right = robot.getDistanceSensor('ps2')    # а также активируем их
right.enable(timestep)
# счётчики для выполнения определённых действий
cntForward=0              # для движения вперёд после потери препятствия
cntLeft=0                 # для поворота налево
cntRight=0                # для поворота направо
cntForwardAfterRotation=0 # для движения вперёд после поворота
# коэффициенты скорости моторов
leftSpeed = 0.0      
rightSpeed = 0.0

while robot.step(timestep) != -1:
        
    rf = rightFor.getValue() # получение данных
    r = right.getValue()     # с сенсоров
    
    leftMotor.setVelocity(leftSpeed * MAX_SPEED)   # задание скорости
    rightMotor.setVelocity(rightSpeed * MAX_SPEED) # на моторах
# движение вперёд после потери препятствия для далнейшего поворота
    if cntForward > 0:
        leftSpeed = 0.4
        rightSpeed = 0.4
        cntForward-=1
        continue    
# выполнение поворота направо на 90 градусов
    if cntRight > 0:
        leftSpeed = 0.1
        rightSpeed = -0.1 
        cntRight-=1
        continue
# движение вперёд после поворота направо, чтобы найти стену справа
    if cntForwardAfterRotation > 0:
        leftSpeed = 0.2
        rightSpeed = 0.2 
        cntForwardAfterRotation-=1
        continue
# выполнение поворота налево на 90 градусов
    if cntLeft > 0: 
        cntLeft-=1
        continue
# проверка показаний датчиков для задания определённых действий
    # если справа и спереди есть препятствие, 
    # то задаём коэффициенты скорости 
    # и количество итераций для поворота налево
    if r > 100 and rf > 290:
        leftSpeed = -0.1
        rightSpeed = 0.1 
        cntLeft = 109
    # если справа стена и спереди ничего не мешает, то ехать прямо
    elif r > 100:
        leftSpeed = 0.4
        rightSpeed = 0.4
    # если робот потерял стену справа, 
    # то задаём количество итераций, 
    # чтобы выполнить небольшой проезд вперёд,
    # повернуть направо и ехать вперёд до 
    # обнаружение препятствия
    elif r < 100:
        cntForward = 24
        cntRight = 110
        cntForwardAfterRotation = 61
    
    pass

