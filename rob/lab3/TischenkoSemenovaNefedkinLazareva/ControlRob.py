"""ControlRob controller.""" 

from controller import Robot 

robot = Robot()

timestep = int(robot.getBasicTimeStep())

left_motor = robot.getMotor('wheel1') #Объявление левого мотора
right_motor = robot.getMotor('wheel2')#Объявление правого мотора

left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

ds_left = robot.getDistanceSensor('ds_left')#Объявление левого ds_left.enable(timestep)			       #датчика
ds_right = robot.getDistanceSensor('ds_right')#Объявлеие правого ds_right.enable(timestep) 				   #датчика

k = 0 #Счетчик времени для объезда препятствий
n = 1 #коэффициент расстояния до препяствий для объезда

while robot.step(timestep) != -1: #Основной цикл контроллера
    left = ds_left.getValue()	  #Присваеваем переменным данные 
    right = ds_right.getValue()	  #с датчиков
    if k != 0:				  #Условие для счетчика времени
        k -= 1				  #Пока не 0 осуществляется 	
        continu   			  #"объезд"
    left_speed = 1			  #Начальная скорость для левого 
    right_speed = 1			  #и правого мотора
    
    if right > 50*n or left > 50*n: #Условие "попадания" в 
        k = 10				    #препятствие
        if right<left:		    #Условие для определения 
            left_speed = 1		    #лучшего способа объезда
            right_speed = -1	    #и присваивание 
        else:				    #соответствующих скоростей
            left_speed = -1		    #левому и
            right_speed = 1 	    #правому моторам
            
    left_motor.setVelocity(left_speed)  #Установка скорости
    right_motor.setVelocity(right_speed)
    pass