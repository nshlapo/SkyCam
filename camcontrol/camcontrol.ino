#include <Stepper.h>

const int stPerRev = 400;  // change this to fit the number of steps per revolution
int moveM = 0;
// for your motor

// initialize the stepper library on pins 8 through 11:
Stepper wStepper(stPerRev, 10, 11);
Stepper eStepper(stPerRev, 5, 6);

void setup() {
  // set the speed at 60 rpm:
  wStepper.setSpeed(80);
  eStepper.setSpeed(80);
  // initialize the serial port:
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    moveM = Serial.parseInt();
  }

  if (moveM == 2) {
    wStepper.step(.1*stPerRev);
  }
  if (moveM == 1) {
    wStepper.step(-.1*stPerRev);
    }

  if (moveM == 3) {
    // wStepper.step()
      }
  // eStepper.step(10*stPerRev);
  // delay(50);


  // eStepper.step(-10*stPerRev);
  // delay(50);
}