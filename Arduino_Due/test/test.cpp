#include <Arduino.h>
#include <Stepper.h>

const int stepsPerRevolution = 200;

Stepper ms(stepsPerRevolution, 2,3,4,5);

void setup(){
    ms.setSpeed(60);
    Serial.begin(9600);
}

void loop(){
    Serial.println("clockwise");
    ms.step(stepsPerRevolution);
    delay(500);

    Serial.println("counter clockwise");
    ms.step(-stepsPerRevolution);
    delay(500);
}