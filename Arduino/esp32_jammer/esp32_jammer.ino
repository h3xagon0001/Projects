#include <SPI.h>
#include <RF24.h>
#include <nRF24L01.h>

// left radio
#define LEFT_CE 21
#define LEFT_CSN 22

// right radio
#define RIGHT_CE 25
#define RIGHT_CSN 26

SPIClass *vspi_pointer = nullptr;
SPIClass *hspi_pointer = nullptr;

// init radios
RF24 leftRadio(LEFT_CE, LEFT_CSN, 16000000);
RF24 rightRadio(RIGHT_CE, RIGHT_CSN, 16000000);

void setup() {
  // put your setup code here, to run once:

  // init vspi and hspi
  vspi_pointer = new SPIClass(VSPI);
  hspi_pointer = new SPIClass(HSPI);
  
  vspi_pointer->begin();
  hspi_pointer->begin();

  Serial.begin(115200);

  if (!leftRadio.begin(vspi_pointer)) {
    Serial.println("Left radio is not responding.");
    while (1) {} // Hold program in infinite loop
  }

  if (!rightRadio.begin(hspi_pointer)) {
    Serial.println("Right radio is not responding.");
    while (1) {} // Hold program in infinite loop
  }

  Serial.println("Both radios initialised successfully.");

  // radio setup
  leftRadio.stopListening();
  rightRadio.stopListening();
  leftRadio.setAutoAck(false);
  rightRadio.setAutoAck(false);
  leftRadio.setRetries(0, 0);
  rightRadio.setRetries(0, 0);
  leftRadio.setPALevel(RF24_PA_MAX, false);
  rightRadio.setPALevel(RF24_PA_MAX, false);
  leftRadio.setDataRate(RF24_250KBPS);
  rightRadio.setDataRate(RF24_250KBPS);
  leftRadio.printPrettyDetails();
  rightRadio.printPrettyDetails();
  
  leftRadio.startConstCarrier(RF24_PA_MAX, 0);
  rightRadio.startConstCarrier(RF24_PA_MAX, 0);
}

void loop() {
  // put your main code here, to run repeatedly:
  leftRadio.setChannel(random(81));
  rightRadio.setChannel(random(81));
}
