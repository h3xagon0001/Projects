#include <SPI.h>
#include <RF24.h>
#include <nRF24L01.h>

// left radio
#define LEFT_CE 21
#define LEFT_CSN 22

// right radio
#define RIGHT_CE 25
#define RIGHT_CSN 26

RF24 leftRadio(LEFT_CE, LEFT_CSN);
RF24 rightRadio(RIGHT_CE, RIGHT_CSN);


const byte address[6] = "00001";

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);

  if (!leftRadio.begin()) {
    Serial.println("Radio left hardware not responding!");
    while (1) {} // Hold program in infinite loop
  }

  if (!rightRadio.begin()) {
    Serial.println("Radio right hardware not responding!");
    while (1) {} // Hold program in infinite loop
  }

  Serial.println("WORKS");
}

void loop() {
  // put your main code here, to run repeatedly:

}
