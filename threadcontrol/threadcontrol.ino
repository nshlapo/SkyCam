#include <Stepper.h>

const int stPerRev = 400;  // change this to fit the number of steps per revolution
int moveM = 0;
// for your motor

// initialize the stepper library on pins 8 through 11:
Stepper wStepper(stPerRev, 10, 11);
Stepper eStepper(stPerRev, 5, 6);

void setup() {
  // set the speed at 60 rpm:
  wStepper.setSpeed(40);
  eStepper.setSpeed(40);
  // initialize the serial port:
  Serial.begin(9600);
}

void threadStep(int stepping, int wDir, int eDir) {
  for(int i=0; i<stepping; i=i+1) {
    wStepper.step(wDir*stPerRev/200);
    eStepper.step(eDir*stPerRev/200);
    // delay(5);
  }
}

void loop() {
  if (Serial.available() > 0) {
    moveM = Serial.parseInt();
  }

  if (moveM == 2) {
    threadStep(50, 1, 1);
  }
  if (moveM == 1) {
    threadStep(50, -1, -1);
    }

  if (moveM == 3) {
    threadStep(50, 1, -1);
      }

  if (moveM==4) {
    threadStep(50, -1, 1);
  }

}