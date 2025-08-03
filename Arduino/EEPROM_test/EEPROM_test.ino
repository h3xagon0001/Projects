#include <EEPROM.h>

int address = 0;
const int rows = 10;
float coordinates[rows][2] = {
  {1.2f,    5.45f},
  {4.2f,    3.335f},
  {0.321f,  -5.55f},
  {9.99f,   0.1001f},
  {11.477f, -0.12f}
};


void setup()
{
  Serial.begin(9600);
  while (!Serial) { } // wait for serial port to connect. Needed for native USB
  Serial.println(EEPROM.length());

  // write
  EEPROM.update(address, coordinates);
  Serial.println("Success.");

  // read
  EEPROM.get(address, coordinates);

  for (int row = 0; row < 5; row++) {
    Serial.print(coordinates[row][0]);
    Serial.print(", ");
    Serial.println(coordinates[row][1]);
  }
}

void loop() { }
