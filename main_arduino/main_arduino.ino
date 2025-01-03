#include <Servo.h>

Servo servo1; // Create servo object for the first motor
Servo servo2; // Create servo object for the second motor
int i;
void setup() {
  Serial.begin(9600);  // Start serial communication
  servo1.attach(3);    // Attach servo1 to pin 3
  servo2.attach(6);    // Attach servo2 to pin 6
  i = 0;
}


void python_command_reciever() {
  if (Serial.available() > 0) {
    char command = Serial.read(); // Read the incoming command
    if (command == '1') {
      servo1.write(0);  // Move servo1 to 0 degrees
      servo2.write(0);  // Move servo2 to 0 degrees
    } else if (command == '2') {
      servo1.write(90); // Move servo1 to 90 degrees
      servo2.write(90); // Move servo2 to 90 degrees
    } else if (command == '3') {
      servo1.write(180); // Move servo1 to 180 degrees
      servo2.write(180); // Move servo2 to 180 degrees
    }
  }

}

int pos = 0, MAX_ANGLE=180, MIN_ANGLE=0;

void test_servo(Servo test_servo){
  for(pos = MIN_ANGLE; pos <= MAX_ANGLE; pos += 1){
    test_servo.write(pos);
    delay(15);
  }
  for(pos = MAX_ANGLE; pos >= MIN_ANGLE; pos -= 1){
    test_servo.write(pos);
    delay(15);
  }
}


void loop(){
  // test_servo(servo1);
}