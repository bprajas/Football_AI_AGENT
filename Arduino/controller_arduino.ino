void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    int cmd = Serial.read() - '0';  // '0' to '2'

    switch (cmd) {
      case 0: // Shoot
        // digitalWrite or USB HID command here
        break;
      case 1: // Pass
        break;
      case 2: // Dribble
        break;
    }

    Serial.print("Action: "); Serial.println(cmd);
  }
}
