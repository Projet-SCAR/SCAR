import time
import serial
import struct
import csv
from influxdb import InfluxDBClient

#Définition du client InfluxDB (ici cette même raspberry (localhost) et nom de la database)
client = InfluxDBClient(host='localhost', port=8086, database='ScarDB')
client.switch_database('ScarDB')

#Ouverture du fichier .csv pour pouvoir stocker les données dedans
d = open('receiver_data.csv','w',newline='')
w = csv.writer(d)

#Initialisation de la communication LoRa (port, baudrate)
lora = serial.Serial(port="/dev/ttyS0",baudrate=9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)


while True:
    
#Lecture des données reçues par LoRa
    data_read = lora.readline()

#Donnée lues mises sous forme de chaine de caractères
    data = str(data_read,'utf-8')

#Modification de certains éléments de la chaine de caractère
    #Par exemple les séparateurs
    L = data.replace("'","")
    L = L.replace("[","")
    L = L.replace("]","")
    L = L.replace(", ",",")
    
#Séparation de la chaine de caractères selon les différentes données, mises dans un tableau
    L = L.split(",")
    L[3] = L[3].replace("\n","")
 
#Ecriture des données dans le fichier 
    w.writerow(L)
    d.flush()
    
#Temporisation d'1s
    time.sleep(1)
    
#On récupère les valeurs des données si elles ne sont pas "NaN"
    if L[0] != 'NaN':
        temperature = float(L[0])
    if L[1] != 'NaN':
        humidite = float(L[1])
    if L[2] != 'NaN':
        luminosite = float(L[2])

# Création de la mesure InfluxDB
    temps = L[3]
    json_body = [
        {
            "measurement": "tps_reel",
        #Le temps correspondant aux mesures correspond au timestamp de la prise de mesure
            "time": temps,
        #Les valeurs des mesure :
            "fields": {
            "temperature": temperature,
            "humidite": humidite,
            "luminosite": luminosite,
            }
        }
        ]
# Écriture de la mesure dans la base de données InfluxDB
    client.write_points(json_body)