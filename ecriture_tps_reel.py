import time
import serial
import struct
import csv
from influxdb import InfluxDBClient

client = InfluxDBClient(host='localhost', port=8086, database='ScarDB')
client.switch_database('ScarDB')

d = open('receiver_data.csv','w',newline='')
w = csv.writer(d)
lora = serial.Serial(port="/dev/ttyS0",baudrate=9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)
# data_read0 = lora.readline()
while True:
    data_read = lora.readline()
    #read data from other lora
#     if data_read:
#         print('++++')
#         print([data_read[:4],data_read[4:8],data_read[-4:]])
#         temp = struct.unpack('<f',data_read[:4])[0]
#         hum = struct.unpack_from('<f',data_read[0:8],4)[0]
#         lum = struct.unpack('<f',data_read[-4:])[0]
#         print([temp,hum,lum])
    data = str(data_read,'utf-8')
#     if data_read0 != data_read:
#         print("********")
#         data_read0 = data_read#Conversion des bytes
#     print(data_read)
    L = data.replace("'","")
    L = L.replace("[","")
    L = L.replace("]","")
    L = L.replace(", ",",")
    L = L.split(",")
    L[3] = L[3].replace("\n","")
 
    w.writerow(L)
    d.flush()
    time.sleep(1)
    
    
    if L[0] != 'NaN':
        temperature = float(L[0])
    if L[1] != 'NaN':
        humidite = float(L[1])
    if L[2] != 'NaN':
        luminosite = float(L[2])
    temps = L[3]
        # Création de la mesure InfluxDB
    json_body = [
        {
            "measurement": "tps_reel",
            "time": temps,
            "fields": {
            "temperature": temperature,
            "humidite": humidite,
            "luminosite": luminosite,
                #"time_real": notre_time
            }
        }
        ]
        # Écriture de la mesure dans la base de données InfluxDB
    client.write_points(json_body)