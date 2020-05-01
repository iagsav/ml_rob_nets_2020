"""SuperMaxController controller."""
import msvcrt
from controller import Robot, Motor, DistanceSensor, Keyboard

TIME_STEP = 64
MAX_SPEED = 6.28

robot = Robot()

#подключаем клавиатуру
keyboard = Keyboard()
keyboard.enable(TIME_STEP)


timestep = int(robot.getBasicTimeStep())


#тут я не использовал ультразвук, но почему бы не использовать его в будущем?
USSensorNames = [
    "left ultrasonic sensor", "front left ultrasonic sensor",
    "front ultrasonic sensor", "front right ultrasonic sensor",
    "right ultrasonic sensor"
]
IRSensorNames = [
    "rear left infrared sensor", "left infrared sensor",
    "front left infrared sensor", "front infrared sensor",
    "front right infrared sensor", "right infrared sensor",
    "rear right infrared sensor", "rear infrared sensor",
    "ground left infrared sensor", "ground front left infrared sensor",
    "ground front right infrared sensor", "ground right infrared sensor"
]
USSensors = []
IRSensors = []


#добавляем все ультразвуковые сенсоры в список
for sensor in USSensorNames:
    USSensors.append(robot.getDistanceSensor(sensor))
    
#добавляем все ИК сенсоры в список    
for sensor in IRSensorNames:
    IRSensors.append(robot.getDistanceSensor(sensor))

#включаем все сенсоры
for sensor in USSensors:
    sensor.enable(TIME_STEP)
for sensor in IRSensors:
    sensor.enable(TIME_STEP)



#включаем моторы, устанавливаем начальную скорость = 0
leftMotor = robot.getMotor('left wheel motor')
rightMotor = robot.getMotor('right wheel motor')
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))
leftMotor.setVelocity(0.0)
rightMotor.setVelocity(0.0)
leftSpeed  = 0
rightSpeed = 0

#тип управления изначально: 0 - авто, 1 - вручную
controlMode = 0
#================================================================#

while robot.step(timestep) != -1:
    
    key=keyboard.getKey()
    
    if key == Keyboard.CONTROL+Keyboard.UP:
        controlMode = 1
        leftSpeed  = 0
        rightSpeed = 0
    elif key == Keyboard.CONTROL+Keyboard.DOWN:
        controlMode = 0
        
        
    if controlMode == 0: #поведение при "автопилоте"
    
        #читаем показания датчиков
        USsensorValues = []
        for sensor in USSensors:
            USsensorValues.append(sensor.getValue())
        IRsensorValues = []
        for sensor in IRSensors:
            IRsensorValues.append(sensor.getValue())
        
        #устанавливаем начальную скорость колес в 50%  
        leftSpeed  = 0.5 * MAX_SPEED
        rightSpeed = 0.5 * MAX_SPEED
    
        #ищем препятствия
        right_obstacle = (IRsensorValues[3] > 300.0 
            or IRsensorValues[5] > 400 
            or IRsensorValues[4] > 250)
        left_obstacle = (IRsensorValues[3] > 300.0 
            or IRsensorValues[1] > 400 
            or IRsensorValues[2] > 250)
        
        if left_obstacle:
        # поворот направо
            leftSpeed  += 0.5 * MAX_SPEED
            rightSpeed -= 1.5 * MAX_SPEED
        elif right_obstacle:
        # поворот налево
            leftSpeed  -= 1.5 * MAX_SPEED
            rightSpeed += 0.5 * MAX_SPEED
    else: #поведение при дистанционном управлении 
          #(но в нашем случае с кдавиатуры)
        if key == ord('W'):
            leftSpeed  = 0.5 * MAX_SPEED
            rightSpeed = 0.5 * MAX_SPEED 
        elif key == ord ('A'):
            leftSpeed  = -1 * MAX_SPEED
            rightSpeed = 1 * MAX_SPEED            
        elif key == ord ('S'):
            leftSpeed  = -0.5 * MAX_SPEED
            rightSpeed = -0.5 * MAX_SPEED
        elif key == ord ('D'):
            leftSpeed  = 1 * MAX_SPEED
            rightSpeed = -1 * MAX_SPEED  

    #двигаем колесо соответственно условиям
    leftMotor.setVelocity(leftSpeed)
    rightMotor.setVelocity(rightSpeed)
    pass

#================================================================#
