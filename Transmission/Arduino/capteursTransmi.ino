/*
   Ce programme sert à récupérer les données des capteurs, puis de les envoyer via liaison I2C à la raspberry.
   Les données seront transmises capteur par capteur et on force l'écriture sur 4 octets afin d'éviter des problèmes de compréhension côté raspberry.
   Pour récupérer les données de température et d'humidité, on utilise les fonctions constructeurs dht comme dans l'exemple fournie dans la documentation 
   (Ce code est le code de la documentation mais adaptée à notre problème, d'où les commentaires en anglais).
*/

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

 
unsigned long lastDebounceTime = 0;  // the last time the output pin was toggled
unsigned long debounceDelay = 50;    // the debounce time; increase if the output flickers
unsigned long lastLedFadeTime = 0;

// Définition variables utilisées, le type char correspond au type octet (ou byte) car ce dernier n'existe pas en C

float ftemp;
unsigned char temp[4] = {0};
float fhum;
unsigned char hum[4] = {0};
float flum;
unsigned char lum[4] = {0};


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
    // Récupération de la température
    dht.temperature().getEvent(&event);
    if (isnan(event.temperature)) {
      Serial.println(F("Error reading temperature!"));
    }
    else {
      Serial.print(F("Temperature: "));
      Serial.print(event.temperature);
      Serial.println(F("°C"));
      ftemp = event.temperature;
      memcpy(temp,&ftemp,4);
    }
    // Récupération de l'humidité
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
    }
    flum = analogRead(sensorPin);
    memcpy(lum,&flum,4);
}

int index = 0;


// Fonction pour envoyer les données
void sendData() { 
  Wire.write(temp,4);
  Wire.write(hum,4);
  Wire.write(lum,4);
 }
