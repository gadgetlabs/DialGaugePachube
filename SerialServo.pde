#include <Servo.h>
 
Servo myservo;  // create servo object to control a servo
 
int maxVal = 950;
int minVal = 50;

int v;    // variable to read the value from the analog pin
 
void setup()
{
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
}
 
void loop()
{
  
  v = 0;

  if ( Serial.available()) {
    char ch = Serial.read();

    switch(ch) {
      case '0'...'9':
        v = v * 10 + ch - '0';
        break;
      case 's':
        
        if (v > maxVal)
        {
          v = maxVal;
        }
        else if (v < minVal)
        {
          v = minVal;
        }
        
        v = map(v, 0, 1023, 0, 179); // scale it to use it with the servo (value between 0 and 180)
      
        myservo.write(v); // sets the servo position according to the scaled value
        v = 0;
        break;
    }
  }
  delay(15);

}