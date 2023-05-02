#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <DHT.h>
#include <DHT_U.h>
#include "rgb_lcd.h"
#include "Arduino.h"
//1: toggle mode, 2: follow mode
#define LED_MODE   1
#define SLAVE_ADDRESS 0x8


#define DHTPIN 5     // Digital pin connected to the DHT sensor 
// Feather HUZZAH ESP8266 note: use pins 3, 4, 5, 12, 13 or 14 --
// Pin 15 can work but DHT must be disconnected during program upload.

// Uncomment the type of sensor in use:
//#define DHTTYPE    DHT11     // DHT 11
#define DHTTYPE    DHT22     // DHT 22 (AM2302)
//#define DHTTYPE    DHT21     // DHT 21 (AM2301)

// See guide for details on sensor wiring and usage:
//   https://learn.adafruit.com/dht/overview

DHT_Unified dht(DHTPIN, DHTTYPE);

uint32_t delayMS;

int sensorPin = A0;    // select the input pin for the potentiometer
int sensorValue = 0;  // variable to store the value coming from the sensor


const int ledPin = 3;      // the number of the LED pin, D3
const int buttonPin = 4;    // the number of the pushbutton pin, D4
const boolean breathMode = true;  // if or not the led lights as breath mode when it's on
 
// Variables will change:
int ledState = LOW;         // the current state of the output pin
int ledFadeValue = 0;
int ledFadeStep = 5;
int ledFadeInterval = 20;   //milliseconds
int buttonState;             // the current reading from the input pin
int lastButtonState = HIGH;   // the previous reading from the input pin
 
unsigned long lastDebounceTime = 0;  // the last time the output pin was toggled
unsigned long debounceDelay = 50;    // the debounce time; increase if the output flickers
unsigned long lastLedFadeTime = 0;

String data = "";
float ftemp;
unsigned char temp[4] = {0};
float fhum;
unsigned char hum[4] = {0};
float flum;
unsigned char lum[4] = {0};
String virgule = ",";
String pv = ";";
void setup() {
    // initialize i2c as slave.
    Serial.begin(9600);
    Wire.begin(SLAVE_ADDRESS);
    Wire.onRequest(sendData); 
    dht.begin();
    sensor_t sensor;
    delayMS = sensor.min_delay / 1000;
    dht.temperature().getSensor(&sensor);
    dht.humidity().getSensor(&sensor);

}

void loop() {
    sensors_event_t event;
    dht.temperature().getEvent(&event);
    if (isnan(event.temperature)) {
      Serial.println(F("Error reading temperature!"));
    }
    else {
      Serial.print(F("Temperature: "));
      Serial.print(event.temperature);
      Serial.println(F("°C"));
//      String data0 = String(event.temperature + 273.2);
      ftemp = event.temperature;
      memcpy(temp,&ftemp,4);
//      data = data + data0;
//      data[data.length()-1] = ;
//      data = data + virgule;
    }
    // Get humidity event and print its value.
    dht.humidity().getEvent(&event);
    if (isnan(event.relative_humidity)) {
      Serial.println(F("Error reading humidity!"));
    }
    else {
      Serial.print(F("Humidity: "));
      Serial.print(event.relative_humidity);
      Serial.println(F("%"));
      fhum = event.relative_humidity;
      memcpy(hum,&fhum,4);
//      String data0 = String(event.relative_humidity);
//      data = data +data0;
//      data = data + virgule;
    }
    flum = analogRead(sensorPin);
    memcpy(lum,&flum,4);
//    String data0 = String(datasensor);
//    data = data +data0;
//    data = data + pv;
//    Serial.println(data);
}

int index = 0;


// callback for sending data
void sendData() { 
  Wire.write(temp,4);
  Wire.write(hum,4);
  Wire.write(lum,4);
//    Wire.write(data[index]);
//    ++index;
//    if (index >= 16) {
//         index = 0;
//    }
 }
