import com.cyberbotics.webots.controller.DistanceSensor;
import com.cyberbotics.webots.controller.Motor;
import com.cyberbotics.webots.controller.Robot;

public class pioneer2 {

  public static void main(String[] args) {

    double max_speed = 10.0;
    double speed_unit = 0.1;
    int num_sensors = 16;
    
    DistanceSensor[] sensor = new DistanceSensor [num_sensors];
    
    Robot robot = new Robot();
    int timeStep = (int) Math.round(robot.getBasicTimeStep());

    for (int i=0; i<num_sensors; i++){
        sensor[i] = robot.getDistanceSensor("ds"+i);
        sensor[i].enable(timeStep);
    }
    
    double leftSpeed = 8.5;
    double rightSpeed = 8.5;
    
    Motor leftMotor = robot.getMotor("left wheel motor");
    Motor rightMotor = robot.getMotor("right wheel motor");
    leftMotor.setPosition(Double.POSITIVE_INFINITY);
    rightMotor.setPosition(Double.POSITIVE_INFINITY);
    leftMotor.setVelocity(leftSpeed);
    rightMotor.setVelocity(rightSpeed);
    
    System.out.println ("The "+robot.getName() + " robot is initialized, it uses " + num_sensors+" distance sensors");
    
    // Main loop:
    while (robot.step(timeStep) != -1) {
        if ((sensor[0].getValue() >100) || (sensor[15].getValue() >100) ||(sensor[1].getValue() >100) || (sensor[14].getValue() >100)) {
    		leftMotor.setVelocity(0);
    		rightMotor.setVelocity(10);
    	}
    	else {
            leftMotor.setVelocity(leftSpeed);
    		rightMotor.setVelocity(rightSpeed);
    	}
    };
    
    // Enter here exit cleanup code.
  }
}
