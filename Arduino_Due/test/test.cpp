#include <Arduino.h>

void setup(){
    pinMode(2, OUTPUT);
    pinMode(3, OUTPUT);
}

void loop(){
    digitalWrite(2, HIGH);
    digitalWrite(2, HIGH);
}