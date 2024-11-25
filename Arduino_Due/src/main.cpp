#include <Arduino.h>
#include <stdio.h>
#include <stdlib.h>  
#include <string.h>
#include <Servo.h>

#define ARM_1_PIN 2
#define ARM_2_PIN 3
#define DRAW_ARM_PIN 4

Servo arm_1;
Servo arm_2;
Servo draw_arm;

float last_a1 = 0;
float last_a2 = 0;

int i = 0;

void test(){
  i = i+0.5;
  arm_1.write(i);
  if(i == 180){
    i = 0;
  }
  delay(50);
}

void move_arms(){
  if(Serial.available() > 5){
    String data = Serial.readString();

    String a1_str = data.substring(0,3);
    String a2_str = data.substring(3,6);
    int a1 = atoi(a1_str.c_str());
    int a2 = atoi(a2_str.c_str());
    Serial.println(a1);
    if(a1 != last_a1){
      arm_1.write(a1);
    }
    if(a2 != last_a2){
      arm_2.write(a2);
    }
    last_a1 = a1;
    last_a2 = a2;
  }
}

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(2);
  arm_1.attach(ARM_1_PIN);
  arm_2.attach(ARM_2_PIN);
  arm_1.write(0);
  arm_2.write(0);
}

void loop() {
  // test();
  move_arms();
}



// put function definitions here:
