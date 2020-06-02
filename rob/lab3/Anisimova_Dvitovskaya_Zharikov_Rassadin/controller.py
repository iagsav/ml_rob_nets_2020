"""Sample Webots controller for highway driving benchmark."""

from vehicle import Driver

# name of the available distance sensors
sensorsNames = [
    'front',
    'front right 0',
    'front right 1',
    'front right 2',
    'front left 0',
    'front left 1',
    'front left 2',
    'rear',
    'rear left',
    'rear right',
    'right',
    'left']
sensors = {}

maxSpeed = 50
maxAngle = 0.1
driver = Driver()
driver.setSteeringAngle(0.0)  # go straight

# get and enable the distance sensors
for name in sensorsNames:
    sensors[name] = driver.getDistanceSensor('distance sensor ' + name)
    sensors[name].enable(10)

frontRange = sensors['front'].getMaxValue()

#define values for PID
kp = 0.12
ki = 0.0022
kd = 1

iMin = -1.0
iMax = 1.0

iSum = 0.0

oldY = 0.0
counter = 0;
while driver.step() != -1:
    # adjust the speed according to the value returned by the front distance sensor
    frontDistance = sensors['front'].getValue()
    speed = maxSpeed * frontDistance / frontRange
    driver.setCruisingSpeed(speed)
    # brake if we need to reduce the speed
    speedDiff = driver.getCurrentSpeed() - speed
    if speedDiff > 0:
        driver.setBrakeIntensity(min(speedDiff / speed, 1))
    else:
        driver.setBrakeIntensity(0)
    rightDistance = sensors['right'].getValue()
    # 6.0 - примерно середина полосы
    rightDiff = rightDistance - 2.85
    # up - пропорциональная составляющая, kp - коэффициент пропорциональной составляющей
    up=kp*rightDiff
    
    #Вычисляем интегральную составляющую.
    #iSum - сумма накопленных ошибок. Ошибка берется с минусом, 
    #потому что нам нужно исправлять её, а не увеличивать
    iSum-=rightDiff
    # Ограничим максимальную и минимальную сумму ошибок
    #Иначе раскачает
    if (iSum > iMax) : iSum=iMax
    else:
        if (iSum < iMin): iSum=iMin
    #ui - интегральная составляющая. ki - коэффициент интегральной составляющей
    ui= ki*iSum
    
    #ud - дифференциальная составляющая. kd - коэффициент дифференциальной составляющей
    #В дифференциальной составляющей определяется насколько мы продолжаем отклоняться от курса
    #независимо от работы пропорциональной составляющей. Если пропорциональной не хватает
    #дифференциальная добавит угол, Если пропорциональная будет излишне поворачивать, 
    #дифференциальная замедлит
    ud = kd* (rightDiff-oldY)
    
    #Вычисляем итоговый угол поворота
    sumAngle = up+ui+ud
    
    if (sumAngle > maxAngle) : sumAngle = maxAngle
    else:
        if (sumAngle < -maxAngle) : sumAngle = -maxAngle
    
    #Назначаем полученный угол
    driver.setSteeringAngle(sumAngle)
    
    #Запоминаем текущее значение отклонения от линии
    oldY = rightDiff
    
    if (counter == 1000) : 
        maxSpeed = 100
        maxAngle = 0.08
        kp= 0.07
        ki = 0.0066
        kd= 1
    else: 
        counter+=1
