#include<Servo.h>
Servo servomotor;
int trigPin=6;
int echoPin=4;
float time;
float distance;
void setup() {
  servomotor.attach(9);
  pinMode(trigPin,OUTPUT);
  pinMode(echoPin,INPUT);
}

void loop() {
  measuredistance();
  servomotor.write(0);
  if (distance<10)
  servomotor.write(90);
  else
  servomotor.write(0);
  }
  void measuredistance()
  {
    digitalWrite(trigPin,LOW);
    digitalWrite(trigPin,HIGH);
    delay(1000);
    digitalWrite(trigPin,LOW);
    time=pulseIn(echoPin,HIGH);
    distance=time*343/20000;
  }
