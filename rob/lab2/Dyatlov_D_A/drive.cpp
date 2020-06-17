// File: drive
// Date: 12.06.2020
// Author:Dyatlov D.A.


#include <webots/Robot.hpp>
#include <webots/Motor.hpp>



using namespace webots;
#define TIME_STEP 64

int main(int argc, char **argv) {

  Robot *robot = new Robot();
  Motor *left_motors = robot->getMotor("left wheel motor");
  Motor *right_motors = robot->getMotor("right wheel motor");
  
  left_motors->setPosition(700);
  right_motors->setPosition(700);
  
  left_motors->setVelocity(2.2);
  right_motors->setVelocity(2);
  
  while (robot->step(TIME_STEP) != -1) {
   
  };

  delete robot;
  return 0;
}
